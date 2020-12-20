# -------------------------- Import ------------------------------ #
import os
import time
from upemtk import *
from random import *
from ast import *

# ------------------------- Fonctions ---------------------------- #

# ----------- Menu du jeu ------------ #

def affichageMenu():
	"""
	Créée le menu avec du texte et des rectangles servant de "boutons"
	"""
	global choix, xy1_Jouer, xy1_Load, xy2_Load, xy2_Jouer, xy1_affichageRegles, xy2_affichageRegles, xy1_Close, xy2_Close
	## Titre du jeu ##
	efface_tout()
	image(largeur*nbCasesX/2+100, 10, 'titreJeu.gif', ancrage="n")

	texte(largeur*nbCasesX/2+100, largeur*4, "Choisissez une action", couleur="black", taille=30, ancrage="n")
	## Cadre ##
	rectangle(largeur*2, largeur*3.5, (nbCasesX*largeur+200)-(largeur*2), (nbCasesY*largeur+75)-(largeur*3), epaisseur = 3, couleur = 'red')
	## Bouton jouer ##
	rectangle(largeur*4, largeur*7, (nbCasesX*largeur)/2, largeur*9, remplissage="green", tag = 'startButton')
	texte(largeur *6.5, largeur*7.5, "Jouer", couleur="white", taille=25, ancrage="n", tag = 'start')
	xy1_Jouer = largeur*4, largeur*7
	xy2_Jouer = (nbCasesX*largeur)/2, largeur*9
	## Bouton continuer ##
	rectangle(largeur*13, largeur*7, largeur*nbCasesX, largeur*9, remplissage="orange", tag = 'loadButton')
	texte(largeur*15.5, largeur*7.5, "Continuer", couleur="white", ancrage="n", tag = 'load')
	xy1_Load = largeur*13, largeur*7
	xy2_Load = largeur*nbCasesX, largeur*9
	## Bouton quitter ##
	rectangle(largeur*4, largeur*11, (nbCasesX*largeur)/2, largeur*13, remplissage="darkred", tag = 'closeButton')
	texte(largeur*6.5, largeur*11.5, "Quitter", couleur="white", ancrage="n", tag = 'close')
	xy1_Close = largeur*4, largeur*11
	xy2_Close = (nbCasesX*largeur)/2, largeur*13
	## Bouton règles ##
	rectangle(largeur*13, largeur*11, largeur*nbCasesX, largeur*13, remplissage="darkblue", tag = 'affichageReglesButton')
	texte(largeur*15.5, largeur*11.5, "Règles", couleur="white", ancrage="n", tag = 'affichageRegles')
	xy1_affichageRegles = largeur*13, largeur*11
	xy2_affichageRegles = largeur*nbCasesX, largeur*13

	## On regarde sur quel bouton le joueur à appuyer ##
	choix = choixMenu()
	if choix == 'Règles':
		affichageRegles()
	if choix == 'Continuer':
		continuer()
	if choix == 'Jouer':
		affichageJoueurs()

def affichageJoueurs():
	"""
	Affiche 2 boutons permettant au joueur de choisir si il veut jouer à 1 ou 2 joueurs.
	"""
	global nbrJoueurs, xy1_1j, xy2_1j, xy1_2j, xy2_2j, xy1_3j, xy2_3j
	## Titre du jeu ##
	efface_tout()
	image(largeur*nbCasesX/2+100, 10, 'titreJeu.gif', ancrage="n")

	texte(largeur*nbCasesX/2+100, largeur*4, "Choisissez une action", couleur="black", taille=30, ancrage="n")
	## Cadre ##
	rectangle(largeur*2, largeur*3.5, (nbCasesX*largeur+200)-(largeur*2), (nbCasesY*largeur+75)-(largeur*3), epaisseur = 3, couleur = 'red', tag = 'cadreMenu')
	## Bouton 1 joueur ##
	rectangle(largeur*4, largeur*7, (nbCasesX*largeur)/2, largeur*9, remplissage="darkred", tag = 'bouton1J')
	texte(largeur *6.5, largeur*7.5, "1 joueur", couleur="white", taille=25, ancrage="n", tag = 'texte1J')
	xy1_1j = largeur*4, largeur*7
	xy2_1j = (nbCasesX*largeur)/2, largeur*9
	## Bouton 2 joueurs ##
	rectangle(largeur*13, largeur*7, largeur*nbCasesX, largeur*9, remplissage="darkblue", tag = 'bouton2J')
	texte(largeur*15.5, largeur*7.5, "2 joueurs", couleur="white", ancrage="n", tag = 'texte2J')
	xy1_2j = largeur*13, largeur*7
	xy2_2j = largeur*nbCasesX, largeur*9
	## Bouton 3 joueurs ##
	rectangle(largeur*8.5, largeur*11, (nbCasesX*largeur)/2 +largeur*4.5, largeur*13, remplissage="orange", tag = 'bouton3J')
	texte(largeur*11, largeur*11.5, "3 joueurs", couleur="white", ancrage="n", tag = 'texte3J')
	xy1_3j = largeur*8.5, largeur*11
	xy2_3j = (nbCasesX*largeur)/2+largeur*4.5, largeur*13

	nbrJoueurs = choixJoueur()
	efface('cadreMenu')
	if nbrJoueurs == '1 joueur':
		return '1j'
	if nbrJoueurs == '2 joueurs':
		return '2j'
	if nbrJoueurs == '3 joueurs':
		return '3j'

