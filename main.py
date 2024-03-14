wiersze=open('galerie_przyklad.txt','r');
# ZADANIE 4.1
# tab=[]
# key=[]
# slownik={}
# for wiersz in wiersze:
#     tab.append(wiersz.strip().split())
#
# for i in range(0, len(tab)):
#     key=tab[i][0]
#
#     if key in slownik:
#         slownik[key]+=1
#     else:
#         slownik[key]=1
#
# print(slownik)

#ZADANIE 4.2
liczba_loklais=[]
liczba_lokali=140
tab=[]
key=[]
slownik={}
for wiersz in wiersze:
    tab.append(wiersz.strip().split())



print(tab)
for i in range(0,len(tab)):
    for liczba in range(2,len(tab[i])):
        if tab[i][liczba]=="0":
            liczba_lokali=liczba_lokali-1
    liczba_loklais.append(int(liczba_lokali/2))
    liczba_lokali=140
powierzchnia=0;
powierzchniaa=[]
for i in range(0,len(tab)):
    for liczba in range(2,len(tab[i])):
        powierzchnia+=int(liczba)
    powierzchniaa.append(powierzchnia)
    powierzchnia=140

print(powierzchniaa)

