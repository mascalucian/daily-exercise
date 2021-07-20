import re
import sys
import os
import random
import datetime

#daca nu exista log, genereaza
def fisiercsv(nume):
    if not os.path.exists(nume+'.csv'):
        with open(nume+'.csv', 'w') as f:
            pass


#genereaza un program random
def genereaza(nume):
    dificultate=input('Doresti sa fie un antrenament usor/mediu/greu?: ')
    if dificultate=='usor':
        f,a,g=(10,10,5)
    elif dificultate=='mediu':
        f,a,g=(20,20,10)
    else:
        f,a,g=(50,50,15)
    print('Ai de facut {} flotari, {} abdomene si {} genoflexiuni'.format(f,a,g))
    gata=input('Daca ai terminat scrie gata, daca nu, orice altceva: ')
    if gata=='gata':
        with open(nume+'.csv','a') as file:

            azi=datetime.date.today()
            azi.strftime("%d/%m/%Y")
            file.write(str(azi)+': '+'[ {},{},{} ]'.format(f,a,g)+'\n')
    else:
        main()

#verifica ce s-a facut in ziua respectiva
def verifica(data,nume):
    cate=[]
    gasit=0
    with open(nume+'.csv') as file:
        for linie in file:
            text=linie.strip()
            cautare=re.search(data,text)
            if data in linie:
                pattern=r'(\d+)\,(\d+)\,(\d+)'
                result=re.search(pattern,text)
                gasit=1

                cate.append(result[1])
                cate.append(result[2])
                cate.append(result[3])


        if gasit==1:
            print('Pe data de {}, {} a facut {} flotari, {} abdomene si {} genoflexiuni'.format(data,nume,cate[0],cate[1],cate[2]))
        else:
            print('In ziua {}, {} nu a facut niciun exercitiu.'.format(data,nume))


#main
def main():
    nume=input('Cum te cheama? ')
    fisiercsv(nume)
    alegere=input('Ce vrei sa faci? (antrenament,verifica,nimic): ')
    if alegere=='antrenament' or alegere=='a':
        genereaza(nume)
    elif alegere=='verifica' or alegere=='v':
        data=input('Ce data vrei sa verifici? (aaaa-ll-zz): ')
        verifica(data,nume)
    else:
        return 0

main()
