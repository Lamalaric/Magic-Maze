# -------------------------- Import ------------------------------ #
import os
import time
from upemtk import *
from random import *

# ------------------------- Fonctions ---------------------------- #

# ----------- Menu du jeu ------------ #

def affichageMenu():
	"""
	Créée le menu avec du texte et des rectangles servant de "boutons"
	"""
	global choix, xy1_Jouer, xy1_Load, xy2_Load, xy2_Jouer, xy1_Rules, xy2_Rules, xy1_Close, xy2_Close
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
	rectangle(largeur*13, largeur*11, largeur*nbCasesX, largeur*13, remplissage="darkblue", tag = 'rulesButton')
	texte(largeur*15.5, largeur*11.5, "Règles", couleur="white", ancrage="n", tag = 'rules')
	xy1_Rules = largeur*13, largeur*11
	xy2_Rules = largeur*nbCasesX, largeur*13

	## On regarde sur quel bouton le joueur à appuyer ##
	choix = choixMenu()
	if choix == 'Règles':
		rules()
	if choix == 'Continuer':
		affichageMenu()
	if choix == 'Jouer':
		nombreJoueurs()

def choixMenu():
	"""
	Compare les coordonnées du clic aux coordonnées des rectangles du menus.
	Si le clic est dans le rectangle "Jouer" : on lance le jeu.
	Si le clic est dans le rectangle "Règles" : on affiche les règles.
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
	if coordClic[0] > xy1_Rules[0] and coordClic[0] < xy2_Rules[0]:
		if coordClic[1] > xy1_Rules[1] and coordClic[1] < xy2_Rules[1]:
			return 'Règles'
		else:					# Si on clique ailleur dans la fenêtre, on reste sur le menu.
			affichageMenu()
	else:
		affichageMenu()

def nombreJoueurs():
	"""
	Affiche 2 boutons permettant au joueur de choisir si il veut jouer à 1 ou 2 joueurs.
	"""
	global nbrJoueurs, xy1_1j, xy2_1j, xy1_2j, xy2_2j
	## Titre du jeu ##
	efface_tout()
	image(largeur*nbCasesX/2+100, 10, 'titreJeu.gif', ancrage="n")

	texte(largeur*nbCasesX/2+100, largeur*4, "Choisissez une action", couleur="black", taille=30, ancrage="n")
	## Cadre ##
	rectangle(largeur*2, largeur*3.5, (nbCasesX*largeur+200)-(largeur*2), (nbCasesY*largeur+75)-(largeur*3), epaisseur = 3, couleur = 'red', tag = 'cadreMenu')
	## Bouton jouer ##
	rectangle(largeur*4, largeur*7, (nbCasesX*largeur)/2, largeur*9, remplissage="green", tag = 'startButton')
	texte(largeur *6.5, largeur*7.5, "1 joueur", couleur="white", taille=25, ancrage="n", tag = 'start')
	xy1_1j = largeur*4, largeur*7
	xy2_1j = (nbCasesX*largeur)/2, largeur*9
	## Bouton continuer ##
	rectangle(largeur*13, largeur*7, largeur*nbCasesX, largeur*9, remplissage="orange", tag = 'loadButton')
	texte(largeur*15.5, largeur*7.5, "3 joueurs", couleur="white", ancrage="n", tag = 'load')
	xy1_2j = largeur*13, largeur*7
	xy2_2j = largeur*nbCasesX, largeur*9

	nbrJoueurs = choixJoueur()
	efface('cadreMenu')
	if nbrJoueurs == '1 joueur':
		return '1j'
	if nbrJoueurs == '3 joueurs':
		return '3j'

def choixJoueur():
	"""
	Compare les coordonnées du clic aux coordonnées des rectangles du menus.
	Si le clic est dans le rectangle "1 joueur" : on lance le jeu en mode 1 joueur.
	Si le clic est dans le rectangle "2 joueurs" : on lance le jeu en mode 2 joueurs.
	"""
	coordClic = attente_clic()
	## Actionner bouton 1 joueur ##
	if coordClic[0] > xy1_1j[0] and coordClic[0] < xy2_1j[0]:
		if coordClic[1] > xy1_1j[1] and coordClic[1] < xy2_1j[1]:
			return '1 joueur'
	## Actionner bouton 2 joueurs ##
	if coordClic[0] > xy1_2j[0] and coordClic[0] < xy2_2j[0]:
		if coordClic[1] > xy1_2j[1] and coordClic[1] < xy2_2j[1]:
			return '3 joueurs'
		else:					# Si on clique ailleur dans la fenêtre, on reste sur la page actuelle.
			choixJoueur()
	else:
		choixJoueur()

def rules():
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
	texte(5, 305, "", couleur='black', ancrage='w', taille=12)
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
		else:
			rules()
	else:
		rules()



# ---------- Partie Logique ---------- #

def creationMap(l, L) :
	"""
	Créer une fenêtre avec un nombre de cases en X et Y donné.
	Créer une matrice remplie de 0
	"""
	global nbCasesX, nbCasesY, largeur, Plateau 
	largeur = 50	# Largeur des carrés
	nbCasesX = l
	nbCasesY = L

	Plateau = []	# Création de la matrice
	for yAxes in range(nbCasesY):
		Plateau.append([])				# Dans chaque ligne du plateau
		for xAxes in range(nbCasesX):
			Plateau[yAxes].append(0)	# On met un 0, qui représente une case vide

	cree_fenetre((nbCasesX*largeur+200), (nbCasesY*largeur + 75))	# Création de la fenêtre

def creationPion():
	"""
	Définit la position de départ de chaque pion sur le plateau.
	Les pions sont contrôllés par les joueurs et doivent tous sortir avant la fin du temps impartit.
	"""
	pionVisé1 = 1
	pionVisé2 = 2
	midX = len(Plateau[0]) // 2 -1		# On stock où est la moitié de l'axe X
	midY = len(Plateau) // 2			# On stock où est la moitié de l'axe Y
	# On définit l'emplacement initial de chaque pion
	Plateau[midY-1][midX] = 1
	Plateau[midY-1][midX+1] = 2
	Plateau[midY][midX] = 3
	Plateau[midY][midX+1] = 4

def creationObjet():
	"""
	Génère 4 objets dans la matrice.
	Chaque joueur doit récupérer son objet.
	"""
	global posObjets
	idObjet = 11
	posObjets = []
	objetsCrées = 0

	while objetsCrées != 4:
		rdmY = randint(0,nbCasesY-1)
		rdmX = randint(0,nbCasesX-1)
		# On ajoute les objets un par un sur des cases libres.
		if Plateau[rdmY][rdmX] == 0 :
			Plateau[rdmY][rdmX] = idObjet
			posObjets.append((rdmY,rdmX))
			idObjet += 1
			objetsCrées += 1

	

def creationSablier(n):
	"""	
	Définit la position de la sortie
	"""
	sablierCréée=0
	while sablierCréée != n:
		rdmY = randint(0,nbCasesY-1)
		rdmX = randint(0,nbCasesX-1)
	# On place un sablier sur une case libre.
		if Plateau[rdmY][rdmX] == 0 :
			Plateau[rdmY][rdmX] = 8
			sablierCréée+=1

def creationSortie():
	"""	
	Définit la position de la sortie
	"""
	rdmY = randint(0,nbCasesY-1)
	rdmX = randint(0,nbCasesX-1)
	sortieCréée=0
	while sortieCréée != 1:
	# On place une sortie sur une case libre.
		if Plateau[rdmY][rdmX] == 0 :
			Plateau[rdmY][rdmX] = 5
			sortieCréée+=1

def creationMur(n) : 
	"""
	Génère n murs dans la matrice.
	Les joueurs ne peuvent pas traverser un mur.
	"""
	mursCrées = 0
	while mursCrées != n :
		rdmY = randint(0,nbCasesY-1)
		rdmX = randint(0,nbCasesX-1)
		# On ajoute un mur sur une case libre.
		if Plateau[rdmY][rdmX] == 0 :
			Plateau[rdmY][rdmX] = 20
			mursCrées += 1
def creationCaseVide(n) : 
	"""
	Génère n cases vides dans la matrice.
	Les joueurs ne peuvent pas aller sur les cases vides.
	"""
	caseVidesCrées = 0
	while caseVidesCrées != n :
		rdmY = randint(0,nbCasesY-1)
		rdmX = randint(0,nbCasesX-1)
		# On ajoute une case vide sur des cases libres.
		if Plateau[rdmY][rdmX] == 0 :
			Plateau[rdmY][rdmX] = 7
			caseVidesCrées += 1

def pionAimed1(pionChoisi1):
	"""
	Fonctionne avec la fonction pionSelected1(i), qui permet de choisir le pion à actionner.
	Elle renvoie le pion séléctionné à bouger.
	"""
	global pionVisé11
	pionVisé11 = pionChoisi1
	pionVisé11 += 1
	# Lorsque appelé, le pion à actionner sera le supérieur au précédent
	if pionVisé11 > 4:
		pionVisé11 = 1
	return pionVisé11

def isSortieOn(etatSortie):
	"""
	Active la sortie si tous les joueurs sont sur leur case objet.
	"""	
	if etatSortie == False :
		pionsSurObj = 0
		for yAxes in range(nbCasesY):
			for xAxes in range(nbCasesX):
				# +1 si un pion est sur sa case objet.
				if Plateau[yAxes][xAxes] == 1:
					if yAxes == posObjets[0][0] and xAxes == posObjets[0][1]:
						pionsSurObj += 1
				if Plateau[yAxes][xAxes] == 2:
					if yAxes == posObjets[1][0] and xAxes == posObjets[1][1]:
						pionsSurObj += 1
				if Plateau[yAxes][xAxes] == 3:
					if yAxes == posObjets[2][0] and xAxes == posObjets[2][1]:
						pionsSurObj += 1
				if Plateau[yAxes][xAxes] == 4:
					if yAxes == posObjets[3][0] and xAxes == posObjets[3][1]:
						pionsSurObj += 1
		# Si tous les pions sont sur leur case objet : sortie active
		if pionsSurObj == 4:
			for yAxes in range(nbCasesY):
				for xAxes in range(nbCasesX):
					if Plateau[yAxes][xAxes] == 5:
						Plateau[yAxes][xAxes] = 6
						efface('exitOff')
						image(12*largeur+26, 3*largeur-25, 'Vortex_transp_on.gif', ancrage = 'center', tag = 'exitOn')
						return True
		return False
	return True

def isWin(pionsSortis, min, sec):
	"""
	Si les 4 joueurs ont atteints la sortie, la partie s'arrête et on à gagner.
	"""
	if pionsSortis == 4:
		gagner(minutes, secondes)

def actionTouche(player1, player2, player3, objets, pionsSortis, debug):
	"""
	Gère les déplacements à faire selon chaque touche directionnelle appuyée.
	Selon la case à laquelle veut aller un pion, l'action sera différente.

	Cette fonction s'occupe également de récupérer la touche appuyée et exécuter l'action correspondante.
	"""
	global touche, pionVisé1, pionVisé2, pionVisé3, pionsInSortie, reverseTimer, a, secElapsed
	dejaVu = False
	touche = attente_touche_jusqua(1000)
	choixMove = ['Left', 'Right', 'Up', 'Down']
	choixPion = [1, 2, 3, 4]

	# Ferme la fenêtre si la touche appuyée est 'F2'
	if touche == 'F2' :
		ferme_fenetre()
	# Change de pion à bouger pour le J1 si la touche appuyée est 'e'
	if touche == 'e' :
		pionVisé1 = pionAimed1(pionVisé1)
	# # Change de pion à bouger pour le J2 si la touche appuyée est 'r'
	# if touche == 'r' :
	# 	pionVisé2 = pionAimed2(pionVisé2)
	# # Change de pion à bouger pour le J3 si la touche appuyée est 't'
	# if touche == 't' :
	# 	pionVisé3 = pionAimed3(pionVisé3)
	# Mode debug on/off
	if touche == 'F1':
		debug = not debug
	if debug == True :		# Choix des mouvements / pions à actionner aléatoire
		touche = choixMove[randint(0,3)]
		player1 = choixPion[randint(0,3)]
	# Action à faire à chaque touche
	if touche != None:
		for yAxes in range(nbCasesY):
			for xAxes in range(nbCasesX):
				if Plateau[yAxes][xAxes] == player1 or Plateau[yAxes][xAxes] == player1+20 or Plateau[yAxes][xAxes] == player1+25:

					## Aller à gauche ##
					if touche == 'Left':
						if xAxes > 0 :									# Si case visée is not 'bord du plateau'
							if Plateau[yAxes][xAxes] == player1+20:			# Si c'est un pion sur un mur horizontal
								if Plateau[yAxes][xAxes-1] == 0:				# Si case visée = vide
									Plateau[yAxes][xAxes-1], Plateau[yAxes][xAxes] = player1, 20
									break
								if Plateau[yAxes][xAxes-1] == 20:				# Si case visée = mur horizontal
									Plateau[yAxes][xAxes-1], Plateau[yAxes][xAxes] = player1+20, 20
									break
								if Plateau[yAxes][xAxes-1] == player1+10:		# Si case visée = objet
									Plateau[yAxes][xAxes-1], Plateau[yAxes][xAxes] = player1, 20
									break
							if Plateau[yAxes][xAxes] == player1+25:			# Si c'est un pion sur un mur vertical
								if Plateau[yAxes][xAxes-1] == 0:				# Si case visée = vide
									Plateau[yAxes][xAxes-1], Plateau[yAxes][xAxes] = player1, 25
									
								if Plateau[yAxes][xAxes-1] == 20:				# Si case visée = mur horizontal
									Plateau[yAxes][xAxes-1], Plateau[yAxes][xAxes] = player1+20, 25
									break
								if Plateau[yAxes][xAxes-1] == 25:				# Si case visée = mur vertical
									Plateau[yAxes][xAxes-1], Plateau[yAxes][xAxes] = player1+25, 25
									break
								if Plateau[yAxes][xAxes-1] == player1+10:		# Si case visée = objet
									Plateau[yAxes][xAxes-1], Plateau[yAxes][xAxes] = player1, 25
									break
								if Plateau[yAxes][xAxes-1] == 6 :				# Si case visée = sortie active
									Plateau[yAxes][xAxes] = 25
									pionsInSortie += 1
									break
								if Plateau[yAxes][xAxes-1] == 8 :				# Si case visée = sablier
									Plateau[yAxes][xAxes-1], Plateau[yAxes][xAxes] = player1, 25
									reverseTimer = not reverseTimer
									a = secElapsed
									secElapsed = 0
									break
							if Plateau[yAxes][xAxes-1] == 0 :				# Si case visée = vide
								Plateau[yAxes][xAxes-1], Plateau[yAxes][xAxes] = player1, 0
								break
							if Plateau[yAxes][xAxes-1] == player1+10 :		# Si case visée = objet
								Plateau[yAxes][xAxes-1],Plateau[yAxes][xAxes] = player1, 0
								break
							if Plateau[yAxes][xAxes-1] == 6 :				# Si case visée = sortie active
								pionsInSortie += 1
								break
							if Plateau[yAxes][xAxes-1] == 8 :				# Si case visée = sablier
								Plateau[yAxes][xAxes-1], Plateau[yAxes][xAxes] = player1, 0
								reverseTimer = not reverseTimer
								a = secElapsed
								secElapsed = 0
								break
							if Plateau[yAxes][xAxes-1] == 20:				# Si case visée = mur horizontal
								Plateau[yAxes][xAxes-1], Plateau[yAxes][xAxes] = player1+20, 0
								break
							# Pour les escalators
							if Plateau[yAxes][xAxes-1] == 31 :		# Si case visée = escalator
								Plateau[yAxes][xAxes-1], Plateau[yAxes][xAxes] = player1, 0
								for i in range (len(Plateau)):
									for j in range (len(Plateau[0])):
										if Plateau[i][j]==30:
											Plateau[i][j], Plateau[yAxes][xAxes-1] = player1, 31										
											break
							if Plateau[yAxes][xAxes-1] == 30 :		# Si case visée = escalator
								Plateau[yAxes][xAxes-1], Plateau[yAxes][xAxes] = player1, 0
								for i in range (len(Plateau)):
									for j in range (len(Plateau[0])):
										if Plateau[i][j]==31:
											Plateau[i][j], Plateau[yAxes][xAxes-1] = player1, 30
											break
							if Plateau[yAxes][xAxes-1] == 32:		# Si case visée = escalator
								Plateau[yAxes][xAxes-1], Plateau[yAxes][xAxes] = player1, 20
								for i in range (len(Plateau)):
									for j in range (len(Plateau[0])):
										if Plateau[i][j]==33:
											Plateau[i][j], Plateau[yAxes][xAxes-1] = player1, 32										
											break
							if Plateau[yAxes][xAxes-1] == 33 :		# Si case visée = escalator
								Plateau[yAxes][xAxes-1], Plateau[yAxes][xAxes] = player1, 25
								for i in range (len(Plateau)):
									for j in range (len(Plateau[0])):
										if Plateau[i][j]==32:
											Plateau[i][j], Plateau[yAxes][xAxes-1] = player1, 33
											break


					## Aller à droite ##
					if touche == 'Right':
						if xAxes < nbCasesX-1 :							# Si case visée is not 'bord du plateau'
							if Plateau[yAxes][xAxes] == player1+20:			# Si c'est un pion sur un mur horizontal
								if Plateau[yAxes][xAxes+1] == 0:				# Si case visée = vide
									Plateau[yAxes][xAxes+1], Plateau[yAxes][xAxes] = player1, 20
									break
								if Plateau[yAxes][xAxes+1] == 20:				# Si case visée = mur horizontal
									Plateau[yAxes][xAxes+1], Plateau[yAxes][xAxes] = player1+20, 20
									break
								if Plateau[yAxes][xAxes+1] == 25:				# Si case visée = mur vertical
									Plateau[yAxes][xAxes+1], Plateau[yAxes][xAxes] = player1+25, 20
									break
								if Plateau[yAxes][xAxes+1] == player1+10 :		# Si case visée = objet
									Plateau[yAxes][xAxes+1], Plateau[yAxes][xAxes] = player1, 20
									break
								if Plateau[yAxes][xAxes+1] == 8 :				# Si case visée = sablier
									Plateau[yAxes][xAxes+1], Plateau[yAxes][xAxes] = player1, 20
									reverseTimer = not reverseTimer
									a = secElapsed
									secElapsed = 0
									break
							if Plateau[yAxes][xAxes] == player1+25:			# Si c'est un pion sur un mur verical
								break
							if Plateau[yAxes][xAxes+1] == 0:				# Si case visée = vide
								Plateau[yAxes][xAxes+1], Plateau[yAxes][xAxes] = player1, 0
								break
							if Plateau[yAxes][xAxes+1] == player1+10 :		# Si case visée = objet
								Plateau[yAxes][xAxes+1], Plateau[yAxes][xAxes] = player1, 0
								break
							if Plateau[yAxes][xAxes+1] == 6 :				# Si case visée = sortie active
								Plateau[yAxes][xAxes] = 0
								pionsInSortie += 1
								break
							if Plateau[yAxes][xAxes+1] == 8 :				# Si case visée = sablier
								Plateau[yAxes][xAxes+1], Plateau[yAxes][xAxes] = player1, 0
								reverseTimer = not reverseTimer
								a = secElapsed
								secElapsed = 0
								break
							if Plateau[yAxes][xAxes+1] == 20 :				# Si case visée = mur horizontal
								Plateau[yAxes][xAxes+1], Plateau[yAxes][xAxes] = player1+20, 0
								break
							if Plateau[yAxes][xAxes+1] == 25 :				# Si case visée = mur vertical
								Plateau[yAxes][xAxes+1], Plateau[yAxes][xAxes] = player1+25, 0
								break
							# Pour les escalators
							if Plateau[yAxes][xAxes+1] == 31 :		# Si case visée = escalator
								Plateau[yAxes][xAxes+1], Plateau[yAxes][xAxes] = player1, 0
								for i in range (len(Plateau)):
									for j in range (len(Plateau[0])):
										if Plateau[i][j]==30:
											Plateau[i][j], Plateau[yAxes][xAxes+1] = player1, 31
											break
							if Plateau[yAxes][xAxes+1] == 30 :		# Si case visée = escalator
								Plateau[yAxes][xAxes+1], Plateau[yAxes][xAxes] = player1, 0
								for i in range (len(Plateau)):
									for j in range (len(Plateau[0])):
										if Plateau[i][j]==31:
											Plateau[i][j], Plateau[yAxes][xAxes+1] = player1, 30
											break
							if Plateau[yAxes][xAxes+1] == 32 :		# Si case visée = escalator
								Plateau[yAxes][xAxes+1], Plateau[yAxes][xAxes] = player1, 0
								for i in range (len(Plateau)):
									for j in range (len(Plateau[0])):
										if Plateau[i][j]==33:
											Plateau[i][j], Plateau[yAxes][xAxes+1] = player1, 32
											break
							if Plateau[yAxes][xAxes+1] == 33 :		# Si case visée = escalator
								Plateau[yAxes][xAxes+1], Plateau[yAxes][xAxes] = player1, 0
								for i in range (len(Plateau)):
									for j in range (len(Plateau[0])):
										if Plateau[i][j]==32:
											Plateau[i][j], Plateau[yAxes][xAxes+1] = player1, 33
											break

					## Aller en haut ##
					if touche == 'Up':
						if yAxes > 0 :									# Si case visée is not 'bord du plateau'
							if Plateau[yAxes][xAxes] == player1+20:			# Si c'est un pion sur un mur horizontal
								if Plateau[yAxes-1][xAxes] == 0:				# Si case visée = vide
									Plateau[yAxes-1][xAxes], Plateau[yAxes][xAxes] = player1, 20
									break
								if Plateau[yAxes-1][xAxes] == 25:				# Si case visée = mur vertical
									Plateau[yAxes-1][xAxes], Plateau[yAxes][xAxes] = player1+25, 20
									break
								if Plateau[yAxes-1][xAxes] == player1+10 :		# Si case visée = objet
									Plateau[yAxes-1][xAxes], Plateau[yAxes][xAxes] = player1, 20
									break
								if Plateau[yAxes-1][xAxes] == 8 :				# Si case visée = sablier
									Plateau[yAxes-1][xAxes], Plateau[yAxes][xAxes] = player1, 20
									reverseTimer = not reverseTimer
									a = secElapsed
									secElapsed = 0
									break
							if Plateau[yAxes][xAxes] == player1+25:			# Si c'est un pion sur un mur vertical
								if Plateau[yAxes-1][xAxes] == 0:				# Si case visée = vide
									Plateau[yAxes-1][xAxes], Plateau[yAxes][xAxes] = player1, 25
									break
								if Plateau[yAxes-1][xAxes] == 25:				# Si case visée = mur vertical
									Plateau[yAxes-1][xAxes], Plateau[yAxes][xAxes] = player1+25, 25
									break
								if Plateau[yAxes-1][xAxes] == 8 :				# Si case visée = sablier
									Plateau[yAxes-1][xAxes], Plateau[yAxes][xAxes] = player1, 25
									reverseTimer = not reverseTimer
									a = secElapsed
									secElapsed = 0
									break
							if Plateau[yAxes-1][xAxes] == 0:				# Si case visée = vide
								Plateau[yAxes-1][xAxes], Plateau[yAxes][xAxes] = player1, 0
								break
							if Plateau[yAxes-1][xAxes] == player1+10 :		# Si case visée = objet
								Plateau[yAxes-1][xAxes], Plateau[yAxes][xAxes] = player1, 0
								break
							if Plateau[yAxes-1][xAxes] == 6 :				# Si case visée = sortie active
								Plateau[yAxes][xAxes] = 0
								pionsInSortie += 1
								break
							if Plateau[yAxes-1][xAxes] == 8 :				# Si case visée = sablier
								Plateau[yAxes-1][xAxes], Plateau[yAxes][xAxes] = player1, 0
								reverseTimer = not reverseTimer
								a = secElapsed
								secElapsed = 0
								break
							if Plateau[yAxes-1][xAxes] == 25 :				# Si case visée = mur vertical
								Plateau[yAxes-1][xAxes], Plateau[yAxes][xAxes] = player1+25, 0
								break

							# Pour les escalators
							if Plateau[yAxes-1][xAxes] == 31 :		# Si case visée = escalator
									Plateau[yAxes-1][xAxes], Plateau[yAxes][xAxes] = player1, 0
									for i in range (len(Plateau)):
										for j in range (len(Plateau[0])):
											if Plateau[i][j]==30:
												Plateau[i][j], Plateau[yAxes-1][xAxes] = player1, 31
												break
							if Plateau[yAxes-1][xAxes] == 30 :		# Si case visée = escalator
									Plateau[yAxes-1][xAxes], Plateau[yAxes][xAxes] = player1, 0
									for i in range (len(Plateau)):
										for j in range (len(Plateau[0])):
											if Plateau[i][j]==31:
												Plateau[i][j], Plateau[yAxes-1][xAxes] = player1, 30
												break
							if Plateau[yAxes-1][xAxes] == 33 :		# Si case visée = escalator
									Plateau[yAxes-1][xAxes], Plateau[yAxes][xAxes] = player1, 20
									for i in range (len(Plateau)):
										for j in range (len(Plateau[0])):
											if Plateau[i][j]==32:
												Plateau[i][j], Plateau[yAxes-1][xAxes] = player1, 33
												break
							if Plateau[yAxes-1][xAxes] == 32 :		# Si case visée = escalator
									Plateau[yAxes-1][xAxes], Plateau[yAxes][xAxes] = player1, 0
									for i in range (len(Plateau)):
										for j in range (len(Plateau[0])):
											if Plateau[i][j]==33:
												Plateau[i][j], Plateau[yAxes-1][xAxes] = player1, 32
												break

							

					## Aller en bas ##
					if touche == 'Down':
						if yAxes < nbCasesY-1:								# Si case visée is not 'bord du plateau'
							if dejaVu == False :
								if Plateau[yAxes][xAxes] == player1+25:			# Si c'est un pion sur un mur vertical
									if Plateau[yAxes+1][xAxes] == 0:				# Si case visée = vide
										Plateau[yAxes+1][xAxes], Plateau[yAxes][xAxes] = player1, 25
										dejaVu = True
										break
									if Plateau[yAxes+1][xAxes] == 25:				# Si case visée = mur vertical
										Plateau[yAxes+1][xAxes], Plateau[yAxes][xAxes] = player1+25, 25
										dejaVu = True
										break
									if Plateau[yAxes+1][xAxes] == 20:				# Si case visée = mur horizontal
										Plateau[yAxes+1][xAxes], Plateau[yAxes][xAxes] = player1+20, 25
										dejaVu = True
										break
									if Plateau[yAxes+1][xAxes] == player1+10 :		# Si case visée = objet
										Plateau[yAxes+1][xAxes], Plateau[yAxes][xAxes] = player1, 25
										dejaVu = True
										break
								if Plateau[yAxes][xAxes] == player1+20:			# Si c'est un pion sur un mur horizontal
									break
								if Plateau[yAxes+1][xAxes] == 0 :				# Si case visée = vide
									if Plateau[yAxes][xAxes] != player1+20:			# Si case != pion + mur vertical
										Plateau[yAxes+1][xAxes], Plateau[yAxes][xAxes] = player1, 0
										dejaVu = True
										break
								if Plateau[yAxes+1][xAxes] == player1+10 :		# Si case visée = objet
									Plateau[yAxes+1][xAxes], Plateau[yAxes][xAxes] = player1, 0
									dejaVu = True
									break
								if Plateau[yAxes+1][xAxes] == 6 :				# Si case visée = sortie active
									Plateau[yAxes][xAxes] = 0
									pionsInSortie += 1
									break
								if Plateau[yAxes+1][xAxes] == 8 :				# Si case visée = sablier
									Plateau[yAxes+1][xAxes], Plateau[yAxes][xAxes] = player1, 0
									reverseTimer = not reverseTimer
									a = secElapsed
									secElapsed = 0
									dejaVu = True
									break
								if Plateau[yAxes+1][xAxes] == 20 :				# Si case visée = mur horizontal
									Plateau[yAxes+1][xAxes], Plateau[yAxes][xAxes] = player1+20, 0
									dejaVu = True
									break
								if Plateau[yAxes+1][xAxes] == 25 : 				# Si case visée = mur vertical
									Plateau[yAxes+1][xAxes], Plateau[yAxes][xAxes] = player1+25, 0
									dejaVu = True
									break
								# Pour les escalators
								if Plateau[yAxes+1][xAxes] == 31 :		# Si case visée = escalator
									Plateau[yAxes+1][xAxes], Plateau[yAxes][xAxes] = player1, 0
									for i in range (len(Plateau)):
										for j in range (len(Plateau[0])):
											if Plateau[i][j]==30:
												Plateau[i][j], Plateau[yAxes+1][xAxes] = player1, 31
												dejaVu=True
												break
								if Plateau[yAxes+1][xAxes] == 30 :		# Si case visée = escalator
									Plateau[yAxes+1][xAxes], Plateau[yAxes][xAxes] = player1, 0
									for i in range (len(Plateau)):
										for j in range (len(Plateau[0])):
											if Plateau[i][j]==31:
												Plateau[i][j], Plateau[yAxes+1][xAxes] = player1, 30	
												dejaVu=True									
												break
								if Plateau[yAxes+1][xAxes] == 32 :		# Si case visée = escalator
									Plateau[yAxes+1][xAxes], Plateau[yAxes][xAxes] = player1, 0
									for i in range (len(Plateau)):
										for j in range (len(Plateau[0])):
											if Plateau[i][j]==33:
												Plateau[i][j], Plateau[yAxes+1][xAxes] = player1, 32
												dejaVu=True
												break
								if Plateau[yAxes+1][xAxes] == 33 :		# Si case visée = escalator
									Plateau[yAxes+1][xAxes], Plateau[yAxes][xAxes] = player1, 0
									for i in range (len(Plateau)):
										for j in range (len(Plateau[0])):
											if Plateau[i][j]==32:
												Plateau[i][j], Plateau[yAxes+1][xAxes] = player1, 33	
												dejaVu=True									
												break

	return debug

# ---------- Partie visuelle ---------- #

def affichage() :
	"""
		Actualise l'affichage en fonction de chaque élément dans la matrice.
		Si l'elem. de la matrice est 0 : c'est une case libre alors on affiche un simple rectangle.
		Si l'elem. de la matrice est 5, 6 : c'est la sortie alors on affiche l'image correspondante.
		Si l'elem. de la matrice est 7 : c'est une case vide alors on affiche un rectangle foncé
		Si l'elem. de la matrice est 1, 2, 3, 4 : c'est un pion alors on affiche l'image correspondante.
		Affiche les objets tant que la sortie n'est pas active.
	"""
	x, y = 0, 0
	if touche != None:
		for yAxes in range(nbCasesY):
			locY = yAxes*largeur-largeur/2+largeur
			for xAxes in range(nbCasesX):
				locX = xAxes*largeur-largeur/2+largeur
				## Affiche les cases libres ##
				rectangle(x, y, x+largeur, y+largeur, remplissage = 'light grey')
				# image(x+largeur//2, y+largeur//2, 'ground.gif', ancrage = 'center')
				x += largeur
				## Affiche les pions ##
				if Plateau[yAxes][xAxes] == 1 :
					image(locX, locY, 'Warrior_pion_transp.gif', ancrage = 'center', tag = 'warrior')
				if Plateau[yAxes][xAxes] == 2 : 
					image(locX, locY, 'Wizzard_pion_transp.gif', ancrage = 'center', tag = 'wizzard')
				if Plateau[yAxes][xAxes] == 3 : 
					image(locX, locY, 'Elf_pion_transp.gif', ancrage = 'center', tag = 'elf')
				if Plateau[yAxes][xAxes] == 4 : 
					image(locX, locY, 'Dwarf_pion_transp.gif', ancrage = 'center', tag = 'dwarf')
				## Affiche sortie on ou off ##
				if Plateau[yAxes][xAxes] == 5 : 
					image(locX+1, locY, 'Vortex_transp_off.gif', ancrage = 'center', tag = 'exitOff')
				if Plateau[yAxes][xAxes] == 6 : 

					image(locX+1, locY, 'Vortex_transp_on.gif', ancrage = 'center', tag = 'exitOn')
				## Affiche les cases vides ##
				if Plateau[yAxes][xAxes] == 7 :
					rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'grey', tag = 'caseVide')
				## Affiche les murs horizontaux ##
				if Plateau[yAxes-1][xAxes] == 20:
					rectangle(xAxes*largeur, yAxes*largeur-3, xAxes*largeur+largeur, yAxes*largeur+3, remplissage = 'black', tag = 'murHorizontal')
				## Affiche les murs verticaux ##
				if Plateau[yAxes][xAxes-1] == 25 :
					rectangle(xAxes*largeur-3, yAxes*largeur, xAxes*largeur+3, yAxes*largeur+largeur, remplissage = 'black', tag = 'murVertical')
				## Affiche mur + pion ##
					# Murs horizontaux + pion
				if Plateau[yAxes-1][xAxes] == 21 :
					rectangle(xAxes*largeur, yAxes*largeur -3, xAxes*largeur+largeur, yAxes*largeur+3, remplissage = 'black', tag = 'murHorizontal+War')
					image(locX, locY-largeur, 'Warrior_pion_transp.gif', ancrage = 'center', tag = 'warrior')
				if Plateau[yAxes-1][xAxes] == 22 :
					rectangle(xAxes*largeur, yAxes*largeur -3, xAxes*largeur+largeur, yAxes*largeur+3, remplissage = 'black', tag = 'murHorizontal+Wiz')
					image(locX, locY-largeur, 'Wizzard_pion_transp.gif', ancrage = 'center', tag = 'wizzard')
				if Plateau[yAxes-1][xAxes] == 23 :
					rectangle(xAxes*largeur, yAxes*largeur -3, xAxes*largeur+largeur, yAxes*largeur+3, remplissage = 'black', tag = 'murHorizontal+Elf')
					image(locX, locY-largeur, 'Elf_pion_transp.gif', ancrage = 'center', tag = 'elf')
				if Plateau[yAxes-1][xAxes] == 24 :
					rectangle(xAxes*largeur, yAxes*largeur -3, xAxes*largeur+largeur, yAxes*largeur+3, remplissage = 'black', tag = 'murHorizontal+Dwa')
					image(locX, locY-largeur, 'Dwarf_pion_transp.gif', ancrage = 'center', tag = 'dwarf')
					# Murs verticaux + pion
				if Plateau[yAxes][xAxes-1] == 26 :
					rectangle(xAxes*largeur-3, yAxes*largeur, xAxes*largeur+3, yAxes*largeur+largeur, remplissage = 'black', tag = 'murVertical+War')
					image(locX-largeur, locY, 'Warrior_pion_transp.gif', ancrage = 'center', tag = 'warrior')
				if Plateau[yAxes][xAxes-1] == 27 :
					rectangle(xAxes*largeur-3, yAxes*largeur, xAxes*largeur+3, yAxes*largeur+largeur, remplissage = 'black', tag = 'murVertical+Wiz')
					image(locX-largeur, locY, 'Wizzard_pion_transp.gif', ancrage = 'center', tag = 'wizzard')
				if Plateau[yAxes][xAxes-1] == 28 :
					rectangle(xAxes*largeur-3, yAxes*largeur, xAxes*largeur+3, yAxes*largeur+largeur, remplissage = 'black', tag = 'murVertical+Elf')
					image(locX-largeur, locY, 'Elf_pion_transp.gif', ancrage = 'center', tag = 'elf')
				if Plateau[yAxes][xAxes-1] == 29 :
					rectangle(xAxes*largeur-3, yAxes*largeur, xAxes*largeur+3, yAxes*largeur+largeur, remplissage = 'black', tag = 'murVertical+Dwa')
					image(locX-largeur, locY, 'Dwarf_pion_transp.gif', ancrage = 'center', tag = 'dwarf')
				if Plateau[yAxes][xAxes] == 30 :
					rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'red', tag = 'caseVide')
				if Plateau[yAxes][xAxes] == 35 :
					rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'green', tag = 'caseVide')
				if Plateau[yAxes][xAxes] == 36 :
					rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'green', tag = 'caseVide')
					image(locX, locY, 'Warrior_pion_transp.gif', ancrage = 'center', tag = 'warrior')
				## Affiche les sabliers ##
				if Plateau[yAxes][xAxes] == 8 :
					image(locX+1, locY, 'sablierReverse2.gif', ancrage = 'center', tag = 'sablierReverse')
				## Affiche les objets tant que la sortie n'est pas active ##
				if not sortieOn:
					if yAxes == posObjets[0][0] and xAxes == posObjets[0][1]:	
						image(locX, locY, 'Warrior_objet_transp.gif', ancrage = 'center', tag = 'warriorObj')	
					if yAxes == posObjets[1][0] and xAxes == posObjets[1][1]:
						image(locX, locY, 'Wizzard_objet_transp.gif', ancrage = 'center', tag = 'wizzardObj')
					if yAxes == posObjets[2][0] and xAxes == posObjets[2][1]:
						image(locX, locY, 'Elf_objet_transp.gif', ancrage = 'center', tag = 'elfObj')
					if yAxes == posObjets[3][0] and xAxes == posObjets[3][1]:
						image(locX, locY, 'Dwarf_objet_transp.gif', ancrage = 'center', tag = 'dwarfObj')
				## Affiche les escalators 
				if yAxes == escalator[0][0] and xAxes == escalator[0][1]:
					rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'green', tag = 'caseVide')
				if yAxes == escalator[1][0] and xAxes == escalator[1][1]:
					rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'green', tag = 'caseVide')
				if yAxes == escalator[2][0] and xAxes == escalator[2][1]:	
					rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'red', tag = 'caseVide')
				if yAxes == escalator[3][0] and xAxes == escalator[3][1]:
					rectangle(xAxes*largeur, yAxes*largeur, xAxes*largeur+largeur, yAxes*largeur+largeur, remplissage = 'red', tag = 'caseVide')
			x = 0
			y += largeur

def affichagePionDroite():
	"""
	Affiche les icônes de pions et leur objet sur le côté, ainsi qu'un rond indiquant quel pion est séléctionné.
	"""
	texte(nbCasesX*largeur +100, largeur, 'État des pions :',taille = 18, ancrage = 'center')
	#Affiche les icônes propres à chaque pion
	image(nbCasesX*largeur +37, largeur*2, 'Warrior_pion_transp.gif', ancrage = 'center')
	texte(nbCasesX*largeur +100, largeur*2, '→', taille = '30', ancrage = 'center')
	image(nbCasesX*largeur +135, largeur*2, 'Warrior_objet_transp.gif', ancrage = 'center')

	image(nbCasesX*largeur +37, largeur*3, 'Wizzard_pion_transp.gif', ancrage = 'center')
	texte(nbCasesX*largeur +100, largeur*3, '→', taille = '30', ancrage = 'center')
	image(nbCasesX*largeur +135, largeur*3, 'Wizzard_objet_transp.gif', ancrage = 'center')

	image(nbCasesX*largeur +37, largeur*4, 'Elf_pion_transp.gif', ancrage = 'center')
	texte(nbCasesX*largeur +100, largeur*4, '→', taille = '30', ancrage = 'center')
	image(nbCasesX*largeur +135, largeur*4, 'Elf_objet_transp.gif', ancrage = 'center')

	image(nbCasesX*largeur +37, largeur*5 -6, 'Dwarf_pion_transp.gif', ancrage = 'center')
	texte(nbCasesX*largeur +100, largeur*5, '→', taille = '30', ancrage = 'center')
	image(nbCasesX*largeur +135, largeur*5, 'Dwarf_objet_transp.gif', ancrage = 'center')

def pionSelected1(i):
	"""
	Affiche le rond de séléction J1
	"""
	cercle(nbCasesX*largeur +37, largeur*2 +(i-1)*largeur, 25, epaisseur = 2, couleur = 'red', tag = 'selecJ1')

def objetsLeft(sortie):
	"""
	Affiche sur le côté les objets restants à voler sur le côté.
	"""
	# Affiche les objets manquants tant que la sortie n'est pas active
	if not sortie:
		texte(nbCasesX*largeur +100, (nbCasesY*largeur)/2 + 0.8*largeur, 'Objectif actuel :',taille = 18, ancrage = 'center')
		image(nbCasesX*largeur +100, (nbCasesY*largeur)/2 + 2*largeur, 'Warrior_objet_transp.gif', ancrage = 'center', tag= 'WarriorObjetPrit')
		image(nbCasesX*largeur +100, (nbCasesY*largeur)/2 + 3*largeur, 'Wizzard_objet_transp.gif', ancrage = 'center', tag= 'WizzardObjetPrit')
		image(nbCasesX*largeur +100, (nbCasesY*largeur)/2 + 4*largeur, 'Elf_objet_transp.gif', ancrage = 'center', tag= 'ElfObjetPrit')
		image(nbCasesX*largeur +100, (nbCasesY*largeur)/2 + 5*largeur, 'Dwarf_objet_transp.gif', ancrage = 'center', tag= 'DwarfObjetPrit')
	if sortie:
		image(nbCasesX*largeur +37, (nbCasesY*largeur)/2 + 2*largeur +largeur/2, 'Vortex_transp_on.gif', ancrage = 'center', tag= 'SortieOn')
	# Efface l'objet sur le côté si le pion est dessus
	for yAxes in range(nbCasesY):
		for xAxes in range(nbCasesX):
			if Plateau[yAxes][xAxes] == 1:
				if yAxes == posObjets[0][0] and xAxes == posObjets[0][1]:
					efface('WarriorObjetPrit')
			if Plateau[yAxes][xAxes] == 2:
				if yAxes == posObjets[1][0] and xAxes == posObjets[1][1]:
					efface('WizzardObjetPrit')
			if Plateau[yAxes][xAxes] == 3:
				if yAxes == posObjets[2][0] and xAxes == posObjets[2][1]:
					efface('ElfObjetPrit')
			if Plateau[yAxes][xAxes] == 4:
				if yAxes == posObjets[3][0] and xAxes == posObjets[3][1]:
					efface('DwarfObjetPrit')

def legendeSelection():
	"""
	Affiche un cercle de couleur, suivi du joueur qui contrôle cette couleur ainsi que les commandes pour déplacer son pion
	"""
	## Cercle rouge pour J1 ##
	if nbrJoueurs == '1 joueur' or nbrJoueurs == '2 joueurs' or nbrJoueurs == '3 joueurs':
		cercle(nbCasesX*largeur +37, largeur*7, 15, couleur = 'red', epaisseur = '2')
		texte(nbCasesX*largeur +60, largeur*7, ': Joueur 1 (\'↑↓→←\')', taille = '12', ancrage = 'w')
	## Cercle rouge pour J3 ##
	if nbrJoueurs == '3 joueurs':
		cercle(nbCasesX*largeur +37, largeur*7.75, 15, couleur = 'blue', epaisseur = '2')
		texte(nbCasesX*largeur +60, largeur*7.75, ': Joueur 2 (\'zqsd\')', taille = '12', ancrage = 'w')

		cercle(nbCasesX*largeur +37, largeur*8.5, 15, couleur = 'green', epaisseur = '2')
		texte(nbCasesX*largeur +60, largeur*8.5, ': Joueur 3 (\'8456\')', taille = '12', ancrage = 'w')

def timer(seconde, startTime, etatReverse) :
	"""
	Affiche un timer décroissant en secondes, depuis le nombre rentré en paramètre.
	"""
	global minutes, secondes, secElapsed
	# secLeft = seconde - secElapsed				# Secondes restantes
	couleur = 'dark green'

	if etatReverse == False:
		secElapsed = int((time.time() - (startTime+a*2) )) 	# Secondes écoulées depuis le début du programme
		secLeft = seconde - secElapsed			# Secondes restantes

	if etatReverse == True:
		secLeft = a - secElapsed
		secElapsed = int((time.time() - (startTime+a) ))
	# print("Seconde écoulées: ", secElapsed)
	# print("Secondes objet prit: ", a)

	# Conversion du temps en minutes:secondes
	minutes = secLeft // 60
	secondes = secLeft - minutes*60

	if minutes < 0:		# Si le temps tombe à 0, partie perdue.
		perdu()
	if minutes == 0 and secondes < 30:			# Si - de 30sec restantes : couleur rouge
		couleur = 'red'

	# print(secLeft)
	# print(secElapsed)
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
	texte(largeur*6 +longueur_texte(minutes+secondes)+longueur_texte('min')-10, nbCasesY*largeur+12, "Commandes:", couleur='black', taille = 14, ancrage = 'w', tag = 'commandes')
	texte(largeur*6 +longueur_texte(minutes+secondes)+longueur_texte('min') +27.5, nbCasesY*largeur+30, "a : Changer de pion à déplacer", couleur='black', taille = 12, ancrage = 'w', tag = 'selectorInstructions')
	texte(largeur*6 +longueur_texte(minutes+secondes)+longueur_texte('min') +27.5, nbCasesY*largeur+50, "←↑→↓ : Déplacer le pion séléctionné", couleur='black', taille = 12, ancrage = 'w', tag = 'movePionInstructions')
	texte(largeur*6 +290 +longueur_texte(minutes+secondes)+longueur_texte('min') +27.5, nbCasesY*largeur+30, "F2 : Quitter le jeu", couleur='black', taille = 12, ancrage = 'w', tag = 'quitterInstructions')
	texte(largeur*6 +290 +longueur_texte(minutes+secondes)+longueur_texte('min') +27.5, nbCasesY*largeur+50, "F1 : Débug mode (on/off)", couleur='black', taille = 12, ancrage = 'w', tag = 'debugModeInstructions')

def affichageDroit():
	if touche != None :
		affichagePionDroite()
		pionSelected1(pionVisé1)
		# pionSelected2(pionVisé2)
		# pionSelected3(pionVisé3)
		legendeSelection()
		ligne(nbCasesX*largeur +7, (nbCasesY*largeur)/2, nbCasesX*largeur +193, (nbCasesY*largeur)/2, couleur='black', epaisseur=3)
		objetsLeft(sortieOn)

def affichageBas():
	efface('separationBas')
	timer(180, startTime, reverseTimer)
	ligne(largeur*5.3+longueur_texte(minutes+secondes)+longueur_texte('min'), nbCasesY*largeur+12, largeur*5.3+longueur_texte(minutes+secondes)+longueur_texte('min'), nbCasesY*largeur+65, couleur='black', epaisseur=3, tag = 'separationBas')
	instructions()

def perdu():
	"""
	Si tous les pions ne sont pas sortis avant la fin du temps impartit, on arrête la partie et on affiche les texte de fin.
	Partie perdue.
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
	Si tous les pions sont sortis, on arrête la partie et on affiche les texte de fin
	Partie gagnée.
	"""
	efface_tout()
	s = 60-sec
	while 1 :
		efface_tout()
		texte((nbCasesX//2+1)*largeur, (nbCasesY//2-1)*largeur, "Vous avez gagné!", couleur="dark green", ancrage = "center", taille = 45)
		texte((nbCasesX//2+1)*largeur, (nbCasesY//1.5)*largeur, "Félicitations, vous avez finit le jeu en " + str(min) + "min" + str(s), couleur="black", ancrage = "center", taille = 25)
		attente_clic()
		break	
	ferme_fenetre()

# ----------------------- Main Program --------------------------- #
if __name__ == '__main__':
	creationMap(18,18)
	a = 0

	## Menu ##
	affichageMenu()

	if nbrJoueurs == '1 joueur' or nbrJoueurs == '3 joueurs':
		## Initialisations variables ##
		startTime = time.time()
		sortieOn = False
		pionVisé1 = 1
		pionVisé2 = 2
		pionVisé3 = 3
		objetsOwn = 0
		pionsInSortie = 0
		debugMode = False
		reverseTimer = False
		
		## Création entités ##
		# creationPion()
		#creationObjet()
		# creationSablier(0)
		# creationSortie()
		# creationMur(10)
		# creationCaseVide(10)

		posObjets = [(1,1),(5,13),(15,5),(10,12)] 
		escalator = [(4,16),(2,14),(13,6),(14,7)]

		Plateau = [ [7,7,7,25,0,25,0,7,8,25,0,20,20,20,0,25,0,0],
					[7,11,0,25,20,25,0,7,7,25,25,0,0,25,0,25,8,0],
					[7,0,7,25,25,25,20,20,20,25,25,0,5,25,31,25,0,0],
					[20,20,0,20,20,20,20,0,0,25,25,20,0,25,20,7,7,7],
					[0,0,25,0,0,0,25,20,20,20,20,25,0,7,0,0,30,0],
					[7,25,25,0,8,25,0,0,0,0,0,25,25,12,0,20,20,20],
					[7,0,25,20,20,0,7,7,0,0,7,7,25,0,25,0,0,8],
					[7,25,25,0,20,0,7,0,0,0,0,7,20,20,0,20,20,20],
					[7,8,25,20,25,0,0,0,1,2,0,0,0,25,0,25,0,20],
					[7,25,25,0,25,0,0,0,3,4,0,0,25,20,20,25,20,0],
					[20,20,25,0,0,20,7,0,0,0,0,7,14,20,20,25,0,20],
					[0,0,0,25,0,20,7,7,0,0,7,7,20,25,0,25,20,0],
					[20,20,0,7,25,8,0,20,20,25,0,0,25,0,0,25,0,20],
					[0,25,0,25,25,0,32,20,20,20,7,0,20,20,20,0,0,0],
					[20,25,7,25,25,20,7,33,7,0,25,25,0,0,25,0,7,8],
					[0,20,25,25,20,13,25,0,0,20,8,25,20,20,25,0,7,20],
					[20,0,25,0,25,20,20,20,7,25,0,25,0,0,25,0,20,0],
					[0,25,0,25,0,0,0,0,0,0,0,25,25,0,0,0,25,0]]

		## Boucle principale ##
		while 1:
			affichageBas()
			affichageDroit()
			affichage()
			isWin(pionsInSortie, minutes, secondes)
			sortieOn = isSortieOn(sortieOn)
			debugMode = actionTouche(pionVisé1, pionVisé2, pionVisé3, objetsOwn, pionsInSortie, debugMode)
			mise_a_jour()
			if touche != None:
				efface_tout()


# GRISER L'IMAGE DU PION QUAND IL NE PEUT PLUS ETRE SELECTIONNER (quand il est sortit) #