def affichageRegles():
	"""
	Affiche les règles du jeu
	"""
	efface_tout()
	## Texte règles ##
	texte(5, 25, "Règles du jeu:", couleur="red", ancrage="w")
	texte(5, 95, "Le jeu se compose de 4 personnages, de 4 objets et d'une porte de sortie. ",couleur='black', ancrage='w', taille=12 )
	texte(5, 130, "Vous pouvez controler les 4 personnages mais uniquement un à la fois. Chaque personnage possède son propre objet.", couleur='black', ancrage='w', taille=12)
	texte(5, 200, "Le but est de récupérer tous les objets puis de sortir.", couleur='black', ancrage='w', taille=12)
	texte(5, 235, "Au départ, la porte de sortie est vérouillée. Pour permettre son ouverture, chaque personnage doit se trouver sur la case de l'objet lui correspondant,", couleur='black', ancrage='w', taille=12)
	texte(5, 270, "cela revient à récupérer tous les objets Le mage possède la fiole, l'elfe possède l'arc, le nain possède la hache et le barbare possède l'épée.", couleur='black', ancrage='w', taille=12)
	texte(5, 335,"ATTENTION, vous disposez d'un temps limité de 3mn. Si vous le dépassez c'est GAME OVER.", couleur='red', ancrage='w',taille=15)
	texte(5, 390,"Si vous êtes proche de la fin du temps imparti, n'hésitez pas à récupérer des sabliers ! Ils permettent d'inverser le temps.", couleur='black', ancrage='w', taille=12)
	texte(5, 425,"Mais attention à ne pas les récupérer si il vous reste beaucoup de temps, ou vous vous retrouverez à devoir courrir!", couleur='black', ancrage='w', taille=12)
	texte(85, 495,"MAINTENANT QUE VOUS SAVEZ TOUT, BONNE CHANCE JEUNES VOLEURS !!", couleur='dark blue', ancrage='w',taille=18)

	## Bouton retour ##
	rectangle(largeur*nbCasesX, largeur/2, largeur*nbCasesX +largeur*3, largeur*1.5, remplissage = 'black')
	texte(largeur*nbCasesX +25, largeur, 'Retour', couleur = 'white', ancrage = 'w')
	coordClic = attente_clic()
	if coordClic[0] > largeur*nbCasesX and coordClic[0] < largeur*nbCasesX +largeur*3:
		if coordClic[1] > largeur/2 and coordClic[1] < largeur*1.5:
			affichageMenu()
		else: affichageRegles()
			
	else: affichageRegles()

def choixMenu():
	"""
	Compare les coordonnées du clic aux coordonnées des rectangles du menus.
	On effectue une action différente en fonction du bouton cliqué par le joueur.
	"""
	coordClic = attente_clic()
	## Actionner bouton jouer ##
	if coordClic[0] > xy1_Jouer[0] and coordClic[0] < xy2_Jouer[0]:
		if coordClic[1] > xy1_Jouer[1] and coordClic[1] < xy2_Jouer[1]:
			return 'Jouer'
	## Actionner bouton continuer ##
	if coordClic[0] > xy1_Load[0] and coordClic[0] < xy2_Load[0]:
		if coordClic[1] > xy1_Load[1] and coordClic[1] < xy2_Load[1]:
			return 'Continuer'
	## Actionner bouton quitter ##
	if coordClic[0] > xy1_Close[0] and coordClic[0] < xy2_Close[0]:
		if coordClic[1] > xy1_Close[1] and coordClic[1] < xy2_Close[1]:
			return 'Quitter'
	## Actionner bouton règles ##
	if coordClic[0] > xy1_affichageRegles[0] and coordClic[0] < xy2_affichageRegles[0]:
		if coordClic[1] > xy1_affichageRegles[1] and coordClic[1] < xy2_affichageRegles[1]:
			return 'Règles'
		else:					# Si on clique ailleur dans la fenêtre, on reste sur le menu.
			affichageMenu()
	else:
		affichageMenu()

def choixJoueur():
	"""
	Compare les coordonnées du clic aux coordonnées des rectangles du menus.
	On lance le jeu avec le mode de joueur séléctionné.
	"""
	coordClic = attente_clic()
	## Actionner bouton 1 joueur ##
	if coordClic[0] > xy1_1j[0] and coordClic[0] < xy2_1j[0]:
		if coordClic[1] > xy1_1j[1] and coordClic[1] < xy2_1j[1]:
			return '1 joueur'
	## Actionner bouton 2 joueurs ##
	if coordClic[0] > xy1_2j[0] and coordClic[0] < xy2_2j[0]:
		if coordClic[1] > xy1_2j[1] and coordClic[1] < xy2_2j[1]:
			return '2 joueurs'
	## Actionner bouton 3 joueurs ##
	if coordClic[0] > xy1_3j[0] and coordClic[0] < xy2_3j[0]:
		if coordClic[1] > xy1_3j[1] and coordClic[1] < xy2_3j[1]:
			return '3 joueurs'
		else:					# Si on clique ailleur dans la fenêtre, on reste sur la page actuelle.
			choixJoueur()
	else:
		choixJoueur()


# ---------- Partie Logique ---------- #

# --- Création entités --- #

def creationMap(l, L) :
	"""
	Créer une fenêtre avec un nombre de cases en X et Y donné.
	Créer une matrice remplie de 0
	"""
	global nbCasesX, nbCasesY, largeur, Plateau 
	largeur, nbCasesX, nbCasesY, Plateau = 50, l, L, list()
	for yAxes in range(nbCasesY):
		Plateau.append([])				# Dans chaque ligne du plateau
		for xAxes in range(nbCasesX):
			Plateau[yAxes].append(0)	# On met un 0, qui représente une case vide
	cree_fenetre((nbCasesX*largeur+350), (nbCasesY*largeur + 75))	# Création de la fenêtre

