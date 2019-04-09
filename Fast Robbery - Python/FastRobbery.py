#-------------------------------------------------------------------------------
# Nom :  Fast Robbery
# Description :  Jeu de plateforme
# But :  Effectuer un cambriolage et s'enfuir
#
# Createurs :  GOUPY Gaspard et DEGHOUL Hassan
# Date de creation :  courant 2017
# Copyright:  (c) dagla 2017
# Licence :  None
#-------------------------------------------------------------------------------


from tkinter import*
from random import*
import time










#====================================================================================================================================================================================================================================================================================================================================================================#
#menu d'avant jeu










#creation de la fenetre d'avant jeu
def menu_jeu():


    global fenetre, canvas, img_menu, img_jouer, img_jouer2, id_jouer, id_jouer2, id_aide, id_aide2, img_quitter, img_quitter2, id_quitter, id_quitter2, id_textaide, img_textaide, img_touche, id_touche, id_textmute, img_textmute, img_mute, img_son, id_mute, id_son, son, choix, jeu


    #base de la fenetre
    fenetre = Tk()
    fenetre.title("Fast Robbery")

    #canevas principal
    canvas = Canvas(fenetre, height=840, width=1430, bg="white" )
    canvas.pack()

    #photo de fond
    img_menu = PhotoImage(file="menu.gif")
    canvas.create_image(0,0, anchor = NW,image=img_menu)

    #bouton jouer
    img_jouer = PhotoImage(file="jouer.gif")
    id_jouer = canvas.create_image(595,120, anchor = NW,image=img_jouer)

    #bouton jouer quand selection dessus
    img_jouer2 = PhotoImage(file="jouer2.gif")
    id_jouer2 = canvas.create_image(584,128, anchor = NW,image=img_jouer2)
    canvas.tag_lower(id_jouer2,ALL)

    #bouton aide
    img_aide = PhotoImage(file="aide.gif")
    id_aide = canvas.create_image(625,300, anchor = NW,image=img_aide)

    #bouton aide quand selection dessus
    img_aide2 = PhotoImage(file="aide2.gif")
    id_aide2 = canvas.create_image(616,309, anchor = NW,image=img_aide2)
    canvas.tag_lower(id_aide2,ALL)

    #bouton quitter
    img_quitter = PhotoImage(file="quitter.gif")
    id_quitter = canvas.create_image(555,480, anchor = NW,image=img_quitter)

    #bouton quitter quand selection dessus
    img_quitter2 = PhotoImage(file="quitter2.gif")
    id_quitter2 = canvas.create_image(550,485, anchor = NW,image=img_quitter2)
    canvas.tag_lower(id_quitter2,ALL)

    #texte du menu d'aide
    img_textaide = PhotoImage(file='textaide.gif')
    id_textaide = canvas.create_image(230, 150, anchor = NW, image = img_textaide)
    canvas.tag_lower(id_textaide, ALL)

    #img touche directionnelles dans le menu d'aide
    img_touche = PhotoImage(file='touche.gif')
    id_touche = canvas.create_image(1100, 545, anchor = NW, image = img_touche)
    canvas.tag_lower(id_touche, ALL)


    #texte pour mute et demute le son
    img_textmute = PhotoImage(file='textmute.gif')
    id_textmute = canvas.create_image(75, 750, anchor = NW, image = img_textmute)

    #logo mute et demute
    img_son = PhotoImage(file='son.gif')
    id_son = canvas.create_image(380,735, anchor = NW, image = img_son)
    img_mute = PhotoImage(file='mute.gif')
    id_mute = canvas.create_image(382,741, anchor = NW, image = img_mute)
    canvas.tag_lower(id_mute, ALL)

    #variable pour savoir si le son est on/off, de base 'on'
    son = 1
    #variable pour connaitre le jeu, et savoir quel son lancer
    jeu = 1

    #musique de fond
    if son == 1 :
        son = 0;


    #initialisation des touches clavier pour choisir les boutons de la fenetre
    canvas.bind_all("<Up>",clavier)
    canvas.bind_all("<Down>",clavier)
    canvas.bind_all("<Return>",clavier) #touche entrer
    canvas.bind_all("<space>",clavier) #touche espace


    #initialisationvariable concernant le choix du bouton
    choix = 0


    #Tkinter supporte un mecanisme appele : 'protocol handlers'
    #WM_DELETE_WINDOW definit ce qui doit se passer quand une fenetre se ferme
    #si l'on appuie sur la 'croix', l'action fermer _fenetre est appele
    fenetre.protocol("WM_DELETE_WINDOW", fermer_fenetre)


    fenetre.mainloop()





def clavier(event):


    global choix, touche, son, jeu


    #Detection des touches clavier
    touche = event.keysym


    #si la touche directionnnelle 'bas' et active
    if touche == 'Down':

        #si le bouton selectionne est inferieur a 3 en partant du haut : on descends
        if choix < 3:
            choix+=1

        #sinon on monte au premier
        else:
            choix=1


    #si la touche directionnnelle 'haut' et active
    if touche == 'Up':

        #si le bouton selectionne est superieur a 1 en partant du haut : on monte
        if choix > 1:
            choix-=1

        #sinon on descend au dernier
        else:
            choix=3


    #on lance l'actualisation des boutons
    animation()


    #si l'on appuie sur la touche 'entrer'
    #on lance la fonction correspondant au bouton(image) choisis

    if touche == 'Return':

        if choix == 1 :
            choix_perso()

        if choix == 2 :
            menu_aide()

        if choix == 3 :
            #[faibles possibilites de winsound] == on joue un son 'partiel' pour stopper la musique
            fenetre.destroy()


    #si l'on appuis sur espace, le son se mute ou se demute
    if touche == 'space' :

        #si le son est on
        if son == 1 :
            #[faibles possibilites de winsound] == on joue un son 'partiel' pour stopper la musique
            canvas.tag_lower(id_son,ALL)
            canvas.tag_raise(id_mute,ALL)
            son = 0

        #si le son est off
        else :
            canvas.tag_lower(id_mute,ALL)
            canvas.tag_raise(id_son,ALL)
            son = 0






#menu d'aide du jeu
def menu_aide():


    #on place les boutons derriere l'image de fond et le texte devant
    canvas.tag_lower(id_jouer,ALL)
    canvas.tag_lower(id_jouer2,ALL)
    canvas.tag_lower(id_quitter,ALL)
    canvas.tag_lower(id_quitter2,ALL)
    canvas.tag_lower(id_aide,ALL)
    canvas.tag_lower(id_aide2,ALL)
    canvas.tag_raise(id_textaide,ALL)
    canvas.tag_raise(id_touche,ALL)





#actualisation des bouton en fonction du choix
def animation():


    if choix == 1 :
        canvas.tag_lower(id_textaide,ALL)
        canvas.tag_lower(id_touche,ALL)
        canvas.tag_lower(id_jouer,ALL)
        canvas.tag_raise(id_jouer2,ALL)
        canvas.tag_lower(id_aide2,ALL)
        canvas.tag_raise(id_aide,ALL)
        canvas.tag_lower(id_quitter2,ALL)
        canvas.tag_raise(id_quitter,ALL)

    if choix == 2:
        canvas.tag_lower(id_touche,ALL)
        canvas.tag_lower(id_textaide,ALL)
        canvas.tag_lower(id_jouer2,ALL)
        canvas.tag_raise(id_jouer,ALL)
        canvas.tag_lower(id_aide,ALL)
        canvas.tag_raise(id_aide2,ALL)
        canvas.tag_lower(id_quitter2,ALL)
        canvas.tag_raise(id_quitter,ALL)

    if choix == 3 :
        canvas.tag_lower(id_touche,ALL)
        canvas.tag_lower(id_textaide,ALL)
        canvas.tag_lower(id_aide2,ALL)
        canvas.tag_raise(id_aide,ALL)
        canvas.tag_lower(id_quitter,ALL)
        canvas.tag_raise(id_quitter2,ALL)
        canvas.tag_raise(id_jouer,ALL)
        canvas.tag_lower(id_jouer2,ALL)





