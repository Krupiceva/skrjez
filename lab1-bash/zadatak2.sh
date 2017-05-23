#!/bin/sh
grep -iE 'banana|jabuka|jagoda|dinja|lubenica' namirnice.txt ; echo

grep -viE 'banana|jabuka|jagoda|dinja|lubenica' namirnice.txt > ne-voce.txt ; echo 

grep -nrE '[A-Z]{3}[0-9]{6}' ~/projekti ; echo

find ~/ -mtime +7 -a -mtime -14 ; echo

for i in $(seq 15) ; do echo -n "$i " ; done ; echo