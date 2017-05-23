#!/usr/bin/perl -w

print "Unesite brojeve: \n";
@listaUcitanihBrojeva=<STDIN>;
$suma=0;
$velicinaPolja=@listaUcitanihBrojeva;
foreach my $broj (@listaUcitanihBrojeva){
 $suma += $broj;
}
$aritmetickaSredina=$suma/$velicinaPolja;
print "Aritmeticka sredina unesenih brojeva je: $aritmetickaSredina.\n";