# --- Actions --- #

def actions1J():
	global actionsJ1, actionsJ2, actionsJ3
	actionsJ1 = ['Left','Right','Up','Down','Vortex','Escalators', 'Exploration']
	actionsJ2, actionsJ3 = list('*'), list('*')

def actions2J():
	global actionsJ1, actionsJ2, actionsJ3
	actionsJ1, actionsJ2, actionsJ3 = list(), list(), list('*')

	directionAppliquee = 0
	while directionAppliquee != 2:
		rdmDirection = directions[randint(0,len(directions)-1)]
		if rdmDirection not in actionsJ2 :
			actionsJ2.append(rdmDirection)
			directionAppliquee += 1
	actionsJ2.append(special[randint(0,len(special)-1)])

	full = directions + special
	actionsJ1 = [i for i in full + actionsJ2 if i not in full or i not in actionsJ2]

def actions3J():
	global actionsJ1, actionsJ2, actionsJ3
	actionsJ1, actionsJ2, actionsJ3 = list(), list(), list()
	# Ajout des actions au J2
	actionsJ2.append(directions[randint(0,len(directions)-1)])
	actionsJ2.append(special[randint(0,len(special)-1)])
	# Ajout des actions au J3
	ajouter_dirJ3, ajouter_actJ3, ajouter_dirJ1, ajouter_actJ1 = 0,0,0,0
	while len(actionsJ1) != 3:
		rdmDirection = directions[randint(0,len(directions)-1)]
		rdmAction = special[randint(0,len(special)-1)]
		# Joueur 3
		if rdmDirection not in actionsJ2 and ajouter_dirJ3 < 1:
			actionsJ3.insert(0,rdmDirection)
			ajouter_dirJ3 += 1
		if rdmAction not in actionsJ2 and ajouter_actJ3 < 1:
			actionsJ3.append(rdmAction)
			ajouter_actJ3 += 1
		# Joueur 1
		if rdmDirection not in actionsJ1 and rdmDirection not in actionsJ2 and rdmDirection not in actionsJ3 and ajouter_dirJ1 < 2:
			actionsJ1.insert(0,rdmDirection)
			ajouter_dirJ1 += 1
		if rdmAction not in actionsJ2 and rdmAction not in actionsJ3 and rdmAction not in actionsJ1 and ajouter_actJ1 < 1:
			actionsJ1.append(rdmAction)
			ajouter_actJ1 += 1

def actionAimedJ1(actionChoisieJ1):
	"""
	Fonctionne avec la fonction actionSelectedJ1(i), qui permet de choisir l'action à effectuer pour le J1.
	Elle renvoie l'action séléctionnée.
	"""
	actionViséeJ1 = actionChoisieJ1+1
	if actionViséeJ1 > len(actionsJ1): actionViséeJ1 = 1
	return actionViséeJ1

def actionAimedJ2(actionChoisieJ2):
	"""
	Fonctionne avec la fonction actionSelectedJ2(i), qui permet de choisir l'action à effectuer pour le J2.
	Elle renvoie l'action séléctionnée.
	"""
	actionViséeJ2 = actionChoisieJ2+1
	if actionViséeJ2 > len(actionsJ2): actionViséeJ2 = 1
	return actionViséeJ2 

def actionAimedJ3(actionChoisieJ3):
	"""
	Fonctionne avec la fonction actionSelectedJ3(i), qui permet de choisir l'action à effectuer pour le J3.
	Elle renvoie l'action séléctionnée.
	"""
	actionViséeJ3 = actionChoisieJ3+1
	if actionViséeJ3 > len(actionsJ3): actionViséeJ3 = 1
	return actionViséeJ3

def pionAimed(pionChoisi):
	"""
	Fonctionne avec la fonction pionSelected(i), qui permet de choisir le pion à séléctionner.
	Elle renvoie le pion séléctionnée.
	"""
	pionVisé = pionChoisi+1
	if pionVisé > 4: pionVisé = 1
	return pionVisé

def vortexAimed(vortexChoisi):
	"""
	Choix du vortex sur lequel se téléporter.
	"""
	vortexVisé = vortexChoisi+1

	if vortexVisé > len(posVortex_Dwa): vortexVisé = 1


	return vortexVisé

def isSortieOn(etatSortie):
	"""
	Active la sortie si tous les joueurs sont sur leur case objet.
	"""	
	global pionsSurObj
	if etatSortie == False :
		pionsSurObj = 0
		for yAxes in range(nbCasesY):
			for xAxes in range(nbCasesX):
				# +1 si un pion est sur sa case objet.
				for i in range(4):
					if Plateau[yAxes][xAxes] == i+1:
						if yAxes == posObjets[i][0] and xAxes == posObjets[i][1]: pionsSurObj += 1
		# Si tous les pions sont sur leur case objet : sortie active
		if pionsSurObj == 4:
			for yAxes in range(nbCasesY):
				for xAxes in range(nbCasesX):
					if Plateau[yAxes][xAxes] == 5:
						Plateau[yAxes][xAxes] = 6
						return True
		return False
	return True

def isWin(pionsSortis, min, sec):
	"""
	Si les 4 joueurs ont atteints la sortie, la partie s'arrête et on à gagner.
	"""
	if pionsSortis == 4:
		gagner(minutes, secondes)