#########################################################################
#########################################################################
#fenetre de choix de personnage





def choix_perso() :


    global img_menu, voleur, choix


    #on supprime tout / plus simple et rends la fenetre moins lourde
    canvas.delete(ALL)


    #photo de fond
    img_menu = PhotoImage(file="menu.gif")
    canvas.create_image(0,0, anchor = NW,image=img_menu)


    #initialisation des touches clavier pour choisir le bouton
    canvas.bind_all("<Right>",clavier2)
    canvas.bind_all("<Left>",clavier2)
    canvas.bind_all("<Return>",clavier2) #touche entrer


    #variable concernant le choix du bouton ( on la remet a 0 )
    choix = 0


    #variable concernant le choix du voleur
    voleur = 0


    #on fait apparaitre les canevas de choix de psg apres 0.4s
    fenetre.after(400,menu_perso)





def menu_perso():


    global img_carrechoix, id_flecheD, id_flecheD2, img_flecheD, img_flecheD2, img_flecheG, img_flecheG2, id_flecheG, id_flecheG2, img_voleurmvtDroite, id_voleurD, id_voleurgrandD, id_voleurpetitD, img_voleurgrandD, img_voleurpetitD
    global img_textvoleur, id_textvoleur, img_textpetitvoleur, id_textpetitvoleur, img_textgrandvoleur, id_textgrandvoleur, img_debutant, img_intermediaire, img_expert, id_debutant, id_expert, id_intermediaire


    #carre blanc ou seront places les personnages et leurs descriptions
    img_carrechoix = PhotoImage(file='carrechoix.gif')
    canvas.create_image(515,255, anchor = NW, image = img_carrechoix)


    #fleches pour choisir le personnages
    img_flecheD = PhotoImage(file='flecheD.gif')
    id_flecheD = canvas.create_image(1037,330,anchor = NW, image = img_flecheD)

    img_flecheD2 = PhotoImage(file='flecheD2.gif')
    id_flecheD2 = canvas.create_image(1037,330,anchor = NW, image = img_flecheD2)
    canvas.tag_lower(id_flecheD2,ALL)

    img_flecheG = PhotoImage(file='flecheG.gif')
    id_flecheG = canvas.create_image(290,330,anchor = NW, image = img_flecheG)

    img_flecheG2 = PhotoImage(file='flecheG2.gif')
    id_flecheG2 = canvas.create_image(290,330,anchor = NW, image = img_flecheG2)
    canvas.tag_lower(id_flecheG2,ALL)


    #voleurs disponibles
    img_voleurmvtDroite = PhotoImage(file="voleurmvtD.gif")
    id_voleurD = canvas.create_image(705, 350, anchor = NW,image=img_voleurmvtDroite)

    img_voleurgrandD = PhotoImage(file="voleurgrandD.gif")
    id_voleurgrandD = canvas.create_image(700, 348, anchor = NW,image=img_voleurgrandD)
    canvas.tag_lower(id_voleurgrandD,ALL)

    img_voleurpetitD = PhotoImage(file="voleurpetitD.gif")
    id_voleurpetitD = canvas.create_image(705, 350, anchor = NW,image=img_voleurpetitD)
    canvas.tag_lower(id_voleurpetitD,ALL)


    #descriptions des voleurs
    img_textvoleur = PhotoImage(file="textvoleur.gif")
    id_textvoleur = canvas.create_image(570, 415, anchor = NW,image=img_textvoleur)

    img_textpetitvoleur = PhotoImage(file="textpetitvoleur.gif")
    id_textpetitvoleur = canvas.create_image(570, 415, anchor = NW,image=img_textpetitvoleur)
    canvas.tag_lower(id_textpetitvoleur,ALL)

    img_textgrandvoleur = PhotoImage(file="textgrandvoleur.gif")
    id_textgrandvoleur = canvas.create_image(570, 415, anchor = NW,image=img_textgrandvoleur)
    canvas.tag_lower(id_textgrandvoleur,ALL)

    img_debutant = PhotoImage(file='debutant.gif')
    id_debutant = canvas.create_image(670,274, anchor = NW, image = img_debutant)
    canvas.tag_lower(id_debutant,ALL)

    img_intermediaire = PhotoImage(file='intermediaire.gif')
    id_intermediaire = canvas.create_image(650,275, anchor = NW, image = img_intermediaire)

    img_expert = PhotoImage(file='expert.gif')
    id_expert = canvas.create_image(685,279, anchor = NW, image = img_expert)
    canvas.tag_lower(id_expert,ALL)





def clavier2(event):


    global choix, touche


    #Detection des touches clavier
    touche = event.keysym


    #si la touche directionnnelle bas et active
    if touche == 'Right':

        choix += 1

        if choix > 1 :
            choix = 1


    #si la touche directionnnelle bas et active
    if touche == 'Left':

        choix -= 1

        if choix<-1 :
            choix =-1


    animation2()





#actualisation des boutons en fonction du choix
def animation2():


    global voleur

    #si on choisis Rob
    if choix == 0:
        canvas.tag_lower(id_voleurpetitD,ALL)
        canvas.tag_lower(id_voleurgrandD,ALL)
        canvas.tag_raise(id_voleurD,ALL)
        canvas.tag_lower(id_textpetitvoleur,ALL)
        canvas.tag_raise(id_textvoleur,ALL)
        canvas.tag_lower(id_textgrandvoleur,ALL)
        canvas.tag_lower(id_debutant,ALL)
        canvas.tag_lower(id_expert,ALL)
        canvas.tag_raise(id_intermediaire,ALL)

        #(pour la premiere detection de touche vu que initialement voleur = 0 / la permiere pression nous fait rentrer dans le menu)
        if touche =='Right':
            canvas.tag_lower(id_flecheD,ALL)
            canvas.tag_raise(id_flecheD2,ALL)
            canvas.tag_lower(id_flecheG2,ALL)
            canvas.tag_raise(id_flecheG,ALL)
        if touche =='Left':
            canvas.tag_lower(id_flecheD2,ALL)
            canvas.tag_raise(id_flecheD,ALL)
            canvas.tag_lower(id_flecheG,ALL)
            canvas.tag_raise(id_flecheG2,ALL)

        #si l'on appuie sur entrer
        if touche =='Return':
            voleur = 1
            initial_jeu1()



    #si on choisis Tally Rob
    if choix == 1 :
        canvas.tag_lower(id_flecheD,ALL)
        canvas.tag_raise(id_flecheD2,ALL)
        canvas.tag_lower(id_flecheG2,ALL)
        canvas.tag_raise(id_flecheG,ALL)
        canvas.tag_lower(id_voleurD,ALL)
        canvas.tag_lower(id_voleurpetitD,ALL)
        canvas.tag_raise(id_voleurgrandD,ALL)
        canvas.tag_lower(id_textvoleur,ALL)
        canvas.tag_lower(id_textpetitvoleur,ALL)
        canvas.tag_raise(id_textgrandvoleur,ALL)
        canvas.tag_lower(id_intermediaire,ALL)
        canvas.tag_lower(id_debutant,ALL)
        canvas.tag_raise(id_expert,ALL)

        #si l'on appuie sur entree
        if touche =='Return':
            voleur = 3
            initial_jeu1()



    #si on choisis Tiny Rob
    if choix == -1:
        canvas.tag_lower(id_flecheD2,ALL)
        canvas.tag_raise(id_flecheD,ALL)
        canvas.tag_lower(id_flecheG,ALL)
        canvas.tag_raise(id_flecheG2,ALL)
        canvas.tag_lower(id_voleurD,ALL)
        canvas.tag_lower(id_voleurgrandD,ALL)
        canvas.tag_raise(id_voleurpetitD,ALL)
        canvas.tag_lower(id_textvoleur,ALL)
        canvas.tag_raise(id_textpetitvoleur,ALL)
        canvas.tag_lower(id_textgrandvoleur,ALL)
        canvas.tag_lower(id_intermediaire,ALL)
        canvas.tag_lower(id_expert,ALL)
        canvas.tag_raise(id_debutant,ALL)

        if touche =='Return':
            voleur = 2
            initial_jeu1()















