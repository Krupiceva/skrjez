#!/bin/sh

#provjera argumenata
if [ $# != 2 ]
then
	echo "Potrebna su 2 argumenta."
	exit 1
fi

izvor="$1"
odrediste="$2"

if [ ! -d $odrediste ]
then
	mkdir "$odrediste"
fi

for slika in $(ls $izvor)
do 
    datum=$(stat -c %y $izvor/$slika | cut -d'-' -f1,2)   
    if [ ! -d $odrediste/$datum ] 
    then
        mkdir $odrediste/$datum
    fi
    mv $izvor/$slika $odrediste/$datum
done