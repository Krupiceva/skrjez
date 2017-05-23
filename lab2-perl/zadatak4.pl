#!/usr/bin/perl -w

while(<>){
	$line = $_;
	@splits = split /;/, $line;
	$jmbag = $splits[0];
	$lastName = $splits[1];
	$firstName = $splits[2];
	$times = $splits[3];
	$lock = $splits[4];

	@splits1 = split / /, $times;
	$startDate = $splits1[0];
	$startTimeFull = $splits1[1];

	@splits2 = split / /, $lock;
	$endDate = $splits2[0];
	$endTimeFull = $splits2[1];

	@splits3 = split /:/, $startTimeFull;
	$startTime = $splits3[0];

	@splits4 = split /:/, $endTimeFull;
	$endTime = $splits4[0];

	if ($startDate ne $endDate || $startTime ne $endTime){
		print "$jmbag $lastName $firstName - PROBLEM: $startDate $startTimeFull --> $endDate $endTimeFull";
	}



}