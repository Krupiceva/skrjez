#!/bin/sh

odrediste=$( eval "echo \${$#}" ) #Da nebi slucajno bio dvoznamenkasti broj!!!

if [ ! -d "$odrediste" ] 
then
    mkdir "$odrediste"
    echo "Kreiran direktorij $odrediste"
fi

preneseno=0

for dat in "${@:1:$(($#-1))}" #podlista od liste argumenata (bez zadnjeg)
do  
    if [ -f "$dat" -a -r "$dat" ]
then 
        cp "$dat" "$odrediste"   
        ((preneseno+=1))     
    else
        echo "Datoteka - "$dat" - ne postoji ili nije čitljiva!"
    fi
done

echo "Broj datoteka kopirano u "$odrediste": "$preneseno""
