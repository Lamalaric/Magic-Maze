from upemtk import *

def affiche_actions(i, color):
    efface_tout()
    rectangle(i*100+20, 200+20, i*100+80, 200+80, color, color)
    for i in [0,1,2,3]:
        rectangle(i*100+25, 200+25, i*100+75, 200+75, "blue", "blue")


couleurChoisie = 1


if __name__ == '__main__':
    
    cree_fenetre(400,400)
    
    valide = False
    numero_action = 0
    actuel = 1
    
    affiche_actions(numero_action,"red")

    while(True):
        touche = attente_touche_jusqua(1000)
        print(touche)

        if touche == None:
            continue


        if touche == 'a':
            if not valide:
                numero_action = (numero_action + 1) % 4
                affiche_actions(numero_action, "red")
                actuel += 1
                if actuel < 4:
                    actuel = 1


        elif touche == 'v':
            if valide == True:
                couleurChoisie = actuel

            else:
                couleurChoisie = 4
            affiche_actions(numero_action, "red" if valide else "black")
            valide = not valide

            
        else:
            print("râté")
            ferme_fenetre()
            quit()