def sauvegarder():
	to_save = [Plateau,actionsJ1,actionsJ2,actionsJ3,nbrJoueurs,pionsInSortie,pionsSurObj]
	with open('save.txt', 'w') as fic_save:
		for elem in to_save: fic_save.write(str(elem)+'$')

def continuer():
	global Plateau, actionsJ1, actionsJ2, actionsJ3, nbrJoueurs, pionsInSortie,pionsSurObj, sortieOn
	efface_tout()
	with open('save.txt', 'r') as fic_save:
		var = str()
		for ligne in fic_save : var += ligne
		var = var.split('$')
	Plateau,actionsJ1,actionsJ2,actionsJ3,nbrJoueurs = literal_eval(var[0]),literal_eval(var[1]),literal_eval(var[2]),literal_eval(var[3]),var[4]
	pionsInSortie, pionsSurObj = int(var[5]), int(var[6])
	if pionsSurObj+pionsInSortie == 4: sortieOn = True

def actionTouche(pion, actionJ1, actionJ2, actionJ3, objets, pionsSortis, debug):
	"""
	Gère les déplacements à faire selon chaque touche directionnelle appuyée.
	Selon la case sur laquelle veut aller un pion, l'action sera différente.
	"""
	global touche, pionVisé, actionViséeJ1, actionViséeJ2, actionViséeJ3, pionsInSortie, reverseTimer, a, secElapsed
	touche = attente_touche_jusqua(1000)
	choixAction = ['Left', 'Right', 'Up', 'Down','Vortex','Escalators','Exploration']
	choixPion = [1, 2, 3, 4]
	deplacement, dejaVu = None, False
	# F1 : Ferme la fenêtre
	if touche == 'F1': ferme_fenetre()
	# F2 : Mode debug on/off
	if touche == 'F2': debug = not debug
	# F3 : Sauvegarder
	if touche == 'F3' : sauvegarder()
	#  e : change de pion à déplacer
	if touche == 'e' : pionVisé = pionAimed(pionVisé)
	# Change l'action séléctionnée pour le Joueur X
	if touche == '1' : actionViséeJ1 = actionAimedJ1(actionViséeJ1)
	if touche == '2' : actionViséeJ2 = actionAimedJ2(actionViséeJ2)
	if touche == '3' : actionViséeJ3 = actionAimedJ3(actionViséeJ3)
	# Déplace le pion avec l'action séléctionnée pour le Joueur X
	if touche == '4' : deplacement = actionsJ1[actionJ1-1]
	if touche == '5' : deplacement = actionsJ2[actionJ2-1]
	if touche == '6' : deplacement = actionsJ3[actionJ3-1]
	# Déplacements et actions aléatoire si le mode debug est ON
	if debug == True : deplacement, pion, touche = choixAction[randint(0,6)], choixPion[randint(0,3)], 'F2'

	# Action pour chaque déplacement
	if deplacement != None or touche != None:
		for yAxes in range(nbCasesY):
			for xAxes in range(nbCasesX):
				if Plateau[yAxes][xAxes] == pion  and dejaVu == False:
					disponnible = False

					if deplacement == 'Left' :
						if not (yAxes,xAxes-1) in posMurV :				# Si case visée != mur vertical
							decalageY, decalageX, autorisationMurH, autorisationMurV = 0, -1, True, False
							if xAxes > 0: disponnible = True							
					if deplacement == 'Right' : 
						if not (yAxes,xAxes) in posMurV :				# Si case visée != mur vertical
							decalageY, decalageX, autorisationMurH, autorisationMurV = 0, 1, True, True
							if xAxes < nbCasesX-1: disponnible = True
					if deplacement == 'Up' :
						if not (yAxes,xAxes) in posMurH :				# Si case visée != mur horizontal
							decalageY, decalageX, autorisationMurV = -1, 0, True
							if yAxes > 0: disponnible = True
					if deplacement == 'Down' :
						if not (yAxes+1,xAxes) in posMurH :				# Si case visée != mur horizontal
							decalageY, decalageX, autorisationMurV = 1, 0, True
							if yAxes < nbCasesY-1: disponnible = True

					if deplacement == 'Vortex' :
						vortexAimed(0)
						dico_VorPion = {1 : posVortex_War, 2:posVortex_Wiz, 3:posVortex_Elf, 4:posVortex_Dwa}
						for i in range(4):
							if pion == i+1: Plateau[yAxes][xAxes],Plateau[(dico_VorPion.get(i+1)[0][0])][dico_VorPion.get(i+1)[0][1]] = 0,pion

					if deplacement == 'Escalators' :
						if Plateau[yAxes][xAxes] == pion and (yAxes,xAxes) in posEscalator:
							for i in range(len(posEscalator)):
								if i%2 == 0: esca = +1
								if i%2 != 0: esca = -1
								if (yAxes,xAxes) == (posEscalator[i][0],posEscalator[i][1]):
									Plateau[yAxes][xAxes],Plateau[posEscalator[i+esca][0]][posEscalator[i+esca][1]] = 0,pion
						dejaVu = True

					if disponnible == True:
						dejaVu = True
						if Plateau[yAxes+decalageY][xAxes+decalageX] == 0 :				# Si case visée = vide
							Plateau[yAxes+decalageY][xAxes+decalageX], Plateau[yAxes][xAxes] = pion, 0
							break
						if Plateau[yAxes+decalageY][xAxes+decalageX] == pion+10 :		# Si case visée = son objet
							Plateau[yAxes+decalageY][xAxes+decalageX],Plateau[yAxes][xAxes] = pion, 0
							break
						if Plateau[yAxes+decalageY][xAxes+decalageX] == 6 :				# Si case visée = sortie active
							Plateau[yAxes][xAxes] = 0
							pionsInSortie += 1
							break
						if Plateau[yAxes+decalageY][xAxes+decalageX] == 8 :				# Si case visée = sablier
								Plateau[yAxes+decalageY][xAxes+decalageX], Plateau[yAxes][xAxes] = pion, 0
								reverseTimer = not reverseTimer
								a = secElapsed
								secElapsed = 0
								break
	return debug

