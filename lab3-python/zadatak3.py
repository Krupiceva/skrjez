'''
Created on May 27, 2017

@author: krupiceva
'''

import sys
import os
import re

#nije definirano sta pisemo ako neki student nije pristupio nekoj vjezbi
#ili sta pisemo ako datoteke s nekim brojem vjezbe nema
#moje rjesenje uzima zadnji najveci broj vjezbe i ispisuje za svakog studenta bodove za sve vjezbe, ukoliko nema podataka pise -

#Rjecnik unutar kojeg ce value bit novi rjecnik
student={}
zadnjaVjezba = 0
header = "{:15s}{:23s}".format("JMBAG", "Prezime, ime") #duljina string plus 10 mjesta
datName = sys.argv[1]
with open(datName, 'r') as dat:
    #Napravi listu koja sadrzi retke datoteke
    lines = dat.readlines()
    for i in range (0, len(lines)):
        #Razdvoji redak sa separatorom razmaka i makni \n sa zadnjeg elementa
        #Iteriraj kroz listu koja se dobi splitanjem i stvori novu listu
        #Oblik: 'jmbag prezime ime'
        line = [i.rstrip('\n') for i in lines[i].split(" ")]
        JMBAG = line[0]
        prezime = line[1]
        ime = line[2]
        student[JMBAG] = {'prezime': prezime, 'ime': ime} #rjesnik unutar rjecnika

#Prodji kroz sve datoteke u trenutnom direktoriju  
for d in os.listdir('.'):
    #Ako su oblika Lab_xx_gxx gdje su xx brojevi 0-99
    if re.match(r"Lab_[0-9][0-9]_g[0-9][0-9]", d):
        with open(d, 'r') as dat:
            #Napravi listu koja sadrzi retke datoteke
            lines = dat.readlines()
            for i in range(0, len(lines)):
                #Razdvoji redak sa separatorom razmaka i makni \n sa zadnjeg elementa
                #Iteriraj kroz listu koja se dobi splitanjem i stvori novu listu
                #Oblik: 'jmbag broj_bodova'
                line = [i.rstrip('\n') for i in lines[i].split(" ")]
                JMBAG = line[0]
                brBodova = line[1]
                #uzmi broj vjezbe iz imena datoteke 
                brVjezbe = int(re.search(r"Lab_([0-9][0-9])_g[0-9][0-9]", d).group(1))
                #zadnja vjezba nam treba kako bi znali do koje vjezbe se doslo
                zadnjaVjezba = max(zadnjaVjezba, brVjezbe)
                brVjezbe = "L" + str(brVjezbe)
                #Sprjeci prepisivanje vec postojecih podataka
                if brVjezbe in student[JMBAG].keys():
                    print ("Vec su uneseni bodovi za vjezbu " + brVjezbe + " za studenta pod JMBAGOM: " + JMBAG )
                else:
                    student[JMBAG][brVjezbe] = brBodova

#Stvori u headeru stupce za sve vjezbe
for i in range(0, zadnjaVjezba):
    br = "L" + str(i+1)
    header += "{:6s}".format(br)

#ispis 
print(header)
stringLine = ""
for jmbag in student:
    stringLine = "{:15s}".format(jmbag)
    ime = student[jmbag].get('prezime') + ", " + student[jmbag].get('ime')
    stringLine += "{:23s}".format(ime)
    for i in range(0, zadnjaVjezba):
        br = "L" + str(i+1)
        #Ako za tog studenta nema zapisa za tu vjezbu stavi -
        stringLine += "{:6s}".format(student[jmbag].get(br, '-'))
    print (stringLine)

    

    