#====================================================================================================================================================================================================================================================================================================================#
#debut du jeu










def initial_jeu1():


    global img_photofond, bouton_enter, but1


    #n supprime le menu d'avant jeu
    canvas.delete(ALL)


    #photo de fond
    img_photofond = PhotoImage(file="photo.gif")
    canvas.create_image(0,0, anchor = NW,image=img_photofond)

    #bouton enter
    bouton_enter = PhotoImage(file="bouton.gif")
    canvas.create_image(30,320, anchor = NW,image=bouton_enter)

    #but 1
    but1 = PhotoImage(file="but1.gif")
    canvas.create_image(330,730, anchor = NW,image=but1)


    #bouton de lancement ( initialise par un evenement ) ( voir fin programme )
    canvas.bind_all("<Return>", lancer_jeu1)


    #on initialise l'evenement sprinter ( pour le voleur ) actif seulement si on laisse appuyez sur shift
    #!!!ces evenements valent pour tous les mini jeux!!!#
    #[voir fin de programme]
    canvas.bind_all("<Key-Shift_L>", sprinter)
    canvas.bind_all("<KeyRelease-Shift_L>", marcher)





def initial_labyrinthe1():


    global img_porte, img_mur, id_porte, X,Y, id_easteregg, img_easteregg
    global img_piece1, img_piece2, img_piece3, id_piece1, id_piece2, id_piece3, totalPiece, sx, sy


    #on efface le contenu de la premiere fenetre
    canvas.delete(ALL)


    #evenements gere par le clavier ( voir fin de programme )
    canvas.bind_all("<Left>", deplacement_gauche)
    canvas.bind_all("<Right>", deplacement_droite)
    canvas.bind_all("<Up>", deplacement_haut)
    canvas.bind_all("<Down>", deplacement_bas)

    #on initialise une commande partielle pour eviter de relancer en appuyant sur entrer en jeu
    canvas.bind_all("<Return>", stop_choix)

    #initialisation des donnees :
    #deplacement selon x
    sx=1
    #deplacement selon y
    sy=0



    #photo de fond
    img_mur = PhotoImage(file ='mur.gif')
    canvas.create_image(0,0, anchor = NW, image = img_mur)


    canvas.focus_set()
    canvas.pack(padx =5, pady =5)

    #creation du labyrinthe
    canvas.create_line(1430,5,0,5,width=10, fill = 'white')
    canvas.create_line(0,100,1330,100,width=10, fill = 'white')
    canvas.create_line(1330,100,1330,200,width=10, fill = 'white')
    canvas.create_line(1430,0,1430,300,width=10, fill = 'white')
    canvas.create_line(1000,300,1430,300,width=10, fill = 'white')
    canvas.create_line(1000,300,1430,300,width=10, fill = 'white')
    canvas.create_line(1100,200,1330,200,width=10, fill = 'white')
    canvas.create_line(1100,100,1100,200,width=10, fill = 'white')
    canvas.create_line(1000,200,1000,300,width=10, fill = 'white')
    canvas.create_line(1000,200,300,200,width=10, fill = 'white')
    canvas.create_line(200,100,200,400,width=10, fill = 'white')
    canvas.create_line(900,300,300,300,width=10, fill = 'white')
    canvas.create_line(800,400,200,400,width=10, fill = 'white')
    canvas.create_line(800,600,800,400,width=10, fill = 'white')
    canvas.create_line(900,500,900,300,width=10, fill = 'white')
    canvas.create_line(900,500,1000,500,width=10, fill = 'white')
    canvas.create_line(800,600,1100,600,width=10, fill = 'white')
    canvas.create_line(1100,600,1100,400,width=10, fill = 'white')
    canvas.create_line(1000,500,1000,300,width=10, fill = 'white')
    canvas.create_line(1100,400,1200,400,width=10, fill = 'white')
    canvas.create_line(1200,400,1200,700,width=10, fill = 'white')
    canvas.create_line(1320,400,1320,800,width=10, fill = 'white')
    canvas.create_line(1430,300,1430,840,width=10, fill = 'white')
    canvas.create_line(700,800,1320,800,width=10, fill = 'white')
    canvas.create_line(700,800,700,840,width=10, fill = 'white')
    canvas.create_line(800,700,1200,700,width=10, fill = 'white')
    canvas.create_line(800,500,800,700,width=10, fill = 'white')
    canvas.create_line(700,400,700,700,width=10, fill = 'white')
    canvas.create_line(1430,840,0,840,width=10, fill = 'white')
    canvas.create_line(600,400,600,550,width=10, fill = 'white')
    canvas.create_line(600,650,600,800,width=10, fill = 'white')
    canvas.create_line(500,400,500,650,width=10, fill = 'white')
    canvas.create_line(500,750,500,860,width=10, fill = 'white')
    canvas.create_line(400,400,400,450,width=10, fill = 'white')
    canvas.create_line(400,550,400,840,width=10, fill = 'white')
    canvas.create_line(300,400,300,450,width=10, fill = 'white')
    canvas.create_line(300,550,300,860,width=10, fill = 'white')
    canvas.create_line(200,400,200,750,width=10, fill = 'white')
    canvas.create_line(200,850,200,860,width=10, fill = 'white')
    canvas.create_line(0,200,100,200,width=10, fill = 'white')
    canvas.create_line(100,300,200,300,width=10, fill = 'white')
    canvas.create_line(0,400,100,400,width=10, fill = 'white')
    canvas.create_line(0,600,100,600,width=10, fill = 'white')
    canvas.create_line(0,800,100,800,width=10, fill = 'white')
    canvas.create_line(100,500,200,500,width=10, fill = 'white')
    canvas.create_line(100,700,200,700,width=10, fill = 'white')
    canvas.create_line(4,0,4,860,width=10, fill = 'white')


    #initialisation de l'image porte de sortie
    img_porte = PhotoImage(file="porteferme.gif")
    id_porte = canvas.create_image(18,120, anchor = NW,image=img_porte)


    #initialisation des pieces a recuperer
    img_piece1 = PhotoImage(file="piece1.gif")
    id_piece1 = canvas.create_image(925,420, anchor = NW,image=img_piece1)

    img_piece2 = PhotoImage(file="piece2.gif")
    id_piece2 = canvas.create_image(1350,770, anchor = NW,image=img_piece2)

    img_piece3 = PhotoImage(file="piece3.gif")
    id_piece3 = canvas.create_image(325,770, anchor = NW,image=img_piece3)


    #initialisation du carre qui, si touche par le voleur, debloquera un nouveau psg ( easter egg )
    img_easteregg = PhotoImage(file='easteregg.gif')
    id_easteregg = canvas.create_image(720,810, anchor = NW, image = img_easteregg)
    canvas.tag_lower(id_easteregg, ALL)


    #coordonnees initial du voleur (place ici pour reutilise la fonction pour les autres mini jeux)
    X=50
    Y=50


    #variable qui permettera de sortir quand le voleur aura recuperer les 3 pieces (place ici afin de ne pas revenir a 0 a chaque appel de foncion )
    totalPiece = 0


    #on initialise le voleur
    initial_voleur1()


    #puis on le fait deplacer apres 0.7s
    fenetre.after(700,deplacer_voleur1)





