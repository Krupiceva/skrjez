'''
Created on May 28, 2017

@author: krupiceva
'''
import sys
import urllib.request
import re

hosts = {}
mails = []
stranica = urllib.request.urlopen(sys.argv[1])
mybytes = stranica.read()
stringPage = mybytes.decode("utf8")
#Ispisi cijelu stranicu
#print(stringPage)

#Pronadji sve linkove
linkovi = re.findall(r'href="htt[ps].*?"', stringPage) #non greedy .*? greedy .*
print("Linkovi: ")
#Iteriraj kroz linkove 
for lin in linkovi:
    #uzmi samo adrese bez href taga
    link  = re.search(r'href="(htt[ps].*?)"', lin).group(1)
    print (link)
    #makni www ako postoji jer to nije dio hosta
    link = re.sub(r'www\.', "", link)
    #pronadi host u linku
    host = re.search(r'https?://(.+?)/', link)
    if host != None:
        host = host.group(1)
        #puni rjecnik oblika {'host' : broj_referenciranja}
        if host not in hosts.keys():
            hosts[host] = 1
        else:
            hosts[host] += 1

print("Hostovi: ")
for host in hosts:
    print(host + " : " + str(hosts[host]))      

print("Mailovi: ")
for match in re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", stringPage):
    if not match in mails:
        mails.append(match)
        print(match)

print("Broj slika: ")        
print(len(re.findall(r'<img.*?>', stringPage)))