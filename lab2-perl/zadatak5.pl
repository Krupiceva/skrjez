#!/usr/bin/perl -w

#use open ':locale';
use locale;
while($line = <>){
	#drugiredak su faktori
	if($. == 2) {
		@factors = split(";", $line);
	}
	#od petog retka pocinju podaci
	if($. > 4){
		$sum = 0;
		@splits = split(";", $line);
		$jmbag = $splits[0];
		$lastName = $splits[1];
		$firstName = $splits[2];
		for($i=3; $i<=9; $i++){
			next if $splits[$i] eq "-";
			$points = $splits[$i];
			$points = $points * $factors[$i-3];
			$sum += $points;
		}

		$key = join(' ', "$lastName,", "$firstName", "($jmbag)");
        $rangList{$key}= $sum;
	}



}
$i=1;
print "Lista po rangu:" . "\n";
print "---------------------" . "\n";
foreach $jmbag ( sort { $rangList{$b} <=> $rangList{$a} } keys %rangList) {
        print "   $i. $jmbag : " . $rangList{$jmbag} . "\n";
        $i++;
}