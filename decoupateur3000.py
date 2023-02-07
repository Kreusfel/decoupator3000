import os
import csv
import configparser
import time
import gc

config = configparser.ConfigParser()
config.read('setup.ini')
F_FichierSource = config['DEFAULT']['FichierSource']
F_FichierSortie = config['DEFAULT']['FichierSortie']
F_ENTETE = config['DEFAULT']['EnTete']

def defdate(DATE):
    return DATE.replace('/','')  
    
def lecture_csv():
    print('[Bienvenue dans le Découpateur 3000]')
    time.sleep(1)
    print('Fichier à découper : '+ F_FichierSource )
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    
    with open(F_FichierSource, newline='') as f:
        reader = csv.reader(f, delimiter=';')
        print(F_ENTETE)
        if F_ENTETE == 'Oui' : 
            print(next(reader))
        date_jour = ''
        fichier = open("init", "a")

        while True:
            try:
                row = next(reader)
                d = row[0][0:10]
                if d != date_jour:
                    fichier.close()
                    del fichier
                    fname = defdate(d) + F_FichierSortie
                    fichier = open(fname, "a")
                    fichier.write(d+';'+row[0][11:]+';'+row[1]+"\n")
                    date_jour = row[0][0:10]
                    print('Création du fichier du ' + date_jour)
                else:
                    fichier.write(d+';'+row[0][11:]+';'+row[1]+"\n")
            except StopIteration:
                break
        fichier.close()
        os.remove('init')
        
lecture_csv()