# ---------- Partie visuelle ---------- #

def affichage() :
	"""
		Actualise l'affichage en fonction de chaque élément dans la matrice.
	"""
	x, y = 0, 0
	if touche != None:
		for yAxes in range(nbCasesY):
			locY = yAxes*largeur-largeur/2+largeur
			for xAxes in range(nbCasesX):
				locX = xAxes*largeur-largeur/2+largeur
				## Affiche un carré gris sur chaque case ##
				rectangle(x, y, x+largeur, y+largeur, remplissage = 'light grey')
				if not sortieOn:
					if yAxes == posVortex_War[0][0] and xAxes == posVortex_War[0][1]: rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'red', tag = 'caseVide')
					if yAxes == posVortex_Wiz[0][0] and xAxes == posVortex_Wiz[0][1]: rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'blue', tag = 'caseVide')
					if yAxes == posVortex_Elf[0][0] and xAxes == posVortex_Elf[0][1]: rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'green', tag = 'caseVide')
					if yAxes == posVortex_Dwa[0][0] and xAxes == posVortex_Dwa[0][1]: rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'yellow', tag = 'caseVide')
					if yAxes == posVortex_Dwa[1][0] and xAxes == posVortex_Dwa[1][1]: rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'yellow', tag = 'caseVide')
					if yAxes == posEscalator[0][0] and xAxes == posEscalator[0][1]: rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'purple', tag = 'caseVide')
					if yAxes == posEscalator[1][0] and xAxes == posEscalator[1][1]: rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'purple', tag = 'caseVide')
					if yAxes == posEscalator[2][0] and xAxes == posEscalator[2][1]: rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'cyan', tag = 'caseVide')
					if yAxes == posEscalator[3][0] and xAxes == posEscalator[3][1]: rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'cyan', tag = 'caseVide')
					if yAxes == posEscalator[4][0] and xAxes == posEscalator[4][1]: rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'brown', tag = 'caseVide')
					if yAxes == posEscalator[5][0] and xAxes == posEscalator[5][1]: rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'brown', tag = 'caseVide')
				## Affiche les pions ##
				if Plateau[yAxes][xAxes] == 1 : image(locX, locY, 'Warrior_pion_transp.gif', ancrage = 'center', tag = 'warrior')
				if Plateau[yAxes][xAxes] == 2 : image(locX, locY, 'Wizzard_pion_transp.gif', ancrage = 'center', tag = 'wizzard')
				if Plateau[yAxes][xAxes] == 3 : image(locX, locY, 'Elf_pion_transp.gif', ancrage = 'center', tag = 'elf')
				if Plateau[yAxes][xAxes] == 4 : image(locX, locY, 'Dwarf_pion_transp.gif', ancrage = 'center', tag = 'dwarf')
				## Affiche sortie on ou off ##
				if Plateau[yAxes][xAxes] == 5 : image(locX+1, locY, 'sortie_off.gif', ancrage = 'center', tag = 'exitOff')
				if Plateau[yAxes][xAxes] == 6 : image(locX+1, locY, 'sortie_on.gif', ancrage = 'center', tag = 'exitOn')
				## Affiche les cases vides ##
				if Plateau[yAxes][xAxes] == 7 : rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'grey', tag = 'caseVide')
				## Affiche les sabliers ##
				if Plateau[yAxes][xAxes] == 8 : image(locX+1, locY, 'sablierReverse2.gif', ancrage = 'center', tag = 'sablierReverse')
				## Affiche les murs horizontaux ##
				if (yAxes,xAxes) in posMurH: rectangle(xAxes*largeur, yAxes*largeur-3, xAxes*largeur+largeur, yAxes*largeur+3, remplissage = 'black', tag = 'murHorizontal')
				## Affiche les murs verticaux ##
				if (yAxes,xAxes-1) in posMurV: rectangle(xAxes*largeur-3, yAxes*largeur, xAxes*largeur+3, yAxes*largeur+largeur, remplissage = 'black', tag = 'murVertical')
				## Affiche les objets tant que la sortie n'est pas active ##
				if not sortieOn:
					if yAxes == posObjets[0][0] and xAxes == posObjets[0][1]: image(locX, locY, 'Warrior_objet_transp.gif', ancrage = 'center', tag = 'warriorObj')
					if yAxes == posObjets[1][0] and xAxes == posObjets[1][1]: image(locX, locY, 'Wizzard_objet_transp.gif', ancrage = 'center', tag = 'wizzardObj')
					if yAxes == posObjets[2][0] and xAxes == posObjets[2][1]: image(locX, locY, 'Elf_objet_transp.gif', ancrage = 'center', tag = 'elfObj')
					if yAxes == posObjets[3][0] and xAxes == posObjets[3][1]: image(locX, locY, 'Dwarf_objet_transp.gif', ancrage = 'center', tag = 'dwarfObj')
				x += largeur
			x,y = 0,y+largeur