#INITIALISATION GLOBALE DU VOLEUR
#VALABLE POUR TOUS LES JEUX
def initial_voleur1():


    global img_voleurpetitG,id_voleurpetitG,img_voleurgrandG,id_voleurgrandG, img_voleurD,img_voleurG, id_voleurD,id_voleurG,id_voleurgrandD,id_voleurpetitD,img_voleurgrandD,img_voleurpetitD,img_voleurmvtDroite,img_voleurmvtGauche
    global img_fatrobD, img_fatrobG, id_fatrobG, id_fatrobD, sprint, dep, pas


    #voleur de base ( on charge l'image )
    img_voleurmvtDroite = PhotoImage(file="voleurmvtD.gif")
    img_voleurmvtGauche = PhotoImage(file="voleurmvtG.gif")
    img_voleurD = canvas.create_image(X, Y, anchor = NW,image=img_voleurmvtDroite)
    img_voleurG = canvas.create_image(X, Y, anchor = NW,image=img_voleurmvtGauche)

    #on supprime le voleur de base pour charger le nouveau
    canvas.delete(img_voleurG)
    canvas.delete(img_voleurD)



    #assignation du voleur en fonction du choix du menu d'avant jeu
    if voleur == 1 :

        #voleur 1  [[conseille pour les test]]
        img_voleurmvtDroite = PhotoImage(file="voleurmvtD.gif")
        img_voleurmvtGauche = PhotoImage(file="voleurmvtG.gif")
        id_voleurD = canvas.create_image(X, Y, anchor = NW,image=img_voleurmvtDroite)
        id_voleurG = canvas.create_image(X, Y, anchor = NW,image=img_voleurmvtGauche)

        #on attribue l'id du canevas du voleur a ceux du voleur 1
        img_voleurD = id_voleurD
        img_voleurG = id_voleurG

        #changement des donnees ( a changer avec le pc qui lance le programme )
        #longueur du pas
        #longueur du pas lorsque le voleur court (sprint)
        pas = 5
        sprint = 8



    if voleur == 2 :

        #voleur 2
        img_voleurpetitD = PhotoImage(file="voleurpetitD.gif")
        id_voleurpetitD = canvas.create_image(X, Y, anchor = NW,image=img_voleurpetitD)
        img_voleurpetitG = PhotoImage (file='voleurpetitG.gif')
        id_voleurpetitG = canvas.create_image(X, Y, anchor = NW,image=img_voleurpetitG)

        #on attribue l'id du canevas du voleur a ceux du voleur 1
        img_voleurD = id_voleurpetitD
        img_voleurG = id_voleurpetitG

        #changement des donnees ( a changer avec le pc qui lance le programme )
        #longueur du pas
        #longueur du pas lorsque le voleur court (sprint)
        pas = 4
        sprint = 5



    if voleur == 3 :

        #voleur 3
        img_voleurgrandD = PhotoImage(file="voleurgrandD.gif")
        id_voleurgrandD = canvas.create_image(X, Y, anchor = NW,image=img_voleurgrandD)
        img_voleurgrandG = PhotoImage (file='voleurgrandG.gif')
        id_voleurgrandG = canvas.create_image(X, Y, anchor = NW,image=img_voleurgrandG)

        #on attribue l'id du canevas du voleur a ceux du voleur 1
        img_voleurD = id_voleurgrandD
        img_voleurG = id_voleurgrandG

        #changement des donnees ( a changer avec le pc qui lance le programme )
        #longueur du pas
        #longueur du pas lorsque le voleur court (sprint)
        pas = 7
        sprint = 12



    if voleur == 4 :

        #on initialise fat rob ( voleur pouvant etre debloque en trouvant un succes
        img_fatrobD = PhotoImage(file="fatrobD.gif")
        img_fatrobG = PhotoImage(file="fatrobG.gif")
        id_fatrobD = canvas.create_image(X, Y, anchor = NW,image=img_fatrobD)
        id_fatrobG = canvas.create_image(X, Y, anchor = NW,image=img_fatrobG)

        #on attribue l'id du canevas du voleur a ceux du voleur 1
        img_voleurD = id_fatrobD
        img_voleurG = id_fatrobG

        #changement des donnees ( a changer avec le pc qui lance le programme )
        #longueur du pas
        #longueur du pas lorsque le voleur court (sprint)
        pas = 8
        #la specialite de fat rob est qu'il peut aller tres doucement au lieu de sprinter
        sprint = 3



    #au lancement du jeu, le voleur marche
    #pas = deplacement quand le voleur marche
    #sprint = deplacement quand le voleur court
    #dep = variable qui varie entre le pas et le sprint
    dep = pas


    canvas.tag_lower(img_voleurG,ALL)
    canvas.tag_raise(img_voleurD,ALL)





