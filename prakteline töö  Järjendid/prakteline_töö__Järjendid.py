

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

#Практическая работа "Isikukood"
arvud=[]
isikukood=[]

while True:
    isikukood=input("Anna isikukood: ") #str
    if isikukood=="1": break
    if len(isikukood)!=11:
        print("liiga palju või liiga võhe sümboleid. Sisesta veel kord: ")
        arvud.append(isikukood)
    else:
        print("isikukoodi kontroll")
        isikukood_list=list(isikukood)
        s1=int(isikukood_list[0]) #"1"->1
        if s1 not in [1,2,3,4,5,6]:
            print("Esimene sümbol ei ole õige!")
            arvud.append(isikukood)
        else:
            print("Esimene sümbol on õige ")
            y=isikukood_list[1]+isikukood_list[2] #aasta
            m=int(isikukood_list[3]+isikukood_list[4]) #kuu
            d=int(isikukood_list[5]+isikukood_list[6]) #päev
            if (int(m)<1 or int(m)>13) and (int(d)<1 or int(d)>31):
                print("sünnipäev ei saa luua")
                arvud.append(isikukood)
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
            if s1 in [1,3,5]:
                print("Nees")
            if s1 in [2,4,6]:
                print("naine")
a1=int(isikukood[0])*1
b1=int(isikukood[1])*2
b2=int(isikukood[2])*3
b3=int(isikukood[3])*4
b4=int(isikukood[4])*5
b5=int(isikukood[5])*6
b6=int(isikukood[6])*7
b7=int(isikukood[7])*8
b8=int(isikukood[8])*9
b9=int(isikukood[9])*1


s11=b1+a1+b2+b3+b4+b5+b6+b7+b8+b9
print(s11)
s=s11//11
print(s)
p=s*11
p1=s11-p
if p1==int(isikukood [10]):
    print(p1)
else:
    a1=int(isikukood[0])*1
b1=int(isikukood[1])*2
b2=int(isikukood[2])*3
b3=int(isikukood[3])*4
b4=int(isikukood[4])*5
b5=int(isikukood[5])*6
b6=int(isikukood[6])*7
b7=int(isikukood[7])*8
b8=int(isikukood[8])*9
b9=int(isikukood[9])*1

s11=b1+a1+b2+b3+b4+b5+b6+b7+b8+b9
print(s11)
s=s11//11
print(s)
p=s*11
p1=s11-p 
if p1==int(isikukood[10]):
    print(p1)

hhh=int(isikukood_list[8]+isikukood_list[9]+isikukood_list[10])
if 1<hhh<=10:
    haigla="kuuresaare Haigla"
elif 11<hhh<=19:
    haigla="Tartu Ülikoolio Naistekliinik, Tartumaa, Tartu"
elif 21<hhh<=220:
    haigla="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
elif 221<hhh<=270:
    haigla=" Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
elif 271<hhh<=370:
    haigla="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
elif 371<hhh<=420:
    haigla="Narva Haigla"
elif 421<hhh<=470:
    haigla="Pärnu Haigla"
elif 471<hhh<=490:
    haigla="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
elif 491<hhh<=520:
    haigla="Järvamaa Haigla (Paide)"
elif 521<hhh<=570:
    haigla="Rakvere, Tapa haigla"
elif 571<hhh<=600:
    haigla="Valga Haigla "
elif 601<hhh<=650:
    haigla="Viljandi Haigla"
elif 651<hhh<=700:
    haigla="Lõuna-Eesti Haigla (Võru), Põlva Haigla "
else:
    haigla="---"
if int(isikukood_list[0])%2==0:
    sugu="naine"
else:
    sugu="mees"
print(f"See in {sugu}, sünnipäev {späev}, ta om sündinu {haigla}")
isikukood.append(isikukood)

print(isikukood)
arvud=list(map(int,arvud))
arvud.sort()
print(arvud)










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



