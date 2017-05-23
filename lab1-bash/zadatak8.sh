#!/bin/sh

if [ $# != 1 ]
then
	echo "Potreban je 1 argument."
	exit 1
fi

dat=$1

if [ ! -r "$dat" ]
then
	echo "Datoteka nije čitljiva."
	exit 1
fi

cat "$dat" | cut -d':' -f 2 | sort | uniq -c | awk '{ print $2 " " $1}'