def pionsDroite():
	"""
	Affiche les icônes de pions et leur objet sur le côté, ainsi qu'un rond indiquant quel pion est séléctionné.
	"""
	texte(nbCasesX*largeur +175, largeur*0.5, 'État des pions :',taille = 22, ancrage = 'center')
	#Affiche les icônes propres à chaque pion
	image(nbCasesX*largeur +125, largeur*1.5, 'Warrior_pion_transp.gif', ancrage = 'center')
	texte(nbCasesX*largeur +175, largeur*1.5, '→', taille = '30', ancrage = 'center')
	image(nbCasesX*largeur +225, largeur*1.5, 'Warrior_objet_transp.gif', ancrage = 'center')

	image(nbCasesX*largeur +125, largeur*2.5, 'Wizzard_pion_transp.gif', ancrage = 'center')
	texte(nbCasesX*largeur +175, largeur*2.5, '→', taille = '30', ancrage = 'center')
	image(nbCasesX*largeur +225, largeur*2.5, 'Wizzard_objet_transp.gif', ancrage = 'center')

	image(nbCasesX*largeur +125, largeur*3.5, 'Elf_pion_transp.gif', ancrage = 'center')
	texte(nbCasesX*largeur +175, largeur*3.5, '→', taille = '30', ancrage = 'center')
	image(nbCasesX*largeur +225, largeur*3.5, 'Elf_objet_transp.gif', ancrage = 'center')

	image(nbCasesX*largeur +125, largeur*4.5 -6, 'Dwarf_pion_transp.gif', ancrage = 'center')
	texte(nbCasesX*largeur +175, largeur*4.5, '→', taille = '30', ancrage = 'center')
	image(nbCasesX*largeur +225, largeur*4.5, 'Dwarf_objet_transp.gif', ancrage = 'center')

def pionSelected(pion):
	"""
	Affiche un rond autour dsu pion séléctionné.
	"""
	efface('selecPion')
	cercle(nbCasesX*largeur +125, largeur*1.5 +(pion-1)*largeur, 25, epaisseur = 2, couleur = 'purple', tag = 'selecPion')

def actionSelectedJ1(i):
	"""
	Affiche un rond autour de l'action séléctionnée pour le Joueur 1.
	"""
	efface('selecActionJ1')
	cercle(nbCasesX*largeur +20 +(i-1)*50, largeur*6.5, 25, epaisseur = 2, couleur = 'red', tag = 'selecActionJ1')

def actionSelectedJ2(i):
	"""
	Affiche un rond autour de l'action séléctionnée pour le Joueur 1.
	"""
	efface('selecActionJ2')
	cercle(nbCasesX*largeur +20 +(i-1)*50, largeur*8.5, 25, epaisseur = 2, couleur = 'blue', tag = 'selecActionJ2')

def actionSelectedJ3(i):
	"""
	Affiche un rond autour de l'action séléctionnée pour le Joueur 3.
	"""
	efface('selecActionJ3')
	cercle(nbCasesX*largeur +20 +(i-1)*50, largeur*10.5, 25, epaisseur = 2, couleur = 'orange', tag = 'selecActionJ3')

def actionSelection():
	"""
	Affiche un cercle de couleur, suivi du joueur qui contrôle cette couleur ainsi que les commandes pour déplacer son pion
	"""
	efface('imgActions')
	actions_img = {'Left' : 'direction_gauche.gif', 'Up' : 'direction_haut.gif', 'Down' : 'direction_bas.gif', 'Right' : 'direction_droite.gif',
	'Vortex' : 'Vortex_transp_on.gif', 'Escalators' : 'Escalator_transp.gif', 'Exploration' : 'loupe.gif'}
	
	pionSelected(pionVisé)
	## Actions J1 ##
	if nbrJoueurs == '1 joueur' or nbrJoueurs == '2 joueurs' or nbrJoueurs == '3 joueurs':
		actionSelectedJ1(actionViséeJ1)
		texte(nbCasesX*largeur +175, largeur*5.5, 'Joueur 1', couleur ='red', taille = 18, ancrage = 'center')
		n=1
		for i in actionsJ1:
			image(nbCasesX*largeur-30 +n*50, largeur*6.5, str(actions_img.get(i)), ancrage = 'center', tag = 'imgActions')
			n+=1
	## Actions J2 ##
	if nbrJoueurs == '2 joueurs' or nbrJoueurs == '3 joueurs':
		actionSelectedJ2(actionViséeJ2)
		texte(nbCasesX*largeur +175, largeur*7.5, 'Joueur 2', couleur ='blue', taille = 18, ancrage = 'center')
		n=1
		for i in actionsJ2:
			image(nbCasesX*largeur-30 +n*50, largeur*8.5, str(actions_img.get(i)), ancrage = 'center', tag = 'imgActions')
			n+=1
	## Actions J3 ##
	if nbrJoueurs == '3 joueurs':
		actionSelectedJ3(actionViséeJ3)
		texte(nbCasesX*largeur +175, largeur*9.5, 'Joueur 3', couleur ='orange', taille = 18, ancrage = 'center')
		n=1
		for i in actionsJ3:
			image(nbCasesX*largeur-30 +n*50, largeur*10.5, str(actions_img.get(i)), ancrage = 'center', tag = 'imgActions')
			n+=1