def deplacer_voleur1():


    global totalPiece, img_porteouverte, id_porteouverte, pas, sprint, dep


    #initialisation des collisions
    collision = canvas.find_overlapping(*canvas.bbox(img_voleurD))


    #collision avec les pieces = action de les recuperer
    if id_piece1 in collision :
        #on supprime la piece
        canvas.delete(id_piece1)
        #on actualise la variable qui nous laissera sortir
        totalPiece += 1


    #collision avec les pieces = action de les recuperer
    if id_piece2 in collision :
        #on supprime la piece
        canvas.delete(id_piece2)
        #on actualise la variable qui nous laissera sortir
        totalPiece += 1


    #collision avec les pieces = action de les recuperer
    if id_piece3 in collision :
        #on supprime la piece
        canvas.delete(id_piece3)
        #on actualise la variable qui nous laissera sortir
        totalPiece += 1

        if totalPiece == 3 :
            #initialisation de l'image porte de sortie ouverte
            img_porteouverte = PhotoImage(file="porteouverte.gif")
            id_porteouverte = canvas.create_image(18,120, anchor = NW,image=img_porteouverte)
            canvas.tag_lower(id_porte, ALL)
            canvas.tag_raise(id_porteouverte, ALL)


    #si la collision est en rapport avec le canevas contenant la porte
    if id_porte in collision :

        #on peut sortir seulement si on a pris toutes les pieces
        if totalPiece == 3 :
            victoire_etape1()

        #sinon on relance la fonction
        else :
            # on continue le jeu
            canvas.move(img_voleurD, sx * dep, sy * dep)
            canvas.move(img_voleurG, sx * dep, sy * dep)
            canvas.update()
            # on actualise (en millisecondes)
            fenetre.after(20, deplacer_voleur1)


    #si le voleur touche le carre 'easteregg'
    elif id_easteregg in collision :
        debloquer_fatrob()


    #si rien de ces elements sont actif
    else :

        if len(collision)>3 and not id_piece1 in collision and not id_piece2 in collision and not id_piece3 in collision and not id_porte in collision and not id_easteregg in collision :
            #voir fin programme
            toucher_mur()
            #son de defaite
            #si le son du jeu est on
            if son == 1 :
                winsound.PlaySound ('wasted.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

        else :
            # on continue le jeu
            canvas.move(img_voleurD, sx * dep, sy * dep)
            canvas.move(img_voleurG, sx * dep, sy * dep)
            canvas.update()
            #on actualise (en millisecondes)
            fenetre.after(20, deplacer_voleur1)





#easter egg qui debloque un nouveau psg : fat rob
def debloquer_fatrob():


    global img_menu, voleur


    canvas.delete(ALL)

    #on affiche la transition pour dire que l'on a debloquer Fat Rob
    #photo de fond
    img_menu = PhotoImage(file="menu.gif")
    canvas.create_image(0,0, anchor = NW,image=img_menu)
    canvas.create_text(710,200,text="BRAVO ! TU AS TROUVE UN EASTER EGG !", fill="firebrick", font="sans 50 bold")
    canvas.create_text(710,350,text="TU AS DEBLOQUE FAT ROB", fill="firebrick", font="sans 47 bold")

    #on actualise la variable voleur
    voleur = 4


    fenetre.after(3000,initial_labyrinthe1)















#========================================================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================================================#
#Debut du mini jeu 2










#mise en place de l'avant jeu 2
def initial_jeu2 ():


    global img_photofond, bouton_enter, but2


    #on efface le contenu de l ancienne fenetre
    canvas.delete(ALL)


    #photo de fond
    img_photofond = PhotoImage(file="photo.gif")
    canvas.create_image(0,0, anchor = NW,image=img_photofond)

    #bouton enter
    bouton_enter = PhotoImage(file="bouton.gif")
    canvas.create_image(30,320, anchor = NW,image=bouton_enter)

    #but 2
    but2 = PhotoImage(file="but2.gif")
    canvas.create_image(550,730, anchor = NW,image=but2)


    #bouton de lancement ( initialise par un evenement ) ( voir fin programme )
    canvas.bind_all("<Return>", lancer_jeu2)





#creation du labyrinthe
def tracer_labyrinthe2():


    global canvas_carre_depart, murA, murB, img_mur, id_securiteD, img_securiteD, id_securiteG, img_securiteG, sx, sy


    #rappel des donnees ( afin de reinitialiser le deplacement initial )
    #deplacement selon x
    sx=1
    #deplacement selon y
    sy=0


    #on initialise une commande partielle pour eviter de relancer en appuyant sur entrer en jeu
    canvas.bind_all("<Return>", stop_choix)


    #effacement de la fenetre d'avant jeu
    canvas.delete(ALL)

    #photo de fond
    img_mur = PhotoImage(file ='mur.gif')
    canvas.create_image(0,0, anchor = NW, image = img_mur)

    #case depart
    canvas_carre_depart = canvas.create_rectangle(250,375,300,425, fill="white", outline ='white', width=10)

    #creation mur
    murA = canvas.create_line(250,375,320,375,320,275,600,275,600,50,900,50,900,275,1200,275,1200,525,  fill="white", width=10)
    murB = canvas.create_line(250,425,320,425,320,525,600,525,600,750,900,750,900,525,1200,525, fill="white", width=10)


    #creation du garde de securite qui va patrouiller
    img_securiteD = PhotoImage(file ='securiteD.gif')
    id_securiteD = canvas.create_image(550,310, anchor = NW, image = img_securiteD)
    img_securiteG = PhotoImage(file ='securiteG.gif')
    id_securiteG = canvas.create_image(550,310, anchor = NW, image = img_securiteG)
    canvas.tag_lower(id_securiteD,ALL)

    #lancement de l'initialisation du voleur
    initial_porte_sortie()





#on initialise les dif portes de sorties avec les suite differentes
def initial_porte_sortie():


    global id_porte1,id_porte2,id_porte3,img_porte1,img_porte2,img_porte3


    #photo des portes
    img_porte1 = PhotoImage(file="porte1.gif")
    img_porte2 = PhotoImage(file="porte2.gif")
    img_porte3 = PhotoImage(file="porte3.gif")

    #id des canevas contenant les portes
    id_porte1 = canvas.create_image(730, 100, anchor = NW,image=img_porte1)
    id_porte2 = canvas.create_image(730, 640, anchor = NW,image=img_porte2)
    id_porte3 = canvas.create_image(1100, 375, anchor = NW,image=img_porte3)


    initial_voleur2()


    #puis on le fait deplacer apres 0.7s
    fenetre.after(700,deplacer_voleur2)





#initialisation du voleur
def initial_voleur2():


    global X, Y


    #coords du voleur dans le nouveau labyrinthe
    X =350
    Y =380


    #on se reference a la premiere initialisation
    initial_voleur1()





#deplacement du voleur
def deplacer_voleur2():


    #on initialise les collisions
    #Peu importe l id que l on choisit du voleur, sachant que les deux images sont supperpose
    collision = canvas.find_overlapping(*canvas.bbox(img_voleurD))


    #liste de nombre
    liste = [1,2,3,4]

    #On choisis un nombre au hasard
    #suivant la valeur du nombre entre 1 et 4, les portes ont une issues differentes.
    #A represente un ensemble d'issue aleatoire
    A=choice(liste)


    #si il y a plus de 3 supperpositions de canvas
    #[[[  voir fin programme pour les fonctions conditionnelles  ]]]
    if len(collision) > 3 :



        if A == 1 :

            #collision avec la bonne porte de sortie
            if id_porte1 in collision :
                enfuir()

            #collision avec la porte declenchant l alarme
            if id_porte2 in collision :
                preambule()

            #collision avec la porte declenchant l alarme
            if id_porte3 in collision :
                preambule()

            #collision avec les murs
            if murA in collision:
                #son de defaite
                #si le son du jeu est on
                if son == 1 :
                    winsound.PlaySound ('wasted.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                #voir fin programme
                toucher_mur()

            if murB in collision:
                #son de defaite
                #si le son du jeu est on
                if son == 1 :
                    winsound.PlaySound ('wasted.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                #voir fin programme
                toucher_mur()



        if A == 2 :

            #collision avec la porte declenchant l alarme
            if id_porte1 in collision :
                preambule()

            #collision avec la porte du garde > perdu
            if id_porte2 in collision :
                perdu()

            #collision avec la bonne porte de sortie
            if id_porte3 in collision :
                enfuir()

            #collision avec les murs
            if murA in collision:
                #son de defaite
                #si le son du jeu est on
                if son == 1 :
                    winsound.PlaySound ('wasted.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                #voir fin programme
                toucher_mur()

            if murB in collision:
                #son de defaite
                #si le son du jeu est on
                if son == 1 :
                    winsound.PlaySound ('wasted.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                #voir fin programme
                toucher_mur()



        if A == 3 :

            #collision avec la porte declenchant l alarme
            if id_porte1 in collision :
                preambule()

            #collision avec la porte declenchant l alarme
            if id_porte2 in collision :
                preambule()

            #collision avec la porte du garde > perdu
            if id_porte3 in collision :
                perdu()

            #collision avec les murs
            if murA in collision:
                #son de defaite
                #si le son du jeu est on
                if son == 1 :
                    winsound.PlaySound ('wasted.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                #voir fin programme
                toucher_mur()

            if murB in collision:
                #son de defaite
                #si le son du jeu est on
                if son == 1 :
                    winsound.PlaySound ('wasted.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                #voir fin programme
                toucher_mur()



        if A == 4 :

            #collision avec la porte du garde > perdu
            if id_porte1 in collision :
                preambule()

            #collision avec la bonne porte de sortie
            if id_porte2 in collision :
                enfuir()

           #collision avec la porte declenchant l alarme
            if id_porte3 in collision :
                preambule()


            #collision avec les murs
            if murA in collision:
                #son de defaite
                #si le son du jeu est on
                if son == 1 :
                    winsound.PlaySound ('wasted.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                #voir fin programme
                toucher_mur()

            if murB in collision:
                #son de defaite
                #si le son du jeu est on
                if son == 1 :
                    winsound.PlaySound ('wasted.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                #voir fin programme
                toucher_mur()


        #si le voleur se fait attraper par le policier
        if id_securiteG in collision :
            if son == 1 :
                winsound.PlaySound ('wasted.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            #voir fin programme
            toucher_mur()



    # on continue le jeu
    else :
        #deplacement des images
        canvas.move(img_voleurD, sx * dep, sy * dep)
        canvas.move(img_voleurG, sx * dep, sy * dep)
        canvas.update()
        #on actualise le deplacement de la securite ( voir fin programme )
        deplacement_securite()
        # on actualise (en millisecondes)
        fenetre.after(20, deplacer_voleur2)















#========================================================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================================================#
#Debut du mini jeu 3










#mise en contexte
def preambule():


    global img_alarm


    canvas.delete(ALL)


    #photo de fond
    img_alarm = PhotoImage(file="alarmbackground.gif")
    canvas.create_image(0,0, anchor = NW,image=img_alarm)

    #si le son du jeu est on
    if son == 1 :
        #son d'alarme de maison
        winsound.PlaySound ('cutalarmsound.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)


    #lance le menu avant jeu apres 3s
    fenetre.after(3000,initial_jeu3)





#mise en place de l'avant jeu
def initial_jeu3 ():


    global img_photofond, img_sortie, bouton_enter, but3


    #on suppr les images du contexte
    canvas.delete(ALL)

    #photo de fond
    img_photofond = PhotoImage(file="photo.gif")
    canvas.create_image(0,0, anchor = NW,image=img_photofond)

    #sortie de secours img
    img_sortie = PhotoImage(file="sortie.gif")
    canvas.create_image(200,100, anchor = NW,image=img_sortie)

    #bouton enter
    bouton_enter = PhotoImage(file="bouton.gif")
    canvas.create_image(30,320, anchor = NW,image=bouton_enter)

    #but 3
    but3 = PhotoImage(file="but3.gif")
    canvas.create_image(560,730, anchor = NW,image=but3)


    #bouton de lancement ( initialise par un evenement ) ( voir fin programme )
    canvas.bind_all("<Return>", lancer_jeu3)





#creation du labyrinthe
def tracer_labyrinthe3():


    global sx, sy, canvas_carre_sortie, canvas_carre_depart,img_photomur, id_photomur, img_issue, jeu


    #initialisation des donnees ( afin de reinitialiser le deplacement initial )
    #deplacement selon x
    sx=1
    #deplacement selon y
    sy=0


    #on initialise une commande partielle pour eviter de relancer en appuyant sur entrer en jeu
    canvas.bind_all("<Return>", stop_choix)


    #variable qui sert a mettre la musique du labyrinthe 3 si on mute/demute avec espace
    jeu = 3

    #creation du labyrinthe :

    #effacement de la fenetre d'avant jeu
    canvas.delete(ALL)

    #photo de fond
    img_photomur = PhotoImage(file="murfond.gif")
    id_photomur = canvas.create_image(0,0, anchor = NW, image=img_photomur)
    #on place l'image de fond sous les autres images
    canvas.tag_lower(id_photomur,ALL)

    #case depart
    canvas_carre_depart = canvas.create_rectangle(50,50,100,100, fill="firebrick", outline="firebrick", width=3)

    #case sortie
    canvas_carre_sortie = canvas.create_rectangle(1350,250,1400,300, fill="firebrick", outline="firebrick", width=3)

    #creation mur
    murA = canvas.create_line(100,50, 450,50, 450,350, 100,350,100,600,150,600,150,400,600,400,600,50,850,50,850,550,600,550,550,550,450,550,450,650,550,650,550,550,750,550,750,700,1000,700,1000,550,1050,550,1050,500,950,500,950,250,1350,250, fill="firebrick", width=4)
    murB = canvas.create_line(100,100,400,100,400,300,50,300,50,650,200,650,200,450,650,450,650,100,800,100,800,500,400,500,400,700,600,700,600,600,700,600,700,750,1050,750,1050,600,1100,600,1100,450,1000,450,1000,300,1350,300, fill="firebrick", width=4)


    #issue de secours (accroche au mur)
    img_issue = PhotoImage(file="issue.gif")
    canvas.create_image(1250,50, anchor = NW, image=img_issue)


    #si le son est on
    if son == 1 :
        winsound.PlaySound ('labymusic.wav', winsound.SND_FILENAME | winsound.SND_ASYNC )


    #lancement de l'initialisation du voleur
    initial_voleur3()





#initialisation du voleur
def initial_voleur3():


    global X,Y, img_voleurD, img_voleurG


    #coords initial du voleur dans le labyrinthe 3
    X = 43
    Y = 532


    #on se referencie a l'initialisation complete du jeu 1
    initial_voleur1()
    animation_ascenseur()





#deplacement du voleur
def deplacer_voleur3():


    global img_photowin


    #on initialise les collisions
    #Peu importe l id que l on choisit du voleur, sachant que les deux images sont supperposes
    collision = canvas.find_overlapping(*canvas.bbox(img_voleurD))


    #tu as reussi a t'enfuir
    if canvas_carre_sortie in collision :
        #voir fin programme
        enfuir()


    #tu a touche un mur
    elif  len(collision) >3 :

        #animation police (fin programme)
        animation_defaite()
        #son de defaite
        #si le son du jeu est on
        if son == 1 :
            winsound.PlaySound ('loosesound.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        # affichage d'un message
        canvas.create_text(720,400,text="WASTED", fill="firebrick", font="sans 45 bold")
        # bouton 'rejouer'
        canvas.create_window(720,450,window=Button(canvas, text="Rejouer", command=tracer_labyrinthe3))


    #rien ne s'est passe
    else :
        # on continue le jeu
        canvas.move(img_voleurD, sx * dep, sy * dep)
        canvas.move(img_voleurG, sx * dep, sy * dep)
        canvas.update()
        # on actualise (en millisecondes)
        fenetre.after(20, deplacer_voleur3)
















#=============================================================================================================================================================================================================================================================================================================================================
#Suites conditionnelles des mini jeux :










#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> POUR NIVEAU 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#si le voleur sort du premier labyrinthe
def victoire_etape1():


    global img_victoire1

    #on efface le canevas
    canvas.delete(ALL)
    #photo de fond
    img_victoire1 = PhotoImage(file="victoire1.gif")
    canvas.create_image(0, 0, anchor = NW,image=img_victoire1)
    #affichage d'un message
    canvas.create_text(720,75,text="Tu as derobe tous les objets de valeurs !",font="sans 55 bold",fill="firebrick")
    canvas.create_text(720,170,text="Trouve la sortie !",font="sans 50 bold",fill="firebrick")
    fenetre.after(3500,initial_jeu2)





#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> POUR NIVEAU 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#si le voleur tombe sur l'agent de securite
def perdu():


    global img_agentsecu

    #on efface le canevas
    canvas.delete(ALL)
    #photo de fond
    img_agentsecu = PhotoImage(file="agentsecu.gif")
    canvas.create_image(0,0, anchor = NW,image=img_agentsecu)
    #si le son du jeu est on
    if son == 1 :
        winsound.PlaySound ('nope.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
    #affichage d'un message
    canvas.create_text(720,50,text="Tu as ouvert la mauvaise porte !",font="sans 47 bold",fill="firebrick")
    canvas.create_text(720,110,text="L'agent de securite t'as trouve...",font="sans 40 bold",fill="firebrick")
    canvas.create_text(720,170,text="GAME OVER",font="sans 40 bold",fill="firebrick")
    #bouton 'rejouer'
    canvas.create_window(720,250,window=Button(canvas, text="Rejouer", command=initial_labyrinthe1))





#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> POUR NIVEAUX 1 et 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#si le voleur touche un mur
def toucher_mur():


    global img_perdu, voleur, collision

    #met en pause le programme pour rendre l'animation plus lente(en s)
    time.sleep(0.9)
    #on suppr le contenu de l'ancienne fenetre
    canvas.delete(ALL)
    #photo de fond
    img_perdu = PhotoImage(file="perdu.gif")
    canvas.create_image(0,0, anchor = NW,image=img_perdu)
    # affichage d'un message
    canvas.create_text(720,70,text="TU AS ETE ATTRAPE ", fill="firebrick", font="sans 65 bold")
    canvas.create_window(720,140,window=Button(canvas, text="Recommencer", command=initial_labyrinthe1))





#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> POUR NIVEAU 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#tant que le garde ne touche pas le voleur / le voleur ne sort pas
def deplacement_securite() :


    global id_securiteD

    #on demande les coords du garde de securite
    A = canvas.coords(id_securiteD)
    #on associe les coords en x et y a celle du canevas
    Ax = A[0]
    Ay = A[1]


    # mvmt sy vers le bas
    if Ax == 550 and Ay < 455  :
        canvas.move(id_securiteD, 0, 3)
        canvas.move(id_securiteG, 0, 3)

    # mvmt sx vers la droite
    if Ay == 457 and Ax < 900 :
        canvas.move(id_securiteD, 3, 0)
        canvas.move(id_securiteG, 3, 0)
        canvas.tag_lower(id_securiteG,ALL)
        canvas.tag_raise(id_securiteD,ALL)

    # mvmt sy vers le haut
    if Ax == 901 and Ay > 310 :
        canvas.move(id_securiteD, 0, -3)
        canvas.move(id_securiteG, 0, -3)

    # mvmt sx vers la gauche
    if Ay == 310 and Ax > 550 :
        canvas.move(id_securiteD, -3, 0)
        canvas.move(id_securiteG, -3, 0)
        canvas.tag_lower(id_securiteD,ALL)
        canvas.tag_raise(id_securiteG,ALL)





#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> POUR NIVEAU 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#animation du policier
def animation_defaite():


    global id_voitureG, id_policierG, img_policierG, img_voitureG, id_voitureD, id_policierD, img_policierD, img_voitureD

    #on stop la musique de jeu
    winsound.PlaySound ('stopsound.wav', winsound.SND_FILENAME | winsound.SND_ASYNC )
    #voiture
    img_voitureG = PhotoImage(file="voitureG.gif")
    id_voitureG = canvas.create_image(105, 56, anchor = NW, image=img_voitureG)
    img_voitureD = PhotoImage(file="voitureD.gif")
    id_voitureD = canvas.create_image(1300,255, anchor = NW, image = img_voitureD)

    #policier
    img_policierG = PhotoImage(file="flicG.gif")
    img_policierD = PhotoImage(file="flicD.gif")


    #on lance le deplacement des voitures (animation)
    for loop in range (30):
        sx=-1
        pas=6
        sy=0
        canvas.move(id_voitureD, sx*pas, sy*pas)
        sx=1
        canvas.move(id_voitureG, sx*pas, sy*pas)

        #met en pause le programme pour rendre l'animation plus lente(en s)
        time.sleep(0.035)
        #met a jour la position du canvas
        canvas.update()

    #une fois l animation finie on ajoute les policiers
    id_policierG = canvas.create_image(350, 56, anchor=NW, image=img_policierG)
    id_policierD = canvas.create_image(1065, 255, anchor=NW, image=img_policierD)





#animation ascenseur au debut du jeu
def animation_ascenseur() :


    global img_voleurD, img_voleurG, img_ascenseur, id_ascenseur


    #creation de l'ascenseur
    img_ascenseur = PhotoImage(file='ascenseur.gif')
    id_ascenseur = canvas.create_image(0,0, anchor =NW, image = img_ascenseur)
    canvas.tag_lower(id_ascenseur,img_voleurD)


    #debut de l'animation
    #mvmt de l'ascenseur
    for loop in range(79) :
        canvas.move(id_ascenseur, 0, -6)
        canvas.move(img_voleurD, 0, -6)
        canvas.move(img_voleurG, 0, -6)
        time.sleep(0.035)
        canvas.update()
    time.sleep(0.5)

    #sortie du voleur de l'asenceur
    for loop in range(30) :
        canvas.move(img_voleurD, 3, 0)
        canvas.move(img_voleurG, 3, 0)
        time.sleep(0.035)
        canvas.update()
    deplacer_voleur3()





#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> POUR NIVEAUX 2 et 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#si le voleur reussit a s'enfuir
def enfuir():


    global img_photowin
    #on efface le canevas
    canvas.delete(ALL)

    #photo de fond
    img_photowin = PhotoImage(file="photo2.gif")
    canvas.create_image(0,0, anchor = NW,image=img_photowin)

    #affichage d'un message
    canvas.create_text(720,100,text="Tu as trouve la sortie !",font="sans 47 bold",fill="firebrick")
    canvas.create_text(720,180,text="Tu t'es enfui avec l'argent !",font="sans 40 bold",fill="firebrick")

    #son de victoire
    #si le son du jeu est on
    if son == 1 :
        winsound.PlaySound ('winsound.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

    fenetre.after(6000,menu_finjeu)





#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> POUR TOUT NIVEAUX <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#on definit une fonction quitter afin de stopper le son avant de fermer la fenetre
def quitter() :

    #[faibles possibilites de winsound] == on joue un son 'partiel' pour stopper la musique
    winsound.PlaySound ('stopsound.wav', winsound.SND_FILENAME | winsound.SND_ASYNC )
    fenetre.destroy()









#evenements du voleur pour sprinter et marcher :


def sprinter(event=None) :

    global dep, sprint
    dep = sprint

def marcher(event=None):

    global dep, pas
    dep = pas





#definition des deplacements clavier par des evenements :


def deplacement_gauche (event=None):

    global sx, sy
    sx = -1
    sy = 0

    #on change le sens de l image
    canvas.tag_lower(img_voleurD,ALL)
    canvas.tag_raise(img_voleurG,ALL)
    canvas.update()


def deplacement_droite (event=None):

    global sx, sy
    sx = 1
    sy = 0

    #on change le sens de l image
    canvas.tag_lower(img_voleurG,ALL)
    canvas.tag_raise(img_voleurD,ALL)
    canvas.update()


def deplacement_haut (event=None):

    global sy, sx
    sy = -1
    sx = 0


def deplacement_bas (event=None):

    global sy, sx
    sy = 1
    sx = 0







#evenements lorsque l'on appuis sur la touche entree pour lancer le jeu
def lancer_jeu1 (event=None):

    initial_labyrinthe1()


def lancer_jeu2 (event=None):

    tracer_labyrinthe2()


def lancer_jeu3 (event=None):

    tracer_labyrinthe3()





#fonction pour arreter les events du dessus apres le lancement des jeux
def stop_choix(event=None):
    #rien de se passe ( code randy )
    rien = None














#====================================================================================================================================================================================================================================================================================================================================================================#
#menu d'apres jeu










def menu_finjeu():


    global img_rejouer, img_rejouer2, id_rejouer, id_rejouer2, img_credits, img_credits2, id_credits, id_credits2, img_quitter, id_quitter2, id_quitter, img_quitter2, choix, img_textcredits, id_textcredits


    #on suppr l'ancien contenu de la fenetre
    canvas.delete(ALL)


    #nouveau titre
    fenetre.title("Fast Robbery")


    #photo de fond
    img_menu = PhotoImage(file="menu.gif")
    canvas.create_image(0,0, anchor = NW,image=img_menu)

    #bouton rejouer
    img_rejouer = PhotoImage(file="rejouer.gif")
    id_rejouer = canvas.create_image(552,120, anchor = NW,image=img_rejouer)

    #bouton rejouer quand souris dessus
    img_rejouer2 = PhotoImage(file="rejouer2.gif")
    id_rejouer2 = canvas.create_image(546,128, anchor = NW,image=img_rejouer2)
    canvas.tag_lower(id_rejouer2,ALL)

    #bouton credits
    img_credits = PhotoImage(file="credits.gif")
    id_credits = canvas.create_image(553,300, anchor = NW,image=img_credits)

    #bouton aide quand souris dessus
    img_credits2 = PhotoImage(file="credits2.gif")
    id_credits2 = canvas.create_image(548,307, anchor = NW,image=img_credits2)
    canvas.tag_lower(id_credits2,ALL)

    #bouton quitter
    img_quitter = PhotoImage(file="quitter.gif")
    id_quitter = canvas.create_image(555,480, anchor = NW,image=img_quitter)

    #bouton quitter quand souris dessus
    img_quitter2 = PhotoImage(file="quitter2.gif")
    id_quitter2 = canvas.create_image(553,483, anchor = NW,image=img_quitter2)
    canvas.tag_lower(id_quitter2,ALL)

    #image des credits
    img_textcredits = PhotoImage(file="textcredits.gif")
    id_textcredits = canvas.create_image(370,150, anchor = NW,image=img_textcredits)
    canvas.tag_lower(id_textcredits,ALL)


    #si le son est on
    if son == 1 :
        #[faibles possibilites de winsound] == on joue un son 'partiel' pour stopper la musique
        winsound.PlaySound ('fond.wav', winsound.SND_FILENAME | winsound.SND_ASYNC )


    #initialisation des nouvelles touches clavier
    canvas.bind_all("<Up>",clavier3)
    canvas.bind_all("<Down>",clavier3)
    canvas.bind_all("<Return>",clavier3) #touche entrer


    #variable concernant le choix du bouton
    choix = 0


    fenetre.mainloop()






def clavier3(event):


    global choix, touche


    #Initialisation des detections clavier
    touche = event.keysym


    #si la touche directionnnelle 'bas' et active
    if touche == 'Down':

        #si le bouton selectionne est inferieur a 3 en partant du haut : on descends
        if choix < 3:
            choix+=1

        #sinon on monte au premier
        else:
            choix=1


    #si la touche directionnnelle 'haut' et active
    if touche == 'Up':

        #si le bouton selectionne est superieur a 1 en partant du haut : on monte
        if choix > 1:
            choix-=1

        #sinon on descend au dernier
        else:
            choix=3


    #on lance l'actualisation des boutons
    animation3(choix)


    #si on appuie sur la touhe 'entrer', en fonction du bouton choisis
    if touche == 'Return':
        if choix == 1 :
            choix_perso()

        if choix == 2 :
            menu_credits()

        if choix == 3 :
            #[faibles possibilites de winsound] == on joue un son 'partiel' pour stopper la musique
            winsound.PlaySound ('stopsound.wav', winsound.SND_FILENAME | winsound.SND_ASYNC )
            fenetre.destroy()





def menu_credits():


    #on place les boutons derriere l'image de fond et le texte devant
    canvas.tag_lower(id_rejouer,ALL)
    canvas.tag_lower(id_rejouer2,ALL)
    canvas.tag_lower(id_quitter,ALL)
    canvas.tag_lower(id_quitter2,ALL)
    canvas.tag_lower(id_credits,ALL)
    canvas.tag_lower(id_credits2,ALL)
    canvas.tag_raise(id_textcredits,ALL)





#actualisation graphique des bouton en fonction du choix
def animation3(choix):


    #bouton rejouer
    if choix == 1 :
        canvas.tag_lower(id_textcredits,ALL)
        canvas.tag_lower(id_rejouer,ALL)
        canvas.tag_raise(id_rejouer2,ALL)
        canvas.tag_lower(id_credits2,ALL)
        canvas.tag_raise(id_credits,ALL)
        canvas.tag_lower(id_quitter2,ALL)
        canvas.tag_raise(id_quitter,ALL)


    #bouton credits
    if choix == 2:
        canvas.tag_lower(id_textcredits,ALL)
        canvas.tag_lower(id_rejouer2,ALL)
        canvas.tag_raise(id_rejouer,ALL)
        canvas.tag_lower(id_credits,ALL)
        canvas.tag_raise(id_credits2,ALL)
        canvas.tag_lower(id_quitter2,ALL)
        canvas.tag_raise(id_quitter,ALL)


    #bouton quitter
    if choix == 3 :
        canvas.tag_lower(id_textcredits,ALL)
        canvas.tag_lower(id_credits2,ALL)
        canvas.tag_raise(id_credits,ALL)
        canvas.tag_lower(id_quitter,ALL)
        canvas.tag_raise(id_quitter2,ALL)
        canvas.tag_raise(id_rejouer,ALL)
        canvas.tag_lower(id_rejouer2,ALL)











#=========================================================================================================================================================================================================================================================================


#pour fermer la fenetre avec la croix
def fermer_fenetre() :


    #on stop la musique de jeu
    winsound.PlaySound ('stopsound.wav', winsound.SND_FILENAME | winsound.SND_ASYNC )
    #on suppr la fenetre
    fenetre.destroy()

#=========================================================================================================================================================================================================================================================================















# lancer le jeu
menu_jeu()
