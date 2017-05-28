'''
Created on May 27, 2017

@author: krupiceva
'''
import sys

print ("Hyp#Q10#Q20#Q30#Q40#Q50#Q60#Q70#Q80#Q90")
datName = sys.argv[1]
with open(datName, 'r') as dat:
    lines = dat.readlines()
    for i in range(0,len(lines)):
        stringLine = "{0:0>3}".format(int(i+1)) + "#" #formatiraj s nulama ispred, ako nema vise od 100 hipoteza!
        line=lines[i]
        numbers = [float(i) for i in line.split(" ")]
        numbers = sorted(numbers)
        for i in range(1,10):
            q = i * 0.1
            hdindex = int(q * len(numbers)) #nije specificirano kako treba zaokruzivati
            hd = numbers[hdindex]
            stringLine += str(hd) + "#"
        stringLine = stringLine[:-1]
        print (stringLine)
    