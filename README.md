# decoupator3000

Script de découpage de CSV. 

L'entrée est de la forme : 
Date; Donnée
13/08/2022 23:59:35; 0,43402779

En sortie vous aurez un fichier par jour sous la forme
Date; Heure; Donnée
13/08/2022; 23:59:35; 0,43402779

En fonction du fichier setup.ini il peut ou non y avoir une en-tête au fichie d'entrée. 
