#!/usr/bin/perl -w

print "unesi niz znakova:\n";
chomp($niz = <STDIN>);
print "unesi broj ponavljanja:\n";
chomp($n=<STDIN>);
for my $i (1..$n){
 print "$niz\n";
}