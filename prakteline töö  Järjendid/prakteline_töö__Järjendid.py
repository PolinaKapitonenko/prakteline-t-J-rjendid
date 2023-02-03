
from math import *
from random import *

#рактическая работа "Isikukood"
isikukood=[]
while True:
    isikukood=input("Anna isikukood: ") #str
    if len(isikukood)!=11:
        print("liiga palju või liiga võhe sümboleid. Sisesta veel kord: ")
    else:
        print("isikukoodi kontroll")
        isikukood_list=list(isikukood)
        s1=int(isikukood_list[0]) #"1"->1
        if s1 not in [1,2,3,4,5,6]:
            print("Esimene sümbol ei ole õige!")
        else:
            print("Esimene sümbol on õige ")
            y=isikukood_list[1]+isikukood_list[2] #aasta
            m=int(isikukood_list[3]+isikukood_list[4]) #kuu
            d=int(isikukood_list[5]+isikukood_list[6]) #päev
            if (int(m)<1 or int(m)>13) and (int(d)<1 or int(d)>31):
                print("sünnipäev ei saa luua")
            else:
                if s1==1 or s1==2:
                    yy="18"
                elif s1==3 or s1==4:
                    yy="19"
                else:
                    yy="20"
                späev=d+"."+m+"."+yy+y #ei ple 18.., 19.., 20..,
                print(f"Sünnipäev on {späev}")
                print(f"Viimane number: {isikukood_list[-1]}")
   #komtrollnumber



#Задание 4: Сортировка

spisok=[-46,75,30,-2,1]
spisok.sort()
print(spisok)
spisok.sort(reverse=True)
print(spisok)

#3
arvud=[]
kogus=int(input("Kogus: "))
for i in range(kogus):
    arvud.append(randint(-100,100))
print(arvud)
max_arv=max(arvud)
ind=arvud.index(max_arv)
print(ind)
print(max_arv)
max_arv=round(max_arv/kogus,2)
arvud.insert(ind,max_arv)
arvud.pop(ind+1)
print(arvud)

#1
index=""
maakonnad=["Tallinn, Narva, Kohtla-Järve, Ida-Virumaa, Tartu, Tartumaa, Virumaa, Viljandi, Pärnumaa, Saaremaa"]
while True:
    try:
        index=int(input("kirjutage  index"))
        if index<99999 and index>10000:
            break
    except:
        print("vale index.")
i=index//10000
print(f"{index} on {maakonnad[i-1]}")
if i in [1,2,3]:
    print("Koju jääma!")
else:
    print("Kanna maske!")

#2
maakonnad=["Tallinn", "Narva", "Kohtla-Järve", "Ida-Virumaa", "Tartu", "Tartumaa", "Virumaa", "Pärnumaa"]
osa1=[]
osa2=[]
print(maakonnad)
if len(maakonnad)%2==0 and len(maakonnad)>=2:
    n=int(len(maakonnad)/2)
    for i in range(n):
        osa1.append(maakonnad[i-1])
    for j in range (n+1,len(maakonnad)+1):
        osa2.append(maakonnad[j-1])
    osa1.reverse()    
    osa2.reverse()
    osa2.extend(osa1)
    print(osa2)
else:
    print("Viga!")



