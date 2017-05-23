#!/usr/bin/perl -w


$encrLetter = shift(@ARGV);
while ($line = <>){
	#chomp;
    #tr/A-Z/a-z/;
	#$line = $_;
	@allChars = split("", $line);
	$shift = ord($encrLetter) - 97; #97 je a, time smo dobili pomak
	#asci(a)=97 asci(z)=122
	$i=0;
	foreach $letter (@allChars){
		$asciiLetter = ord($letter);
		#velika slova pretvorimo u mala (dodamo 32)
		if($asciiLetter >= 65 && $asciiLetter <= 90){
			$asciiLetter = $asciiLetter + 32;
		}
		#samo ako je vrijednost izmedju 97 i 122 onda je slovo i treba ga sifrirat
		#u suprotnom samo prekopiramo znak
		if($asciiLetter >= 97 && $asciiLetter <=122){
			#skalirat cemo 97 u 0
			$asciiLetter = $asciiLetter - 97;
			$shiftLetter = ($asciiLetter + $shift) % 26;
			#skaliramo natrag na ascii ali velika slova
			$shiftLetter = $shiftLetter + 97 - 32;
			$letter = chr($shiftLetter);
		}
		$allEncript[$i] = $letter;
		$i++;
	}

	foreach $newLetter (@allEncript){
		print "$newLetter";
	}

}
print "\n";