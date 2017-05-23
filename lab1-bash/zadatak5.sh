#!/bin/sh

#provjera argumenata
if [ $# != 2 ]
then
	echo "Potrebna su 2 argumenta."
	exit 1
fi

echo "$@" ; echo

direktorij=$1
uzorak=$2
declare -i br=0

OldIFS="$IFS"
IFS=$'\n'
for file in $(find "$direktorij" -name "$uzorak"); do
    br+=$(($(wc -l "$file" | cut -d' ' -f1) ))
done
IFS="OldIFS"
echo $br