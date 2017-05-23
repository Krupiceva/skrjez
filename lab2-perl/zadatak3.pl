#!/usr/bin/perl -w

$isNewHour=0;

while(<>){
	@nameOfFile = split /\./, $ARGV;
	$date = $nameOfFile[1];

	$line = $_;

	@tempSplit = split /\[/, $line;
	@tempSplit1 = split /:/, $tempSplit[1];

	$hour = $tempSplit1[1];

	if ($isNewHour == 0){
		print " \nDatum: $date \n";
		print "Sat : Broj pristupa \n";
		print "------------------------------- \n";
		$isNewHour = 1;
	}

	if($isNewHour == 1){
		$numberOfAction[$hour] += 1;
	}

	if(eof){
		for($i=0; $i<24; $i++){
			print " $i : $numberOfAction[$i] \n";
			$numberOfAction[$i]=0;
		}
		$isNewHour = 0;
	}

}