def objectif(sortie):
	"""
	Affiche en bas à droite les objets restants à vole.
	"""
	# Affiche les objets manquants tant que la sortie n'est pas active
	texte(nbCasesX*largeur +175, (nbCasesY*largeur)/2 + 3.8*largeur, 'Objectif actuel :',taille = 22, ancrage = 'center')
	if not sortie:
		image(nbCasesX*largeur +175, (nbCasesY*largeur)/2 + 5*largeur, 'Warrior_objet_transp.gif', ancrage = 'center', tag= 'WarriorObjetPrit')
		image(nbCasesX*largeur +175, (nbCasesY*largeur)/2 + 6*largeur, 'Wizzard_objet_transp.gif', ancrage = 'center', tag= 'WizzardObjetPrit')
		image(nbCasesX*largeur +175, (nbCasesY*largeur)/2 + 7*largeur, 'Elf_objet_transp.gif', ancrage = 'center', tag= 'ElfObjetPrit')
		image(nbCasesX*largeur +175, (nbCasesY*largeur)/2 + 8*largeur, 'Dwarf_objet_transp.gif', ancrage = 'center', tag= 'DwarfObjetPrit')
	if sortie: image(nbCasesX*largeur +175, (nbCasesY*largeur)/2 + 6*largeur, 'sortie_on.gif', ancrage = 'center', tag= 'SortieOn')
	# Efface l'objet en bas à droite si le pion est dessus
	for yAxes in range(nbCasesY):
		for xAxes in range(nbCasesX):
			if Plateau[yAxes][xAxes] == 1:
				if yAxes == posObjets[0][0] and xAxes == posObjets[0][1]: efface('WarriorObjetPrit')
			if Plateau[yAxes][xAxes] == 2:
				if yAxes == posObjets[1][0] and xAxes == posObjets[1][1]: efface('WizzardObjetPrit')
			if Plateau[yAxes][xAxes] == 3:
				if yAxes == posObjets[2][0] and xAxes == posObjets[2][1]: efface('ElfObjetPrit')
			if Plateau[yAxes][xAxes] == 4:
				if yAxes == posObjets[3][0] and xAxes == posObjets[3][1]: efface('DwarfObjetPrit')
					
