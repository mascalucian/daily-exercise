import re
import sys
import os
#import random
import datetime

ro={
'dificultate_antrenament':'Doresti sa fie un antrenament usor/mediu/greu?: ',
'eroare_dificultate':'Aceasta dificultate nu exista! Programul se va inchide.'
}
en={
'dificultate_antrenament':'Do you want your workout easy/medium/hard?: ',
'eroare_dificultate':'This dificulty does not exist. The program will close.'
}
limba=en

#daca nu exista log, genereaza
def fisiercsv(nume):
    if not os.path.exists(nume+'.csv'):
        with open(nume+'.csv', 'w') as f:
            pass


#genereaza un program random
def genereaza(nume):
    global limba
    dificultate=input(limba['dificultate_antrenament'])
    if dificultate=='usor':
        f,a,g=(10,10,5)
    elif dificultate=='mediu':
        f,a,g=(20,20,10)
    elif dificultate=='greu' or dificultate=='hard' or dificultate=='3':
        f,a,g=(50,50,15)
    else:
        print(limba['eroare_dificultate'])
        return 0
    print('Ai de facut {} flotari, {} abdomene si {} genoflexiuni'.format(f,a,g))
    gata=input('Daca ai terminat scrie gata, daca nu, orice altceva: ')
    if gata=='gata':
        with open(nume+'.csv','a') as file:

            azi=datetime.date.today()
            azi.strftime("%d/%m/%Y")
            file.write(str(azi)+': '+'[ {},{},{} ]'.format(f,a,g)+'\n')
    else:
        main()
    do_more()

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
    do_more()
#continuare program
def do_more():
    alegere=input('Doresti sa faci si altceva?: ')
    if alegere=='da' or alegere=='DA' or alegere=="Da" or alegere=='yes':
        main()
    else:
        return 0


def intro():
    nume=input('Cum te cheama? ')
    fisiercsv(nume)
    return nume


#main
def main():
    global nume
    #nume=input('Cum te cheama? ')
    #fisiercsv(nume)
    alegere=input('Ce vrei sa faci? (antrenament,verifica,nimic): ')
    if alegere=='antrenament' or alegere=='a':
        genereaza(nume)
    elif alegere=='verifica' or alegere=='v':
        data=input('Ce data vrei sa verifici? (aaaa-ll-zz): ')
        verifica(data,nume)
    else:
        return 0

nume=intro()
main()
