#!/bin/sh
 for log in $(ls localhost_access_log.[0-9][0-9][0-9][0-9]-02-*) 
 do
    echo $log | sed -r 's/.*\.([0-9]+)-([0-9]+)-([0-9]+).*/datum: \3-\2-\1/'
    echo "-----------------------------------------------------"
    cat $log | cut -d'"' -f 2 | sort | uniq -c | sort -rn | sed -r 's/\s+([0-9]*)(\s+)(.*)/    \1  :  \3/' 
    echo
done