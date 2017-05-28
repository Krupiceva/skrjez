'''
Created on May 27, 2017

@author: krupiceva
'''

#Rijetke matrice pohranjujem u rijecnik
#Cijele matrice pohranjujem u ugnjezdjene liste
import sys

wholeMat1 = []
wholeMat2 = []
result = []
res = {}

#Funkcija koja ucitava matrice iz datoteke u rijetkom obliku i sprema ih u rjecnik
def ucitajMatricu(mat):
    parsMat = {}
    line = mat.split('\n')
    #prva linija je velicina  
    parsMat['velicina'] = line[0]
    #od druge linije nadalje su zapisi u matrici
    for i in range(1, len(line)):
        temp = line[i].split(" ")
        row = temp[0]
        col = temp[1]
        val = temp[2]
        key = row + " " + col
        parsMat[key] = val
    return parsMat

#Funkcija koja provjerava mogu li se dvije matrice pomnoziti
#broj stupaca prve mora biti isti broju redaka druge
def provjeriIspravnost(mat1, mat2):
    vel1 = mat1['velicina']
    vel2 = mat2['velicina']
    temp = vel1.split(" ")
    #broj stupaca prve
    m1 = temp[1]
    temp = vel2.split(" ")
    #broj redaka druge
    n2 = temp[0]
    if m1 == n2: return True
    else: return False

#Funkcija koja od rjecnika tj rijetke matrice radi cijelu matricu u obliku ugnjezdjene liste
#stavlja nule na elemente kojih nema u rjecniku
def napraviCijeluMatricu(mat):
    r, s = mat['velicina'].split(' ')
    #Napravi nul matricu danih velicina:
    #Napravi listu koja ima elemenata koliko ima stupaca i takvih listi unutar liste kolko ima redaka
    wholeMat = [[0 for x in range(int(s))] for y in range(int(r))]
    #popuni mjesta u matrici za par redak,stupac koji postoji
    for keys in mat:
            if keys != 'velicina': 
                r, s = keys.split(" ")
                #oduzmi 1 jer indexi u listi unutar liste idu od 0
                wholeMat[int(r)-1][int(s)-1] = float(mat[keys])
    return wholeMat
    
#Funkcija koja mnozi matrice, mnozi matrice u cijelom obliku tj listama   
def pomnoziMatrice(mat1, mat2):
    #rezultantna matrica ima redaka koliko redaka ima prva matrica i stupaca koliko stupaca ima druga matrica
    res = [[0 for x in range(len(mat2[0]))] for y in range(len(mat1))]
    # iteriraj kroz redove prve matrice
    for i in range(len(mat1)):
        # iteriraj kroz stupce druge matrice
        for j in range(len(mat2[0])):
            # iteriraj kroz redove druge matrice
            for k in range(len(mat2)):
                res[i][j] += mat1[i][k] * mat2[k][j]
                res[i][j] = float(res[i][j])
    return res

#Funkcija koja od liste tj cijele matrice radi rijetku matricu u obliku rjecnika
#za elemente koji su 0 ne stavlja zapise u rjecnik
def napraviRijetkuMatricu(mat):
    rMar = {}
    r = len(mat)
    s = len(mat[0])
    rMar['velicina'] = str(r) + " " + str(s)
    #index reda
    i = 0
    #iteriraj po redovima
    for row in mat:
        i += 1
        #index stupca
        j = 0
        #iteriraj po stupcima
        for col in row: 
            j += 1
            #ako je vrijednost u matrici razlicita od 0
            if col != 0:
                key = str(i) + " " + str(j)
                rMar[key] = str(col)
    return rMar

#Funkcija koja zapisuje rijetku matricu u datoteku
def zapisiRijetkuMatricuUDat(mat):
    with open('umnozak_matrica.txt', 'w') as dat:
        dat.write(mat['velicina'] + '\n')
        for keys in mat:
            if keys != 'velicina':
                dat.write(keys + ' ' + "{:3.2f}".format(float(mat[keys])) + '\n')      

datName = sys.argv[1]
with open(datName, 'r') as dat:
    lines = dat.read()
    #print(repr(lines)) #provjerevam kako izgleda prazan red \n\n ili \r\n\r\n
    #odvoji zapise matrica
    mats =lines.split('\n\n')
    mat1 = ucitajMatricu(mats[0])
    mat2 = ucitajMatricu(mats[1])
    if provjeriIspravnost(mat1, mat2):
        wholeMat1 = napraviCijeluMatricu(mat1)
        wholeMat2 = napraviCijeluMatricu(mat2)
        result = pomnoziMatrice(wholeMat1, wholeMat2)
        #Ispisi rezultantnu matricu u cijelom obliku
        for r in result:
            print(r)
        res = napraviRijetkuMatricu(result)
        zapisiRijetkuMatricuUDat(res)
        
    else: 
        print("Matrice se ne mogu mnoziti ako broj stupaca prve nije isti broju redaka druge")
    