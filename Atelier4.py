 #coding : utf-8 
#############################################################################################################
##################################*Bienvenue au jeu Dunes*###################################################
#############################################################################################################

####################################REPRESENTATION DES DONNEES###############################################
import random
#random.seed()
#initialisation des grilles et autres variables de jeu
grille1 = [['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]

'''grille2 = [['_', '_', '_', '_', '_', '_', 'o', '_', '_', '_'],
           ['_', '_', '_', 'o', '_', '_', '_', '_', '_', 'o'],
           ['_', '_', '_', '_', '_', 'o', 'x', '_', 'o', '_'],
           ['_', 'x', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', 'x'],
           ['_', '_', '_', 'o', '_', 'x', '_', '_', '_', '_'],
           ['_', '_', 'x', '_', '_', '_', '_', 'o', '_', 'o'],
           ['_', '_', '_', '_', 'x', '_', '_', '_', 'x', '_'],
           ['_', '_', '_', 'o', '_', '_', '_', '_', '_', '_'],
           ['x', '_', '_', '_', '_', 'o', '_', '_', '_', 'x']]'''

grille2 = [['_', '_', '_', '_', '_', '_', 'o', '_', '_', '_'],
           ['_', '_', '_', 'o', '_', '_', '_', '_', '_', 'o'],
           ['_', 'x', '_', '_', '_', 'o', 'x', '_', 'o', '_'],
           ['_', 'o', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['o', '_', 'o', 'x', '_', '_', '_', '_', '_', 'x'],
           ['_', 'x', '_', 'o', '_', 'x', '_', '_', '_', '_'],
           ['_', '_', 'x', '_', '_', '_', 'x', 'o', '_', 'o'],
           ['_', '_', '_', '_', 'x', '_', '_', '_', 'x', '_'],
           ['_', '_', '_', 'o', '_', 'o', '_', '_', '_', '_'],
           ['x', '_', '_', '_', '_', 'o', '_', '_', '_', 'x']]

grille3 = [['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', 'o', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', 'x'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', 'o', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', 'o', 'x', '_']]

def reprensentation_jeu(): #cette fonction permet de decrire le jeu ainsi que les joueurs et leurs pions
    print("bienvenue a Dunes,un jeu de société ")
    print("se jouant sur un plateau de 10x10 avec 40 pions au total, 20 pour chaque joueur.")
    print("L'objectif principal du jeu est de s'emparer de tous les pions de l'adversaire.")
    print("le joueur 1 (j1) est le joueur ayant les pions representés par des x")
    print("le joueur 2 (j2) est le joueur ayant les pions representés par des o")
    print("je vous souhaite une agreable partie\n")
    
# REPRESENTATION GRAPHIQUE
def afficher_grille(grille):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J']
    numero = ['_|', 1, '|', 2, '|', 3, '|', 4, '|', 5, '|', 6, '|', 7, '|',8, '|', 9, '|' ,10, '|']
    for i in range(len(numero)):
        print(numero[i], end="")     #afficher la premiere ligne (les numeros)
    print('')
    for ligne in range(len(alphabet)):         #c'est pour afficher les lignes (ligne par ligne)
        print(alphabet[ligne]+"|", end="")        
        for indice in range(len(grille[ligne])):
            print(grille[ligne][indice]+'|', end="")
        print('')
    print("  Joueur 1 : x")                 
    print("  Joueur 2 : ○")
    return "Voici la"
    
def avancement_du_jeu(grille):
    #c'est une fonction qui nous permet de savoir les nombres de pions capturés et restant
    nbpions_x,nbpions_o=20,20
    i,j=0,0  # i et j nous permettent de savoir le nombre des pions x et o presents dans la grille       
    for ligne in range(10):                 
        for colonne in range(10):
            if grille[ligne][colonne]=='o':
                i+=1
            elif grille[ligne][colonne]=='x':
                j+=1
    print("il y'a "+str(i)+" pions o et donc le joueur1 a capturé "+str(nbpions_o - i)+" pions o")
    print("il y'a "+str(j)+" pions x et donc le joueur2 a capturé "+str(nbpions_x - j)+" pions x")
    print('')

def choix_grille():#cette fonction permet a l'utilisateur de choisir la grille parmi les 3 proposées
    numgrille = input(" saisir 1 ou 2 ou 3 selon la grille dans laquelle vous voulez jouer ")
    while not(numgrille=='1' or numgrille=='2' or numgrille=='3'):
        numgrille=input("veuillez ressaisir votre reponse tapez 1 ou 2 ou 3 ")
    if int(numgrille) == 1:
        print(afficher_grille(grille1), "grille 1 que vous avez choisi\n")
        return grille1
    elif int(numgrille) == 2:
        print(afficher_grille(grille2), "grille 2 que vous avez choisi\n")
        return grille2
    else:
        print(afficher_grille(grille3), "grille 3 que vous avez choisi\n")
        return grille3

def choix_joueur_adversaire():
    choixadv=input("vous voulez jouez contre l'ordinateur ou contre un autre joueur ? tapez 1 pour joueur ou 2 pour ordinateur ")
    while not(choixadv=='1' or choixadv=='2'):
      choixadv=input("veuillez ressaisir votre reponse,tapez 1 pour joueur ou 2 pour ordinateur")
    return choixadv
#################################################################################################################    
#####################################*Fonctions de verification*#################################################
#################################################################################################################

#fonction pour savoir si l'utilisateur a saisi une lettre majuscule puis un chiffre
def est_au_bon_format(coordonnes):               
    l = len(coordonnes)
    if 2<=l<=3:     #puisque la grille est 10*10 donc les faut prendre en consideration la colonne 10 
        ligne, colonne = coordonnes[0], coordonnes[1:]  #coordonnes[1:]:permet de prendre un fragment de la chaine
        if len(colonne)==1:
            x, y = ord(ligne), ord(colonne[0])
            return ((65 <= x <= 90) and (48 <= y <= 57))
        elif len(colonne)==2:
            x, y ,z= ord(ligne), ord(colonne[0]), ord(colonne[1])
            return ((65 <= x <= 90) and (48 <= y <= 57) and (48 <= z <= 57))
        else:
            return False
    else:
        return False

#une fonction pour savoir si la lettre majuscule est entr A et J et le chiffre entre 1 et 10
def est_dans_grille(coordonnes):
    #J'ai pris un seul argument (coordonnees) au lieu de deux(ligne,colonne) 
    if est_au_bon_format(coordonnes):
        x, y = ord(coordonnes[0]), int(coordonnes[1:])
        return ((65 <= x <= 74) and (1 <= y <= 10))
    else:
        return (False)
    
def pion_correspond_joueur(grille,joueur,pion_choisi):
    test=False
    if joueur==1:
        if grille[ord(pion_choisi[0])-65][int(pion_choisi[1:])-1]=="x":
            test=True
    elif joueur==2:
        if grille[ord(pion_choisi[0])-65][int(pion_choisi[1:])-1]=="o":
            test=True
    return test

def case_vide(grille, coordonnees):
    return grille[ord(coordonnees[0])-65][int(coordonnees[1:])-1]=="_"

def est_pion_adverse(grille,joueur,pion_ad_lig,pion_ad_col):
    coordonnees=chr(pion_ad_lig+65)+str(pion_ad_col+1)
    if joueur==1:
        return est_dans_grille(coordonnees) and grille[pion_ad_lig][pion_ad_col] =="o"
    else:
        return est_dans_grille(coordonnees) and grille[pion_ad_lig][pion_ad_col] =="x"

def est_au_bord_ligne(pion_lig):
    return pion_lig in {0,9}

def est_au_bord_colonne(pion_col):
    return  pion_col in {0,9}
    
def est_pion_joueur(grille,joueur,pion_lig,pion_col):
    coordonnees=chr(pion_lig+65)+str(pion_col+1)
    if joueur==1:
        return est_dans_grille(coordonnees) and grille[pion_lig][pion_col]=="x"
    else:
        return est_dans_grille(coordonnees) and grille[pion_lig][pion_col]=="o"

def est_liste_vide(liste):
    return liste==[]
################################################################################################################    
#########################################*fonctions de saisie*##################################################
################################################################################################################

def choix_joueur_depart():
    numjoueur=int(input("Veuillez taper 1 pour joueur1 ou 2 pour joueur2 "))
    while not(numjoueur==1 or numjoueur==2):
        numjoueur=int(input("Veuillez retaper 1 pour joueur1 ou 2 pour joueur2 "))
    if numjoueur==1:
        print("Le joueur1 avec le pion x commence")
    else:
        print("Le joueur2 avec le pion o commence")
    return numjoueur
        
# la fonction saisir_coordonnes_pion_départ oblige l'utilisateur de respecter quel joueur (1 ou 2 ) il doit jouer
def saisir_coordonnes_pion_départ(grille,joueur):
    print("Quel pion voulez-vous deplacer?")
    coordonnes_depart = input("veuillez saisir ses coordonnées correspondantes ex:A1 ")
    while not(est_dans_grille(coordonnes_depart) and pion_correspond_joueur(grille,joueur,coordonnes_depart)):
        coordonnes_depart = input("coordonnes invalides, veuillez resaisir ligne puis colonne du pion de départ")
    return coordonnes_depart


def saisir_coordonnees_case_darrivees(grille, pion_depart):
    print("Ou voulez-vous vous deplacer?")
    coordonnes_arrivees = input("veuillez saisir les coordonnées de la case d'arrivée (ligne puis colonne)")
    while not(est_dans_grille(coordonnes_arrivees) and case_vide(grille, coordonnes_arrivees)
              and deplacement_orthogonal(grille,pion_depart,coordonnes_arrivees)):
        coordonnes_arrivees = input("coordonnes invalides, veuillez resaisir ligne puis colonne de la case d'arrivée")
    return coordonnes_arrivees
        

#############################################################################################################
###################################################*ATELIER3*#################################################
#############################################################################################################

def deplacement_orthogonal(grille,pion_depart,case_arrivée):
    #cette fonction permet de verifier si le deplacement coreespond aux regles du jeu ou pas 
    test=True
    pd_l,pd_c=ord(pion_depart[0])-65,int(pion_depart[1:])-1   #pd_l: pion depart ligne , #pd_c: pion depart colonne
    ca_l,ca_c=ord(case_arrivée[0])-65,int(case_arrivée[1:])-1
    if ca_l==pd_l:
        if pd_c== ca_c-1:
            print("deplacement du pion "+pion_depart+" vers la case adjacente de droite")
        elif pd_c-1==ca_c:
            print("deplacement du pion "+pion_depart+" vers la case adjacente de gauche")
        else:
            test=False
            print("case n'est pas adjacente")
    elif pd_c==ca_c:
        if pd_l-1==ca_l:
            print("deplacement du pion "+pion_depart+" vers la case adjacente en haut")
        elif pd_l==ca_l-1:
            print("deplacement du pion "+pion_depart+" vers la case adjacente en bas")
        else:
            test=False
            print("case n'est pas adjacente")
    else:
        test=False
    return test

def appliquer_deplacement(grille,joueur,pion_depart,case_arrivée):
    pd_l=ord(pion_depart[0])-65   #pd_l: pion depart ligne
    pd_c=int(pion_depart[1:])-1   #pd_c: pion depart colonne
    ca_l,ca_c=ord(case_arrivée[0])-65,int(case_arrivée[1:])-1
    grille[pd_l][pd_c],grille[ca_l][ca_c]=grille[ca_l][ca_c],grille[pd_l][pd_c]
    appliquer_capture(grille, case_arrivée, joueur)
    afficher_grille(grille)
    avancement_du_jeu(grille)
    return grille
    
def appliquer_capture(grille, case_arrivée, num_joueur):
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Nord, Est, Sud, Ouest
    
    joueur_pion = "x" if num_joueur == 1 else "o"
    adversaire_pion = "o" if num_joueur == 1 else "x"
    
    for direction_x,direction_y in directions :
        x=ord(case_arrivée[0])-65
        y=int(case_arrivée[1:])-1
        x = x + direction_x
        y = y + direction_y
        case_a_capturer=chr(65+x)+str(y+1)
        #On vérifie bien qu'on soit bien dans la grille  
        if est_dans_grille(case_a_capturer) and est_pion_adverse(grille,num_joueur,x,y):
            if (y==9 and grille[x][y-2] == '_') or (y==0 and grille[x][y+2] =='_'):
                grille[x][y] = "_"
            if (not est_dans_grille(chr(65+x)+str(y+2)) or grille[x][y+1] == joueur_pion ) and (not est_dans_grille(chr(65+x)+str(y-1)) or grille[x][y-1] == joueur_pion ) :
                grille[x][y] = "_" # capture
            if (x==9 and grille[x-2][y] == '_') or (x==0 and grille[x+2][y] =='_'):
                grille[x][y] = "_"
            if (not est_dans_grille(chr(x+66)+str(y+1)) or grille[x+1][y] == joueur_pion ) and (not est_dans_grille(chr(x+64)+str(y+1)) or grille[x-1][y] == joueur_pion) :
                grille[x][y] = "_" # capture


#############################################################################################################
###################################################*ATELIER4*#################################################
#############################################################################################################


def indice_vers_coordonnees(ligne, colonne):
    return chr(ligne + 65) + str(colonne+1)

def liste_deplacement_aleatoire(grille,joueur):
    mv_droite=[]     # liste pour stocker les mouvements possibles
    mv_gauche=[]
    mv_haut=[]
    mv_bas=[]
    for ligne in range(10):
        for colonne in range(10):
            case_depart=indice_vers_coordonnees(ligne,colonne)
            if est_pion_joueur( grille,joueur, ligne,colonne):
                for L, C in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # parcours des directions orthogonales possibles
                    ligne_cible, colonne_cible = ligne + L, colonne + C
                    if est_dans_grille(indice_vers_coordonnees(ligne_cible, colonne_cible)) and case_vide(grille, indice_vers_coordonnees(ligne_cible, colonne_cible)):
                        case_arrivee = indice_vers_coordonnees(ligne_cible, colonne_cible)
                        if L==-1 and C==0:
                            mv_haut.append((case_depart,case_arrivee))# ajout du mouvement à la liste des mouvements possibles
                        elif L==1 and C==0:
                            mv_bas.append((case_depart,case_arrivee))
                        elif L==0 and C==-1:
                            mv_gauche.append((case_depart,case_arrivee))
                        elif L==0 and C==1:
                            mv_droite.append((case_depart,case_arrivee))           
    return mv_droite,mv_gauche,mv_haut,mv_bas


def tour_de_jeu(grille,joueur):
    grille_temp=grille
    pion_depart=saisir_coordonnes_pion_départ(grille,joueur)
    case_arrivée=saisir_coordonnees_case_darrivees(grille, pion_depart)
    grille_temp=appliquer_deplacement(grille,joueur,pion_depart,case_arrivée)

def tour_ia_selon_choix_type_dep(grille,liste,choix_type,joueur):
    mouvement_choisi = random.choice(liste)
    coordonnees_depart,coordonnees_arrivees=mouvement_choisi
    Test=deplacement_orthogonal(grille,coordonnees_depart,coordonnees_arrivees)
    grille=appliquer_deplacement(grille,joueur,coordonnees_depart,coordonnees_arrivees)
    
def tour_de_IA(grille,ia):
    mv_droite,mv_gauche,mv_haut,mv_bas=liste_deplacement_aleatoire(grille,ia)
    
    print("voici les mouvement possible a droite:",mv_droite)
    print("voici les mouvement possible a gauche:",mv_gauche)
    print("voici les mouvement possible a haut:",mv_haut)
    print("voici les mouvement possible a bas:",mv_bas)
   
    choix_type = random.randint(1,4)
    while ((choix_type==1 and est_liste_vide(mv_droite)) or (choix_type==2 and est_liste_vide(mv_gauche)) or
           (choix_type==3 and est_liste_vide(mv_haut)) or (choix_type==4 and est_liste_vide(mv_bas))):
        choix_type = random.randint(1,4)
        
    if choix_type==1:
        tour_ia_selon_choix_type_dep(grille,mv_droite,choix_type,ia)
    elif choix_type==2:
        tour_ia_selon_choix_type_dep(grille,mv_gauche,choix_type,ia)
    elif choix_type==3:
        tour_ia_selon_choix_type_dep(grille,mv_haut,choix_type,ia)
    elif choix_type==4:
        tour_ia_selon_choix_type_dep(grille,mv_bas,choix_type,ia)


def fin_de_partie(grille):
    caractere_o = 'o'
    caractere_x = 'x'
    somme_o = 0
    somme_x = 0
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == caractere_x:
                somme_x += 1
            elif grille[i][j] == caractere_o:
                somme_o +=1
    return (somme_o==0 or somme_x==0)

def joueur_gagant(grille):
    caractere_o = 'o'
    caractere_x = 'x'
    somme_o = 0
    somme_x = 0
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == caractere_x:
                somme_x += 1
            elif grille[i][j] == caractere_o:
                somme_o +=1
    if somme_o==0:
        print("La partie est terminée. Félicitations au joueur 1 qui est gagant")
    elif somme_x==0:
        print("La partie est terminée. Félicitations au joueur 2 qui est gagant")

def joueur_vs_joueur():
    grille=choix_grille()
    numjoueur=choix_joueur_depart()
    tour = 1
    while not fin_de_partie(grille):
        print(f"Tour {tour}:") 
        tour_de_jeu(grille,numjoueur)
        if fin_de_partie(grille):
            break
        if numjoueur==1:
            numjoueur=2
            print("c'est le tour du joueur2")
        else:
            print("c'est le tour du joueur1")
            numjoueur=1
        tour+=1
    if fin_de_partie(grille):
        joueur_gagant(grille)
        
def choix_joueur_courant_ia(): 
    choix = input("Choisissez le joueur qui commence - Joueur 1 (tapez '1') ou Joueur 2 (tapez '2'):")
    while choix not in ['1', '2']:
        print("Choix invalide.")
        choix = input("Veuillez choisir le joueur qui commence - Joueur 1 (tapez '1') ou Joueur 2 (tapez '2') : ")
    joueur_humain=input("Choisissez quel joueur humain(vous) vous voulez- Joueur 1 (tapez '1') ou Joueur 2 (tapez '2') : ")
    while joueur_humain not in ['1', '2']:
        print("Choix invalide.")
        joueur_humain = input("Veuillez choisir le joueur humain(vous) - Joueur 1 (tapez '1') ou Joueur 2 (tapez '2') : ")
    print('')
    return (choix,joueur_humain)

def joueur_vs_ordinateur():
    grille=choix_grille()
    joueur_courant,joueur_humain=choix_joueur_courant_ia() 
    ia='2' if joueur_humain=='1' else '1'
    tour = 1
    while not fin_de_partie(grille):
        print(f"Tour {tour}:")
        if not ia==joueur_courant:
            tour_de_jeu(grille,int(joueur_humain))
            if fin_de_partie(grille):
                print("La partie est terminée. Félicitations au joueur ",joueur_courant,"!")
                break  
        else:
            tour_de_IA(grille,int(joueur_courant))
            if fin_de_partie(grille):
                print("La partie est terminée. Félicitations a l'ia !")
                break
            
        if joueur_courant=='1':
            print("c'est le tour du joueur2")
        else:
            print("c'est le tour du joueur1")
        joueur_courant = '2' if joueur_courant == '1' else '1'
        tour+=1

########################################################################################################
########################################*Fonctions de TEST*#############################################
########################################################################################################

def test_deplacement_orthogonal():
    assert deplacement_orthogonal(grille1,"B1","D1") == False, "case arrivée n'est pas adjacente"
    assert deplacement_orthogonal(grille1,"B1","C1") == True, "case d'arrivée valide on peut appliquer le deplacement"
    print("ok, deplacement_orthogonal validé")
    
def test_case_vide():
    assert case_vide(grille1, "B1") == False, "la case n'est pas vide"
    assert case_vide(grille1, "A1") == True, "la case est bien vide"
    print("ok, case_vide validé")
 
def test_pion_correspond_joueur():
    assert pion_correspond_joueur(grille1,1,'A1') == False, "pion_depart ne correspond pas au joueur 1"
    assert pion_correspond_joueur(grille1,2,'A1') == False, "pion_depart ne correspond pas au joueur 2"
    assert pion_correspond_joueur(grille2,1,'J9') == False, "pion_depart de coordonnees invalides"
    assert pion_correspond_joueur(grille1,1,'D1') == True, "pion_depart correspond au joueur choisi"
    print("ok, pion_correspond_joueur validé")
    
def test_est_pion_adverse():
    assert est_pion_adverse(grille2,1,7,9) == False, "(7,9) correspond a H10 qui est une case vide"
    assert est_pion_adverse(grille2,1,6,9) == True, "(6,9) correspond a G10 qui est un pion adversaire pour le joueur 2"
    print("ok, est_pion_adverse validé ")
    
def test_est_au_bord_ligne():
    assert est_au_bord_ligne(1) == False, "le pion se sitant a la 2eme ligne n'est pas situé au bord"
    assert est_au_bord_ligne(0) == True, "le pion se sitant a la 1eme ligne est situé au bord"
    print("ok, est_au_bord_ligne validé")
    
def test_est_au_bord_colonne():
    assert est_au_bord_colonne(4) == False, "pion_depart ne correspond pas au joueur 1"
    assert est_au_bord_colonne(9) == True, "pion_depart ne correspond pas au joueur 2"
    print("ok, est_au_bord_colonne validé")

grille4 = [['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],  #j'ai rajouté cette grille pour tester la fonction fin_grille 
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', 'o'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', 'o', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', 'o'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]

def test_fin_de_partie():
    assert fin_de_partie(grille1) == False, "la partie n'est pas encore terminée"
    assert fin_de_partie(grille2) == False, "la partie n'est pas encore terminée"
    assert fin_de_partie(grille3) == False, "la partie n'est pas encore terminée"
    assert fin_de_partie(grille4) == True, "la partie est terminée"
    print("ok, fin_de_partie validé")
    
def test_indice_vers_coordonnees():
    assert indice_vers_coordonnees(0, 0) == ('A1'), "Erreur pour les coordonnées A1"
    assert indice_vers_coordonnees(1, 1) ==('B2') , "Erreur pour les coordonnées B2"
    assert indice_vers_coordonnees(0, 3)== ('A4') , "Erreur pour les coordonnées A4"
    assert indice_vers_coordonnees(9, 7) == ('J8'), "Erreur pour les coordonnées J8"
    assert indice_vers_coordonnees(4, 4) == ('E5'), "Erreur pour les coordonnées E5"
    print("ok, indice_vers_coordonnees validé ")

def test_liste_deplacement_aleatoire():
    assert liste_deplacement_aleatoire(grille1,1)==([],[],[('D1', 'C1'), ('D2', 'C2'), ('D3', 'C3'), ('D4', 'C4'), ('D5', 'C5'), ('D6', 'C6'), ('D7', 'C7'), ('D8', 'C8'), ('D9', 'C9'), ('D10', 'C10'), ('I1', 'H1'), ('I2', 'H2'), ('I3', 'H3'), ('I4', 'H4'), ('I5', 'H5'), ('I6', 'H6'), ('I7', 'H7')
                                                          , ('I8', 'H8'), ('I9', 'H9'), ('I10', 'H10')],
[('D1', 'E1'), ('D2', 'E2'), ('D3', 'E3'), ('D4', 'E4'), ('D5', 'E5'), ('D6', 'E6'), ('D7', 'E7'), ('D8', 'E8'), ('D9', 'E9'), ('D10', 'E10'), ('I1', 'J1'), ('I2', 'J2'), ('I3', 'J3'), ('I4', 'J4'), ('I5', 'J5'), ('I6', 'J6'), ('I7', 'J7'), ('I8', 'J8'), ('I9', 'J9'), ('I10', 'J10')]
)
    assert liste_deplacement_aleatoire(grille1,2)== ([],[],[('B1', 'A1'), ('B2', 'A2'), ('B3', 'A3'), ('B4', 'A4'), ('B5', 'A5'), ('B6', 'A6'), ('B7', 'A7'), ('B8', 'A8'), ('B9', 'A9'), ('B10', 'A10'), ('G1', 'F1'), ('G2', 'F2'), ('G3', 'F3'), ('G4', 'F4'), ('G5', 'F5'), ('G6', 'F6'), ('G7', 'F7'), ('G8', 'F8'), ('G9', 'F9'), ('G10', 'F10')]
,[('B1', 'C1'), ('B2', 'C2'), ('B3', 'C3'), ('B4', 'C4'), ('B5', 'C5'), ('B6', 'C6'), ('B7', 'C7'), ('B8', 'C8'), ('B9', 'C9'), ('B10', 'C10'), ('G1', 'H1'), ('G2', 'H2'), ('G3', 'H3'), ('G4', 'H4'), ('G5', 'H5'), ('G6', 'H6'), ('G7', 'H7'), ('G8', 'H8'), ('G9', 'H9'), ('G10', 'H10')])
    assert liste_deplacement_aleatoire(grille2,1)==([('C2', 'C3'), ('C7', 'C8'), ('E4', 'E5'), ('F2', 'F3'), ('F6', 'F7'), ('G3', 'G4'), ('H5', 'H6'), ('H9', 'H10'), ('J1', 'J2')],[('C2', 'C1'), ('E10', 'E9'), ('F2', 'F1'), ('F6', 'F5'), ('G3', 'G2'), ('G7', 'G6'), ('H5', 'H4'), ('H9', 'H8'), ('J10', 'J9')],
    [('C2', 'B2'), ('C7', 'B7'), ('E4', 'D4'), ('E10', 'D10'), ('F2', 'E2'), ('F6', 'E6'), ('G3', 'F3'), ('G7', 'F7'), ('H5', 'G5'), ('H9', 'G9'), ('J1', 'I1'), ('J10', 'I10')],[('C7', 'D7'), ('E10', 'F10'), ('F2', 'G2'), ('F6', 'G6'), ('G3', 'H3'), ('G7', 'H7'), ('H5', 'I5'), ('H9', 'I9')])
    assert liste_deplacement_aleatoire(grille3,1)==([('J9', 'J10')],[('G10', 'G9')],[('G10', 'F10'), ('J9', 'I9')],[('G10', 'H10')])
    assert liste_deplacement_aleatoire(grille3,2)==([('D7', 'D8'), ('I8', 'I9')],[('D7', 'D6'), ('I8', 'I7'), ('J8', 'J7')],[('D7', 'C7'), ('I8', 'H8')],[('D7', 'E7')])
    print("ok, liste_deplacement_aleatoire validé ")

#########################################################################################################
#######################################***CODE PRINCIPAL***##############################################
#########################################################################################################

reprensentation_jeu()
# execution affichage sur les 3 grilles et autres variables de jeux
print(afficher_grille(grille1), "grille de début de partie\n")
avancement_du_jeu(grille1)

print(afficher_grille(grille2), "grille en milieu de partie\n")
avancement_du_jeu(grille2)

print(afficher_grille(grille3), "grille de fin de partie\n")
avancement_du_jeu(grille3)

##fonctions de verification
#jeux de tests
def test_generale():
    test_case_vide()
    test_deplacement_orthogonal()
    test_fin_de_partie()
    test_pion_correspond_joueur()
    test_est_pion_adverse()
    test_est_au_bord_ligne()
    test_est_au_bord_colonne()
    test_indice_vers_coordonnees()
    test_liste_deplacement_aleatoire()
    

#affichage des coordonnees saisies
#test_generale()   #decommenter ca pour voir le fonctionnenment des fonctions de tests
print("Et la partie commence...")
'''numjoueur=choix_joueur_depart()
grille=choix_grille()
tour_de_jeu(grille,numjoueur)'''

def main():
    test_generale()    #C'est l'appel a la fonction generale de tests pour tester chaque fonction du code 
    choixadv=choix_joueur_adversaire()
    if choixadv=='1' :
        joueur_vs_joueur()
    else:
        joueur_vs_ordinateur()
    
            
            
if __name__ == "__main__":
    main()
 