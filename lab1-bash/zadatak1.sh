#!/bin/sh
proba="Ovo je Proba"
echo $proba ; echo

lista_datoteka=* ; echo $lista_datoteka ; echo

proba3=""
for i in 1 2 3
do
	proba3+="${proba}. "
done
echo $proba3 ; echo

a=4 ; b=3 ; c=7
d=$(( ($a+4)*$b%$c )) ; echo $d ; echo


broj_rijeci=$(cat *.txt | wc -w) ; echo $broj_rijeci ; echo

ls ~ ; echo

cat /etc/passwd | cut -d':' -f1,6,7 ; echo

ps -ef | tr -s ' ' | cut -d' ' -f1,2,8 ; echo