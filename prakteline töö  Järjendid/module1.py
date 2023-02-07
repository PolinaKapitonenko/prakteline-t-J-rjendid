def sugu(isikukood_list)->str:
    """ esimise tahe järgi määrne sugu
    :param list isikukood_list: Järjend isikukoodinumbrides
    :trupe
    """
    if int(isikukood_list[0])%2==0:
        sugu="naine"
    else:
        sugu="mees"
    return sugu


def sünnikoht(a:int)->str:
    """определяет дату рождения 
    """
    
    if 1<a<=10:
        haigla="kuuresaare Haigla"
    elif 11<a<=19:
        haigla="Tartu Ülikoolio Naistekliinik, Tartumaa, Tartu"
    elif 21<a<=220:
        haigla="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif 221<a<=270:
        haigla=" Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271<a<=370:
        haigla="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif 371<a<=420:
        haigla="Narva Haigla"
    elif 421<a<=470:
        haigla="Pärnu Haigla"
    elif 471<a<=490:
        haigla="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif 491<a<=520:
        haigla="Järvamaa Haigla (Paide)"
    elif 521<a<=570:
        haigla="Rakvere, Tapa haigla"
    elif 571<a<=600:
        haigla="Valga Haigla "
    elif 601<a<=650:
        haigla="Viljandi Haigla"
    elif 651<a<=700:
        haigla="Lõuna-Eesti Haigla (Võru), Põlva Haigla "
    else:
        haigla="---"
    return haigla

def späev(d:int,m: int,y: int)->str:
    """
    """
    s1=int(isikukood_list[0])
    y=isikukood_list[1]+isikukood_list[2] #aasta
    m=int(isikukood_list[3]+isikukood_list[4]) #kuu
    d=int(isikukood_list[5]+isikukood_list[6]) #päev
    if (int(m)<1 or int(m)>13) and (int(d)<1 or int(d)>31):
            späev="viga"
            #arvud.append(isikukood)
    else:
                if s1==1 or s1==2:
                    yy="18"
                elif s1==3 or s1==4:
                    yy="19"
                else:
                    yy="20"
                späev=d+"."+m+"."+yy+y #ei ple 18.., 19.., 20..,
                return späev
            
def naised_mehed(ikoodid:list):
    """
    :rtype list
    """
    naised=[]
    mehed=[]
    for kood in ikoodid:
        isikukood_list=list(kood)
        sugu=sugu(isikukood_list)
        if sugu=="naine":
            naised.appemd(kood)
        else:
            mehed.append(kood)
    ikoodid.clear()
    ikoodid.extend(naised)
    ikoodid.extend(naised)
    ikoodid.exted(mehed)