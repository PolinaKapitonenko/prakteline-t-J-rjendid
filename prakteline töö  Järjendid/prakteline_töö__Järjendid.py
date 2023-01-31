
from math import *
from random import *


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
        index=int(input("введите индекс"))
        if index<99999 and index>10000:
            break
    except:
        print("неправильный индекс.")
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