def timer(seconde, startTime, etatReverse) :
	"""
	Affiche un timer décroissant en secondes, depuis le nombre rentré en paramètre.
	"""
	global minutes, secondes, secElapsed
	couleur = 'dark green'

	if etatReverse == False:
		secElapsed = int((time.time() - (startTime+a*2) )) 	# Secondes écoulées depuis le début du programme
		secLeft = seconde - secElapsed						# Secondes restantes
	if etatReverse == True:
		secElapsed = int((time.time() - (startTime+a) ))
		secLeft = a - secElapsed
	# Conversion du temps en minutes:secondes
	minutes = secLeft // 60
	secondes = secLeft - minutes*60
	if minutes < 0:	perdu()									# Si le temps tombe à 0, partie perdue.
	if minutes == 0 and secondes < 30: couleur = 'red'		# Si - de 30sec restantes : couleur rouge
	#Affichage du temps restant en secondes
	efface('timer')
	texte(largeur//2, nbCasesY*largeur+37.5, "Temps restant: " + str(minutes) + "min" + str(secondes), couleur=couleur, taille = 20, tag = "timer", ancrage = 'w')

def instructions():
	"""
	Affiche sous forme de texte les actions que le joueur peut faire
	"""
	efface('commandes')
	efface('selectorInstructions')
	efface('quitterInstructions')
	efface('movePionInstructions')
	efface('debugModeInstructions')
	efface('Tableau')
	texte(largeur*6 +longueur_texte(minutes+secondes)+longueur_texte('min')-10, nbCasesY*largeur+12, "Commandes:", couleur='black', taille = 14, ancrage = 'w', tag = 'commandes')
	texte(largeur*6 +longueur_texte(minutes+secondes)+longueur_texte('min') +27.5, nbCasesY*largeur+30, "F1 : Quitter le jeu", couleur='black', taille = 12, ancrage = 'w', tag = 'selectorInstructions')
	texte(largeur*6 +longueur_texte(minutes+secondes)+longueur_texte('min') +37.5, nbCasesY*largeur+50, "F2 : Débug mode (on/off)", couleur='black', taille = 12, ancrage = 'w', tag = 'movePionInstructions')
	image(largeur*6 +longueur_texte(minutes+secondes)+longueur_texte('min') +500, nbCasesY*largeur+40, 'Tableau_cmdJ.gif', ancrage = 'w', tag= 'Tableau')
	texte(largeur*6 +220 +longueur_texte(minutes+secondes)+longueur_texte('min') +27.5, nbCasesY*largeur+30, "F3 : Sauvegarder", couleur='black', taille = 12, ancrage = 'w', tag = 'quitterInstructions')
	texte(largeur*6 +220 +longueur_texte(minutes+secondes)+longueur_texte('min') +27.5, nbCasesY*largeur+50, "e : Changer de pion à déplacer", couleur='black', taille = 12, ancrage = 'w', tag = 'debugModeInstructions')

def affichageDroit():
	if touche != None :
		pionsDroite()
		actionSelection()
		ligne(nbCasesX*largeur +7, nbCasesY*largeur-300, nbCasesX*largeur +343, nbCasesY*largeur-300, couleur='black', epaisseur=3)
		objectif(sortieOn)

def affichageBas():
	efface('separationBas')
	timer(9999, startTime, reverseTimer)
	ligne(largeur*5.3+longueur_texte(minutes+secondes)+longueur_texte('min'), nbCasesY*largeur+12, largeur*5.3+longueur_texte(minutes+secondes)+longueur_texte('min'), nbCasesY*largeur+65, couleur='black', epaisseur=3, tag = 'separationBas')
	instructions()

def perdu():
	"""
	Si tous les pions ne sont pas sortis avant la fin du temps impartit, la partie est perdue.
	"""
	efface_tout()
	while 1 :
		texte((nbCasesX//2+1)*largeur, (nbCasesY//2-1)*largeur, "Temps écoulé, perdu..", couleur="red", ancrage = "center", taille = 45)
		texte((nbCasesX//2+1)*largeur, (nbCasesY//1.5)*largeur, "Vous ferez mieux la prochaine fois, retentez votre chance!", couleur="black", ancrage = "center", taille = 25)
		attente_clic()
		break
	ferme_fenetre()

def gagner(min, sec):
	"""
	Si tous les pions sont sortis, la prtie est gagnée.
	"""
	efface_tout()
	s = 60-sec
	while 1 :
		texte((nbCasesX//2+1)*largeur, (nbCasesY//2-1)*largeur, "Vous avez gagné!", couleur="dark green", ancrage = "center", taille = 45)
		texte((nbCasesX//2+1)*largeur, (nbCasesY//1.5)*largeur, "Félicitations, vous avez finit le jeu en " + str(min) + "min" + str(s), couleur="black", ancrage = "center", taille = 25)
		attente_clic()
		break	
	ferme_fenetre()

# ----------------------- Main Program --------------------------- #
if __name__ == '__main__':
	creationMap(18,18)

	## Création entités ##
	directions = ['Left', 'Right', 'Up', 'Down']
	special = ['Vortex', 'Escalators', 'Exploration']
	sortieOn = False
	pionsInSortie = 0
	posObjets = [(1,1),(5,14),(15,5),(10,12)]
	posVortex_War, posVortex_Wiz, posVortex_Elf, posVortex_Dwa = [(1,2)], [(0,4)], [(0,6)], [(0,17),(4,17)]
	posEscalator = [(0,10),(1,11),(7,1),(8,3),(13,9),(12,10)]
	posMurH = [(1,11),(1,12),(1,13),(2,4),(3,6),(3,7),(3,8),(4,0),(4,1),(4,3),(4,4),(4,5),(4,6),(4,11),(4,14),(5,7),(5,8),(5,9),(5,10),
	(6,15),(6,16),(6,17),(7,3),(7,4),(8,4),(8,12),(8,13),(8,15),(8,16),(8,17),(9,3),(9,17),(10,13),(10,14),(10,16),(11,0),(11,1),(11,5),(11,13),
	(10,14),(11,17),(12,5),(12,12),(12,16),(13,0),(13,1),(13,7),(13,8),(13,17),(14,7),(14,8),(14,9),(14,12),(14,13),(14,14),
	(15,0),(15,5),(16,1),(16,4),(16,9),(16,12),(16,13),(16,17),(17,0),(17,5),(17,6),(17,7),(17,16)]
	posMurV = [(0,3),(0,5),(0,9),(0,15),(1,3),(1,5),(1,9),(1,10),(1,13),(1,15),(2,3),(2,4),(2,5),(2,9),(2,10),(2,13),(2,15),
	(3,9),(3,10),(3,13),(4,2),(4,6),(4,11),(5,1),(5,2),(5,5),(5,11),(5,12),(6,2),(6,12),(6,14),(7,1),(7,2),(8,2),(8,4),(8,13),(8,15),
	(9,1),(9,2),(9,4),(9,12),(9,15),(10,2),(10,15),(11,3),(11,13),(11,15),(12,4),(12,9),(12,12),(12,15),(13,1),(13,3),(13,4),(14,1),(14,3),(14,4),
	(14,11),(14,14),(15,2),(15,3),(15,6),(15,8),(15,11),(15,14),(16,2),(16,4),(16,9),(16,11),(16,14),(17,1),(17,3),(17,11),(17,12),(17,16)]
	Plateau = [ [7,7,7,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0],
				[7,11,0,0,0,0,0,7,7,0,0,0,0,0,0,0,8,0],
				[7,0,7,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,7],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0],
				[7,0,0,0,8,0,0,0,0,0,0,0,0,0,12,0,0,0],
				[7,0,0,0,0,0,7,7,0,0,7,7,0,0,0,0,0,0],
				[7,0,0,0,0,0,7,0,0,0,0,7,0,0,0,0,0,0],
				[7,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0],
				[7,0,0,0,0,0,0,0,3,4,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,7,0,0,0,0,7,14,0,0,0,0,0],
				[0,0,0,0,0,0,7,7,0,0,7,7,0,0,0,0,0,0],
				[0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0],
				[0,0,7,0,0,0,7,0,0,0,0,0,0,0,0,0,7,0],
				[0,0,0,0,0,13,0,0,0,0,8,0,0,0,0,0,7,0],
				[0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
	## Menu ##
	affichageMenu()
	if nbrJoueurs == '1 joueur': actions1J()
	if nbrJoueurs == '2 joueurs': actions2J()
	if nbrJoueurs == '3 joueurs': actions3J()

	## Initialisations variables ##
	startTime = time.time()
	pionVisé, actionViséeJ1, actionViséeJ2, actionViséeJ3 = 1, 1, 1, 1
	debugMode, reverseTimer = False, False
	objetsOwn = 0
	a = 0

	## Boucle principale ##
	while 1:
		affichageBas()
		affichageDroit()
		affichage()
		isWin(pionsInSortie, minutes, secondes)
		sortieOn = isSortieOn(sortieOn)
		debugMode = actionTouche(pionVisé, actionViséeJ1, actionViséeJ2, actionViséeJ3, objetsOwn, pionsInSortie, debugMode)
		mise_a_jour()
		if touche != None:
			efface_tout()

# GRISER L'IMAGE DU PION QUAND IL NE PEUT PLUS ETRE SELECTIONNER (quand il est sortit) #