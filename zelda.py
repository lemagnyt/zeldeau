import pygame
import os, inspect
import pygame.surfarray as surfarray
from pygame.transform import scale
import math
import random


#recherche du rÃ©pertoire de travail
scriptPATH = os.path.abspath(inspect.getsourcefile(lambda:0)) # compatible interactive Python Shell
scriptDIR  = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR,"data")
assets1 = os.path.join(scriptDIR,"data/items")
assets2 = os.path.join(scriptDIR,"data/nonitems")
assets3 = os.path.join(scriptDIR,"data/map")
assets4= os.path.join(scriptDIR,"data/son")


GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
BLEU = (0,0,255)
RED = (255,0,0)
#############################################################

#Initialise pygame
pygame.init()

# Set the width and height of the screen [width,height]
screenWidth = 800
screenHeight = 400

#Initialise la hauteur et la largeur de la fenetre
WINDOW_SIZE = [screenWidth, screenHeight]

screen = pygame.display.set_mode(WINDOW_SIZE)
son = pygame.mixer.Sound(os.path.join(assets4, "introson.mp3"))
son.set_volume(0.3)
son.play(loops=-1, maxtime=0, fade_ms=0)
sonmechant = pygame.mixer.Sound(os.path.join(assets4, "mechant.mp3"))
sonmechant.play(loops=-1, maxtime=0, fade_ms=0)
sonmechant.set_volume(0)

#Met le titre du jeu et de la fenetre
pygame.display.set_caption("ZELD'EAU")

#Loop pour savoir quand l'utilisateur appuie sur le bouton fermer
termine = False

#Initialise la clock
clock=pygame.time.Clock()

# liste des etats
EtatMarcheDroite = 100
EtatMarcheGauche  = 200
EtatMarcheAvant  = 300
EtatMarcheArriere  = 400
EtatStop = 500
EtatEpeeDroite = 600
EtatEpeeGauche = 700
EtatEpeeAvant = 800
EtatEpeeArriere = 900
EtatArcDroit = 950
EtatArcGauche = 960
EtatArcHaut = 970
EtatArcBas = 980


#Importe les images
fond = pygame.image.load(os.path.join(assets, "fond.png"))

fondcolision = pygame.image.load(os.path.join(assets3, "map1_colision.png"))
map1=pygame.image.load(os.path.join(assets3, "map1.png"))
map1_colision=pygame.image.load(os.path.join(assets3, "map1_colision.png"))

maison1 = pygame.image.load(os.path.join(assets3, "maisonzelda1.png"))
maison_colision1 = pygame.image.load(os.path.join(assets3, "maisonzelda1_colision.png"))

mapboss=pygame.image.load(os.path.join(assets3,"mapboss.png"))
mapboss_colision=pygame.image.load(os.path.join(assets3,"mapboss_colision.png"))


grotte=pygame.image.load(os.path.join(assets3, "map_grotte.png"))
grotte_colision=pygame.image.load(os.path.join(assets3, "map_grotte_colision.png"))

magasin = pygame.image.load(os.path.join(assets3, "magasin.png"))
magasin_colision=pygame.image.load(os.path.join(assets3, "magasin_colision.png"))

maison2 = pygame.image.load(os.path.join(assets3, "maisonzelda2.png"))
maison_colision2 = pygame.image.load(os.path.join(assets3, "maisonzelda2_colision.png"))

inventaire_sprite = pygame.image.load(os.path.join(assets, "inventaire.png"))
aide_sprite =  pygame.image.load(os.path.join(assets, "aide.png"))

link_sprite=pygame.image.load(os.path.join(assets, "link_sprite.png"))
potionvie = pygame.image.load(os.path.join(assets1, "item1.png"))
potionvitesse = pygame.image.load(os.path.join(assets1, "item2.png"))
potionforce = pygame.image.load(os.path.join(assets1, "item3.png"))
arc = pygame.image.load(os.path.join(assets1, "item4.png"))
coeur = pygame.image.load(os.path.join(assets1, "item5.png"))
nonpotionvie = pygame.image.load(os.path.join(assets2, "nonitem1.png"))
nonpotionvitesse = pygame.image.load(os.path.join(assets2, "nonitem2.png"))
nonpotionforce = pygame.image.load(os.path.join(assets2, "nonitem3.png"))
nonarc = pygame.image.load(os.path.join(assets2, "nonitem4.png"))
noncoeur = pygame.image.load(os.path.join(assets2, "nonitem5.png"))
nonvie = pygame.image.load(os.path.join(assets, "nonvie.png"))
vie = pygame.image.load(os.path.join(assets, "coeur.png"))
monstre_sprite = pygame.image.load(os.path.join(assets, "sprite_boss.png"))

gemmerouge = pygame.image.load(os.path.join(assets, "gemme.png"))
gemmebleu = pygame.image.load(os.path.join(assets, "gemmebleu.png"))
gemmeverte = pygame.image.load(os.path.join(assets, "gemmeverte.png"))

carreitem = pygame.image.load(os.path.join(assets, "pour_item.png"))

tresorouvert = pygame.image.load(os.path.join(assets, "coffreouvert.png"))
tresorferme = pygame.image.load(os.path.join(assets, "coffreferme.png"))
arctresor = pygame.image.load(os.path.join(assets, "arctresor.png"))
coeurtresor = pygame.image.load(os.path.join(assets, "coeurtresor.png"))

forcemagasin = pygame.image.load(os.path.join(assets, "forcemagasin.png"))
viemagasin = pygame.image.load(os.path.join(assets, "viemagasin.png"))
vitessemagasin = pygame.image.load(os.path.join(assets, "vitessemagasin.png"))

fleche = pygame.image.load(os.path.join(assets1, "fleche.png"))
fleche_vertical = pygame.image.load(os.path.join(assets1, "fleche_vertical.png"))

GAMEOVER = pygame.image.load(os.path.join(assets, "GAMEOVER.png"))

feusprite = pygame.image.load(os.path.join(assets1, "bouledefeu.png"))

explosion_sprite = pygame.image.load(os.path.join(assets, "planche_explosion.png"))

triforce_sprite = pygame.image.load(os.path.join(assets1, "triforce.png"))

coeur1 = pygame.image.load(os.path.join(assets, "coeur1.png"))

image_de_fin = pygame.image.load(os.path.join(assets, "image_de_fin.png"))


# liste des items

itemsbool = [False, False, False, True, False]

# liste des items acheté ou non
itemsmagasin = [False,False,False]
itemsprix = [50,50,50]

#liste des trésors
listtresorouvert = [False,False]
tresorcoordonne = [(451,120),(311,100)]
fondtresor = [maison2,maison1]

#Image quand on reçoit un nouvel objet
itemsimage = [viemagasin, vitessemagasin, forcemagasin,arctresor, coeurtresor]

#liste des coeurs présents dans la salle des bosss
LISTcoeur = [[138,86],[638,86]]

#Variable pour les differentes coordonenees
itemssprite = (potionvie, potionvitesse,potionforce, arc, coeur)
nonitemssprite = (nonpotionvie, nonpotionvitesse,nonpotionforce, nonarc, noncoeur)
vitesse = 3
ZJ_xdecor = 50
ZJ_ydecor = 200
commence = False
link_x =screenWidth/2
link_y= screenHeight/2
potionvie_x = 100
potionvie_y = 200
barredevie = 5
itemactif = -1
force = 1
viemax = 5
T0 = -1
T0force = -1
T0tresor = -1
gemme = 0
dansMagasin = False
itemmagasin = -1
inventaire = False
aide = False
coup = False
sprite_epee = 0
T0tresor = 0
afficheimage = -1
tirfleche = False
sprite_fleche = 0
monstreestproche = False
fini = False
degat_epee = 2
degat_arc = 1
boss_x = 348
boss_y = 90
boss_x1 = 348
boss_y1 = 90
vie_max_boss = 16
vie_boss = 16
boss_mort = False
salleboss = False
feuLIST = []
compteur_creation = 0
sprite_explosion = 0
avoirtriforce = False
boostvitesse = False
boostforce = False
triforce_x = 0
triforce_y = 0
GAGNER = False

#Permet la teleportation
teleportation_bool = False
estTeleporter=False
ancien_ZJ_xdecor=0
ancien_ZJ_ydecor=0

#Ancienne coordonnees du link
ancien_link_x=0
ancien_link_y=0

#Largeur du sprite de link
LARG = 32

#Largeur du sprite de monstre
LARG2 = 100

#Fonction qui permet de charger les spites
def ChargeSerieSprites(id,planche_sprites,largeur):
   sprite = []
   for i in range(12):
      spr = planche_sprites.subsurface(((largeur * i), largeur * id, largeur,largeur))
      test = spr.get_at((10,10))
      if ( test != (255,0,0,255) ):
         sprite.append( spr )
   return sprite

def ChargeSerieSprites2(id,planche_sprites,largeur):
   sprite = []
   for i in range(12):
      spr = planche_sprites.subsurface(((largeur * i), largeur * id, largeur-2,largeur+3))
      test = spr.get_at((10,10))
      if ( test != (255,0,0,255) ):
         sprite.append( spr )
   return sprite

def ChargeSerieSprites3(id,planche_sprites,largeur):
   sprite = []
   for i in range(12):
      spr = planche_sprites.subsurface(((largeur * i), largeur * id, largeur-4,largeur-3))
      test = spr.get_at((10,10))
      if ( test != (255,0,0,255) ):
         sprite.append( spr )
   return sprite

def ChargeSerieSprites4(id,planche_sprites,largeur):
   sprite = []
   for i in range(12):
      spr = planche_sprites.subsurface(((largeur * i), largeur * id+5, largeur-10,largeur))
      test = spr.get_at((10,10))
      if ( test != (255,0,0,255) ):
         sprite.append( spr )
   return sprite

def clic() :
   pos = pygame.mouse.get_pos()
   x = pos[0]
   y = pos[1]
   a = 215
   b = screenHeight/2-inventaire_sprite.get_height()/2+100
   for i in range (0,5):
    if(intervalle(x,a+i*75,a+i*75+74) and intervalle(y,b,b+100) and itemsbool[i]) :
        return i
   return -1

def clic1() :
   pos = pygame.mouse.get_pos()
   x = pos[0]
   y = pos[1]
   for i in range (0,3):
    if(intervalle(x,230+i*135,285+i*135) and intervalle(y,75,175) and not itemsmagasin[i]) :
        return i
   return -1

def intervalle(x, a, b) :
   return (a<=x and x<=b)

#Savoir si il y a une collision quand on va vers le bas, return True si il y a une collision
def collision_bas():
    return (fondcolision.get_at((int(ZJ_xdecor+link_x+LARG/2),int(ZJ_ydecor+link_y+LARG)))==(255,255,255))

#Savoir si il y a une collision quand on va vers le haut, return True si il y a une collision
def collision_haut():
    return (fondcolision.get_at((int(ZJ_xdecor+link_x+LARG/2),int(ZJ_ydecor+link_y+10)))==(255,255,255))

#Savoir si il y a une collision quand on va vers la droite, return True si il y a une collision
def collision_droite():
    return (fondcolision.get_at((int(ZJ_xdecor+link_x+LARG-12),int(ZJ_ydecor+link_y+LARG/2)))==(255,255,255))

#Savoir si il y a une collision quand on va vers la gauche, return True si il y a une collision
def collision_gauche():
    return (fondcolision.get_at((int(ZJ_xdecor+link_x-5),int(ZJ_ydecor+link_y+LARG/2)))==(255,255,255))


#Savoir que est le monstre le plus proche
def dist_min(a, b):
    monstremin = -1
    for i in range(0,3) :
        if(monstresmap[i]== fond) :
            if (((a - monstrescoordonnées[i][0])**2 + (b - monstrescoordonnées[i][1])**2) <= ((a - monstrescoordonnées[monstremin][0])**2 + (b - monstrescoordonnées[monstremin][1])**2)) or monstremin==-1 :
                monstremin = i
    if monstres_mort[monstremin] :
        return-1
    else :
        return monstremin


#Permet d'etre repousser
def repousse(a, b, c):
    return   ((ZJ_xdecor + link_x ) - a )**2 + ( (ZJ_ydecor + link_y) - b )**2 <= c**2

#Permet de savoir si il y a un tresor a cote
def tresoracote() :
        for i in range (0,2) :
            if (((link_x +10+ZJ_xdecor-tresorcoordonne[i][0]-25)**2 + (link_y+20+ZJ_ydecor-tresorcoordonne[i][1]-25)**2)<625) and not listtresorouvert[i] and fond==fondtresor[i] :
                return i
        return -1

#############################################################


#Charge les differents sprites de link
marchedroite = ChargeSerieSprites(2,link_sprite,LARG)
marchegauche = ChargeSerieSprites(3,link_sprite,LARG)
marcheavant = ChargeSerieSprites(0,link_sprite,LARG)
marchearriere = ChargeSerieSprites(1,link_sprite,LARG)
arc_arriere=ChargeSerieSprites2(4,link_sprite,LARG)
arc_avant=ChargeSerieSprites2(5,link_sprite,LARG)
arc_droit=ChargeSerieSprites2(6,link_sprite,LARG)
arc_gauche=ChargeSerieSprites2(7,link_sprite,LARG)
epee_arriere=ChargeSerieSprites3(8,link_sprite,LARG+1)
epee_avant=ChargeSerieSprites4(9,link_sprite,LARG)
epee_droit=ChargeSerieSprites3(10,link_sprite,LARG+1)
epee_gauche=ChargeSerieSprites3(11,link_sprite,LARG+1)


#Charge les differents sprites de monstre
monstre1 = ChargeSerieSprites(0,monstre_sprite,LARG2)
monstre2 = ChargeSerieSprites(1,monstre_sprite,LARG2)
monstre3 = ChargeSerieSprites(2,monstre_sprite,LARG2)
monstre4 = ChargeSerieSprites(3,monstre_sprite,LARG2)


#listedesmonstres
monstresimage = [monstre1, monstre2, monstre3]
monstresmap = [map1, grotte, map1]
monstresvie = [2, 4, 6]
monstrescoordonnées = [(330,225),(580,340),(365,865)]
monstres_mort = [False, False, False]
monstresviemax= [2, 4, 6]

#EXPLOSION
explosion=ChargeSerieSprites3(0,explosion_sprite,60)


#Etat de link et de son inventaire
etatlink = EtatStop


## Loop logique principale du jeu, permet de detecter des appuis sur le clavier ainsi que les differentes actions

while not termine:
    time = int( pygame.time.get_ticks() / 100 )
    event = pygame.event.Event(pygame.USEREVENT)
    pygame.event.pump()
    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close
            termine = True  # Flag that we are done so we exit this loop
    if not fini :
        #Commandes clavier
        KeysPressed = pygame.key.get_pressed()

        if not coup and not tirfleche:
            etatlink = EtatStop

        if KeysPressed[pygame.K_RETURN]:
            if not commence :
                sonstart = pygame.mixer.music.load(os.path.join(assets4, "start.wav"))
                pygame.mixer.music.play()
                commence = True
                fond = map1
                screen = pygame.display.set_mode((screenWidth,screenHeight))
                son.set_volume(0)
                son1 = pygame.mixer.Sound(os.path.join(assets4, "son.mp3"))
                son1.set_volume(0.3)
                son1.play(loops=-1, maxtime=0, fade_ms=0)

        if commence and not tirfleche  :
            if not inventaire and not aide  :
                if KeysPressed[pygame.K_UP]:
                    if(ZJ_ydecor+link_y>0 and collision_haut()) :
                            link_y-=vitesse
                            if( (link_y) <= 0 ):
                                if(ZJ_ydecor- screenHeight/2 - LARG/2) < 0:
                                    decalage = ZJ_ydecor
                                    ZJ_ydecor -= decalage
                                    link_y += decalage

                                else :
                                    ZJ_ydecor -= (screenHeight/2)+LARG/2
                                    link_y = (screenHeight/2)-LARG/2
                    etatlink = EtatMarcheAvant

                if KeysPressed[pygame.K_DOWN]:
                    if(ZJ_ydecor+link_y+LARG)<fond.get_height() and collision_bas():
                            link_y+=vitesse
                            if (link_y+LARG>=screenHeight ):
                                if(ZJ_ydecor + screenHeight/2) > (fond.get_height()-screenHeight):
                                    decalage = fond.get_height()-(ZJ_ydecor+screenHeight)
                                    ZJ_ydecor += decalage
                                    link_y -= decalage
                                else :
                                    ZJ_ydecor += (screenHeight/2)-LARG/2
                                    link_y = (screenHeight/2)-LARG/2

                    etatlink = EtatMarcheArriere

                if KeysPressed[pygame.K_LEFT]:
                    if(link_x+ZJ_xdecor)>0 and collision_gauche() :
                            link_x-=vitesse
                            if( (link_x) <= 0 ):
                                if(ZJ_xdecor- screenWidth/2) < 0:
                                    decalage = ZJ_xdecor
                                    ZJ_xdecor -= decalage
                                    link_x +=decalage
                                else :
                                    ZJ_xdecor -= (screenWidth/2)+LARG/2
                                    link_x = screenWidth/2-LARG/2

                    etatlink = EtatMarcheGauche

                if KeysPressed[pygame.K_RIGHT]:
                    if(link_x+LARG+ZJ_xdecor)<fond.get_width() and collision_droite() :
                            link_x+=vitesse
                            if( (link_x + LARG) >= screenWidth ):
                                if(ZJ_xdecor+ screenWidth/2) > (fond.get_width()- screenWidth):
                                    decalage = fond.get_width()-(ZJ_xdecor+screenWidth)
                                    ZJ_xdecor += decalage
                                    link_x -=decalage
                                else :
                                    ZJ_xdecor += (screenWidth/2)-LARG/2
                                    link_x = screenWidth/2-LARG/2

                    etatlink = EtatMarcheDroite

                if KeysPressed[pygame.K_e]:
                    numero = tresoracote()
                    if numero >=0 :
                        listtresorouvert[numero] = True
                        afficheimage = numero+3
                        T0tresor = int(pygame.time.get_ticks()/1000)
                        coffreitem = pygame.mixer.music.load(os.path.join(assets4, "coffreitem.wav"))
                        pygame.mixer.music.play()
                        itemsbool[numero+3] = True

                #ARC
                if KeysPressed[pygame.K_d] and not dansMagasin and itemactif==3:
                    son_arc=pygame.mixer.music.load(os.path.join(assets4,"arc.mp3"))
                    pygame.mixer.music.play()
                    etatlink = EtatArcDroit
                    tirfleche = True
                    fleche_x = link_x+15
                    fleche_y= link_y+ LARG/2
                    degat = 1
                if KeysPressed[pygame.K_q] and not dansMagasin and itemactif==3:
                    son_arc=pygame.mixer.music.load(os.path.join(assets4,"arc.mp3"))
                    pygame.mixer.music.play()
                    etatlink = EtatArcGauche
                    tirfleche = True
                    fleche_x = link_x+LARG/2-15
                    fleche_y= link_y+ LARG/2+2
                    degat = 1
                if KeysPressed[pygame.K_z] and not dansMagasin and itemactif==3:
                    son_arc=pygame.mixer.music.load(os.path.join(assets4,"arc.mp3"))
                    pygame.mixer.music.play()
                    etatlink = EtatArcHaut
                    tirfleche = True
                    fleche_x = link_x+LARG/2-5
                    fleche_y= link_y+ LARG/2-15
                    degat = 1
                if KeysPressed[pygame.K_s] and not dansMagasin and itemactif==3:
                    son_arc=pygame.mixer.music.load(os.path.join(assets4,"arc.mp3"))
                    pygame.mixer.music.play()
                    etatlink = EtatArcBas
                    tirfleche = True
                    fleche_x = link_x+LARG/2-10
                    fleche_y= link_y+ LARG/2+5
                    degat = 1

                #Commande pour utiliser un objet
                if KeysPressed[pygame.K_SPACE]:
                    if itemactif==0 and barredevie<viemax :
                            barredevie = 5
                            itemsbool[0] = False
                            itemactif = -1
                            son2 = pygame.mixer.music.load(os.path.join(assets4, "potion.mp3"))
                            pygame.mixer.music.play()
                    if itemactif == 1 :
                            vitesse *= 2
                            boostvitesse = True
                            T0 = int(pygame.time.get_ticks()/1000)
                            itemsbool[1] = False
                            itemactif = -1
                            son2 = pygame.mixer.music.load(os.path.join(assets4, "potion.mp3"))
                            pygame.mixer.music.play()
                    if itemactif == 2 :
                            degat_arc *= 2
                            degat_epee *= 2
                            boostforce = True
                            T0force = int(pygame.time.get_ticks()/1000)
                            itemsbool[2] = False
                            itemactif = -1
                            son2 = pygame.mixer.music.load(os.path.join(assets4, "potion.mp3"))
                            pygame.mixer.music.play()
                    if itemactif == 4 :
                            viemax +=1
                            barredevie += 1
                            itemsbool[4] = False
                            itemactif = -1
                            soncoeur = pygame.mixer.music.load(os.path.join(assets4, "soncoeur.wav"))
                            pygame.mixer.music.play()

                # coup épée
                if event.type == pygame.MOUSEBUTTONDOWN and not dansMagasin and etatlink==EtatStop and not coup :
                    son_epee=pygame.mixer.music.load(os.path.join(assets4,"epee.mp3"))
                    pygame.mixer.music.play()
                    if not salleboss:
                        monstre_proche = dist_min( (ZJ_xdecor + link_x), (ZJ_ydecor + link_y) )
                        if monstre_proche == -1 :
                            etatlink = EtatEpeeArriere
                        else:
                            mp_x =  monstrescoordonnées[monstre_proche][0]
                            mp_y =  monstrescoordonnées[monstre_proche][1]
                            if( mp_x >= ( ZJ_xdecor + link_x ) and mp_y >= ( ZJ_ydecor + link_y )):
                                if( (mp_x - ( ZJ_xdecor + link_x ))**2 <= ( mp_y - ( ZJ_ydecor + link_y ))**2 ):
                                    etatlink = EtatEpeeArriere
                                else:
                                    etatlink = EtatEpeeDroite
                            elif( mp_x <= ( ZJ_xdecor + link_x ) and mp_y > ( ZJ_ydecor + link_y )):
                                if( (mp_x - ( ZJ_xdecor + link_x ))**2 <= ( mp_y - ( ZJ_ydecor + link_y ))**2 ):
                                    etatlink = EtatEpeeArriere
                                else:
                                    etatlink = EtatEpeeGauche
                            elif( mp_x > ( ZJ_xdecor + link_x ) and mp_y <= ( ZJ_ydecor + link_y )):
                                if( (mp_x - ( ZJ_xdecor + link_x ))**2 <= (mp_y - ( ZJ_ydecor + link_y ))**2 ):
                                    etatlink = EtatEpeeDroite
                                else:
                                    etatlink = EtatEpeeAvant
                            elif( mp_x < ( ZJ_xdecor + link_x ) and mp_y < ( ZJ_ydecor + link_y )):
                                if( (mp_x - ( ZJ_xdecor + link_x ))**2 <= ( mp_y - ( ZJ_ydecor + link_y ))**2 ):
                                    etatlink = EtatEpeeAvant
                                else:
                                    etatlink = EtatEpeeGauche
                    else:
                            if( boss_x >= ( ZJ_xdecor + link_x ) and boss_y >= ( ZJ_ydecor + link_y )):
                                if( ( boss_x- ( ZJ_xdecor + link_x ))**2 <= ( boss_y - ( ZJ_ydecor + link_y ))**2 ):
                                    etatlink = EtatEpeeArriere
                                else:
                                    etatlink = EtatEpeeDroite
                            elif( boss_x <= ( ZJ_xdecor + link_x ) and boss_y > ( ZJ_ydecor + link_y )):
                                if( ( boss_x - ( ZJ_xdecor + link_x ))**2 <= ( boss_y - ( ZJ_ydecor + link_y ))**2 ):
                                    etatlink = EtatEpeeArriere
                                else:
                                    etatlink = EtatEpeeGauche
                            elif( boss_x > ( ZJ_xdecor + link_x ) and boss_y <= ( ZJ_ydecor + link_y )):
                                if( (boss_x - ( ZJ_xdecor + link_x ))**2 <= (boss_y - ( ZJ_ydecor + link_y ))**2 ):
                                    etatlink = EtatEpeeDroite
                                else:
                                    etatlink = EtatEpeeAvant
                            elif( boss_x < ( ZJ_xdecor + link_x ) and boss_y < ( ZJ_ydecor + link_y )):
                                if( (boss_x - ( ZJ_xdecor + link_x ))**2 <= ( boss_y - ( ZJ_ydecor + link_y ))**2 ):
                                    etatlink = EtatEpeeAvant
                                else:
                                    etatlink = EtatEpeeGauche
                    coup = True
                    degat = 2




            #ouvrir l'inventaire
            if KeysPressed[pygame.K_t]:
                if not inventaire and not aide:
                    inventaire = True
                    sonouvrirmenu = pygame.mixer.music.load(os.path.join(assets4, "ouvrirmenu.wav"))
                    pygame.mixer.music.play()

            #ouvrir l'aide
            if KeysPressed[pygame.K_ESCAPE]:
                if not inventaire and not aide:
                    aide = True
                    sonouvrirmenu = pygame.mixer.music.load(os.path.join(assets4, "ouvrirmenu.wav"))
                    pygame.mixer.music.play()


            #fermer l'inventaire
            if KeysPressed[pygame.K_BACKSPACE]:
                if inventaire or aide :
                    inventaire = False
                    fermermenu = pygame.mixer.music.load(os.path.join(assets4, "fermermenu.wav"))
                    pygame.mixer.music.play()
                    inventaire = False
                    aide =False

            # commande pour sélectionner un item
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inventaire :
                    ancienitem = itemactif
                    if clic()>=0 :
                        itemactif = clic()
                    if ancienitem!=itemactif and itemactif>=0 :
                        sonchoixitem = pygame.mixer.music.load(os.path.join(assets4, "choixitem.wav"))
                        pygame.mixer.music.play()
                if dansMagasin :
                    itemachete = clic1()
                    if itemachete>=0  :
                        if gemme>=itemsprix[itemachete] :
                            itemsmagasin[itemachete]=True
                            gemme-=itemsprix[itemachete]
                            itemsbool[itemachete]=True
                            afficheimage = itemachete
                            T0tresor = int(pygame.time.get_ticks()/1000)
                            recevoiritem = pygame.mixer.music.load(os.path.join(assets4, "recevoiritem.wav"))
                            pygame.mixer.music.play()

            #booster la vitesse 20 secondes
        if T0 >= 0 :
            T1 =  int(pygame.time.get_ticks()/1000)
            if T1-T0 > 20 :
                vitesse = 3
                T0 = -1
                boostvitesse = False

            #booster la force 20 secondes
        if T0force >= 0 :
            T1force =  int(pygame.time.get_ticks()/1000)
            if T1force-T0force > 20 :
                degat_arc = 1
                degat_epee = 2
                T0force = -1
                boostforce = False

            # Afficher l'image durant 3 secondes
        if T0tresor >= 0 :
            T1tresor =  int(pygame.time.get_ticks()/1000)
            if T1tresor-T0tresor > 3:
                afficheimage = -1
                T0tresor = -1


    ##Permet de ramasser des items
        #ramasser triforce
        if (((link_x +10-triforce_x-15)**2 + (link_y+20-triforce_y-15)**2)<225) and fond==mapboss and avoirtriforce:
            sonvictoire = pygame.mixer.Sound(os.path.join(assets4, "victoire.mp3"))
            sonvictoire.set_volume(0.4)
            sonvictoire.play(loops=0, maxtime=0, fade_ms=0)
            GAGNER = True
            sonvictoireboss.set_volume(0)


        #ramasser coeurs
        for i in range (0,2):
            if (((link_x +10-LISTcoeur[i][0]-10)**2 + (link_y+20-LISTcoeur[i][1]-10)**2)<100) and fond==mapboss:
                soncoeur1 = pygame.mixer.music.load(os.path.join(assets4, "soncoeur.wav"))
                pygame.mixer.music.play()
                LISTcoeur[i][0]=1000
                if barredevie < viemax :
                    barredevie += 1


    ##Permet la teleportation dans des maisons et dans la grotte

        if not estTeleporter:
            #Pour les maisons rouges
            if (KeysPressed[pygame.K_UP] and not collision_haut() and fondcolision.get_at((int(ZJ_xdecor+link_x+LARG/2),int(ZJ_ydecor+link_y)))==(0,255,0)):
                ancien_link_x=link_x+ZJ_xdecor
                ancien_link_y=link_y+ZJ_ydecor
                ancien_ZJ_xdecor=ZJ_xdecor
                ancien_ZJ_ydecor=ZJ_ydecor
                ZJ_xdecor=0
                ZJ_ydecor=0
                teleportation_bool= True
                fond = maison1
                link_x=396
                link_y=290
                fondcolision=maison_colision1

            #Pour les maisons bleues
            elif (KeysPressed[pygame.K_UP] and not collision_haut() and fondcolision.get_at((int(ZJ_xdecor+link_x+LARG/2),int(ZJ_ydecor+link_y)))==(0,0,255)):
                teleportation_bool = True
                ancien_link_x=link_x
                ancien_link_y=link_y
                fond=maison2
                link_x=560
                link_y=242
                fondcolision=maison_colision2
                ancien_ZJ_xdecor=ZJ_xdecor
                ancien_ZJ_ydecor=ZJ_ydecor
                ZJ_xdecor=0
                ZJ_ydecor=0

            #Pour la grotte
            elif (KeysPressed[pygame.K_UP] and not collision_haut() and fondcolision.get_at((int(ZJ_xdecor+link_x+LARG/2),int(ZJ_ydecor+link_y)))==(255,255,0)):
                ancien_link_x=link_x
                ancien_link_y=link_y
                ancien_ZJ_xdecor=ZJ_xdecor
                ancien_ZJ_ydecor=ZJ_ydecor
                fond=grotte
                fondcolision=grotte_colision
                ZJ_xdecor=0
                ZJ_ydecor=670
                link_x = 110
                link_y = 157
                teleportation_bool = True

            #Pour le magasin
            elif (KeysPressed[pygame.K_UP] and not collision_haut() and fondcolision.get_at((int(ZJ_xdecor+link_x+LARG/2),int(ZJ_ydecor+link_y)))==(255,0,255)):
                ancien_link_x=link_x
                ancien_link_y=link_y
                ancien_ZJ_xdecor=ZJ_xdecor
                ancien_ZJ_ydecor=ZJ_ydecor
                ZJ_xdecor=0
                ZJ_ydecor=0
                link_x=387
                link_y=350
                teleportation_bool = True
                fond=magasin
                fondcolision=magasin_colision
                new_decor_x=0
                new_decor_y=0
                dansMagasin=True
                son1.set_volume(0)
                sonmagasin = pygame.mixer.Sound(os.path.join(assets4, "magasin.mp3"))
                sonmagasin.set_volume(0.4)
                sonmagasin.play(loops=-1, maxtime=0, fade_ms=0)


    ##Permet de se reteleporter dans la map principale

        if teleportation_bool and estTeleporter:
            #Si on etait dans la maison rouge
            if (fondcolision.get_at((int(ZJ_xdecor+link_x+LARG/2),int(ZJ_ydecor+link_y+LARG)))==(0,255,0)) and KeysPressed[pygame.K_DOWN]:
                teleportation_bool=False
                link_x=ancien_link_x-ancien_ZJ_xdecor
                link_y=ancien_link_y-ancien_ZJ_ydecor
                fond=map1
                fondcolision=map1_colision
                ZJ_xdecor=ancien_ZJ_xdecor
                ZJ_ydecor=ancien_ZJ_ydecor

            #Si on etait dans la maison bleue
            if fondcolision.get_at((int(ZJ_xdecor+link_x+LARG-12),int(ZJ_ydecor+link_y+LARG/2+10)))==(0,0,255):
                teleportation_bool=False
                link_x=ancien_link_x
                link_y=ancien_link_y
                fond=map1
                fondcolision=map1_colision
                ZJ_xdecor=ancien_ZJ_xdecor
                ZJ_ydecor=ancien_ZJ_ydecor

            #Si on etait dans le magasin
            if fond == magasin and KeysPressed[pygame.K_BACKSPACE]:
                ZJ_xdecor=ancien_ZJ_xdecor
                ZJ_ydecor=ancien_ZJ_ydecor
                teleportation_bool=False
                link_x=ancien_link_x
                link_y=ancien_link_y
                fond=map1
                fondcolision=map1_colision
                dansMagasin=False
                sonmagasin.set_volume(0)
                son1.set_volume(0.3)

            #Si on etait dans la grotte et qu'on revient dans la map1
            if fondcolision.get_at((int(ZJ_xdecor+link_x+LARG/2),int(ZJ_ydecor+link_y)))==(100,100,100) and KeysPressed[pygame.K_UP]:
                teleportation_bool=False
                ZJ_xdecor=ancien_ZJ_xdecor
                ZJ_ydecor=ancien_ZJ_ydecor
                link_x=ancien_link_x+10
                link_y=ancien_link_y+20
                fond=map1
                fondcolision = map1_colision

            #Si on etait dans la grotte et qu'on va dans la salle du boss
            if (fondcolision.get_at((int(ZJ_xdecor+link_x+LARG/2),int(ZJ_ydecor+link_y)))==(0,0,0) and KeysPressed[pygame.K_UP]) :
                teleportation_bool=True
                ZJ_xdecor=0
                ZJ_ydecor=0
                fond=mapboss
                fondcolision=mapboss_colision
                link_x=393
                link_y=328
                salleboss = True
                son1.set_volume(0)
                sonboss = pygame.mixer.Sound(os.path.join(assets4, "boss.mp3"))
                sonboss.set_volume(0.3)
                sonboss.play(loops=-1, maxtime=0, fade_ms=0)

        #Affiche tresor ouvert ou ferme
        for i in range (0,2) :
            if fond==fondtresor[i] :
                if listtresorouvert[i] :
                    screen.blit(tresorouvert,(tresorcoordonne[i][0]-ZJ_xdecor,tresorcoordonne[i][1]-ZJ_ydecor))
                else :
                    screen.blit(tresorferme,(tresorcoordonne[i][0]-ZJ_xdecor,tresorcoordonne[i][1]-ZJ_ydecor))

    ##Affiche la map et le rectangle

        if commence :
            if teleportation_bool :
                zonejaune=pygame.Rect(ZJ_xdecor,ZJ_ydecor,screenWidth, screenHeight)
                screen.blit(fond,(0,0),area=zonejaune)
                estTeleporter=True
            elif not teleportation_bool:
                estTeleporter=False
                zonejaune = pygame.Rect(  ZJ_xdecor, ZJ_ydecor, screenWidth, screenHeight )
                screen.blit(fond,(0,0),area = zonejaune)
        else :
            screen.blit(fond,(0,0))


    ##Décalage car tros près des monstres

        if(fond == map1):
            if( repousse(monstrescoordonnées[0][0], monstrescoordonnées[0][1], 30 ) and not monstres_mort[0]  ):
                if( etatlink == EtatMarcheAvant or etatlink == EtatMarcheGauche):
                    link_y += 50
                elif( etatlink == EtatMarcheDroite):
                    link_x -= 50
                elif( etatlink == EtatMarcheArriere):
                    link_y -= 50
                barredevie -= 1
                degat=pygame.mixer.music.load(os.path.join(assets4, "degat.wav"))
                pygame.mixer.music.play()
                etatlink = EtatStop


            if( repousse(monstrescoordonnées[2][0]+25, monstrescoordonnées[2][1]+25, 50 ) and not monstres_mort[2] ):
                if( etatlink == EtatMarcheAvant ):
                    link_y += 40
                elif( etatlink == EtatMarcheGauche ):
                    link_x += 20
                elif( etatlink == EtatMarcheDroite ):
                    link_x -= 50
                elif( etatlink == EtatMarcheArriere ):
                    link_x -= 50
                barredevie -= 1
                degat=pygame.mixer.music.load(os.path.join(assets4, "degat.wav"))
                pygame.mixer.music.play()
                etatlink = EtatStop

        elif( fond == grotte ):
            if( repousse(monstrescoordonnées[1][0] + 25, monstrescoordonnées[1][1] + 25, 60 ) and not monstres_mort[1]  ):
                if( etatlink == EtatMarcheAvant ):
                    link_y += 50
                elif( etatlink == EtatMarcheGauche ):
                    link_x += 50
                elif( etatlink == EtatMarcheDroite ):
                    link_x -= 50
                elif( etatlink == EtatMarcheArriere ):
                    link_y -= 50
                barredevie -= 1
                degat=pygame.mixer.music.load(os.path.join(assets4, "degat.wav"))
                pygame.mixer.music.play()
                etatlink = EtatStop
        elif fond == mapboss:
            if( repousse(boss_x+50, boss_y+50, 50 ) and not boss_mort ):
                if( etatlink == EtatMarcheAvant ):
                    link_y += 50
                elif( etatlink == EtatMarcheGauche ):
                    link_x += 50
                elif( etatlink == EtatMarcheDroite ):
                    link_x -= 50
                elif( etatlink == EtatMarcheArriere ):
                    link_y -= 50
                etatlink = EtatStop

    #Affiche tresor ouvert ou ferme
        for i in range (0,2) :
            if fond==fondtresor[i] :
                if listtresorouvert[i] :
                    screen.blit(tresorouvert,(tresorcoordonne[i][0]-ZJ_xdecor,tresorcoordonne[i][1]-ZJ_ydecor))
                else :
                    screen.blit(tresorferme,(tresorcoordonne[i][0]-ZJ_xdecor,tresorcoordonne[i][1]-ZJ_ydecor))


    ##Affichez les monstres

        #dégât à l'épée
        if event.type == pygame.MOUSEBUTTONDOWN and etatlink!= EtatMarcheArriere and etatlink!= EtatMarcheAvant and etatlink != EtatMarcheGauche and etatlink!=EtatMarcheDroite and sprite_epee==0:
            if salleboss:
                 if( link_x  - boss_x-50)**2 + (link_y - boss_y-50 )**2 <= 75**2 :
                    vie_boss -= degat_epee
                    if( vie_boss <= 0 ):
                        if not boss_mort:
                            barredevie = viemax
                            gemme+=1000
                        boss_mort = True

            else:
                for i in range (0,3) :
                    if fond==monstresmap[i] :
                        if(monstresimage==monstre3) :
                            dec = 50
                        else :
                            dec = 25
                        if( ((ZJ_xdecor + link_x ) - (monstrescoordonnées[i][0] + dec))**2 + ( (ZJ_ydecor + link_y) - (monstrescoordonnées[i][1] + dec))**2 < 60**2):
                            monstresvie[i] -= degat_epee
                            print(monstresvie[i])
                            if( monstresvie[i] <= 0 ):
                                if not monstres_mort[i]:
                                    gemme += 100
                                monstres_mort[i] = True
                                monstre_mort = pygame.mixer.music.load(os.path.join(assets4, "chewbaka.mp3"))
                                pygame.mixer.music.play()

        #dégât à l'arc
        if etatlink == EtatArcDroit :
            pointefleche_x = fleche_x+20
            pointefleche_y = fleche_y+2
        if etatlink == EtatArcGauche :
            pointefleche_x = fleche_x
            pointefleche_y = fleche_y+2
        if etatlink == EtatArcHaut :
            pointefleche_x = fleche_x+2
            pointefleche_y = fleche_y
        if etatlink == EtatArcBas :
            pointefleche_x = fleche_x+2
            pointefleche_y = fleche_y+20
        if tirfleche :
            for i in range (0,3) :
                dec1 = 25
                if monstresimage[i]==monstre2:
                    dec1= 10
                if  monstresimage[i]==monstre3 :
                    dec1 = 35
                if ((monstrescoordonnées[i][0]+dec1-ZJ_xdecor-pointefleche_x)**2 + (monstrescoordonnées[i][1]+dec1-ZJ_ydecor-pointefleche_y)**2)<dec1*20 and monstresmap[i]==fond and not  monstres_mort[i] :
                    tirfleche = False
                    son_arc=pygame.mixer.music.load(os.path.join(assets4,"bruit-de-fleche.mp3"))
                    pygame.mixer.music.play()
                    sprite_fleche = 0
                    monstresvie[i] -= degat_arc
                    if( monstresvie[i] <= 0 ):
                        if not monstres_mort[i]:
                            gemme += 100
                        monstres_mort[i] = True
            if fond == mapboss :
                if ((boss_x+50-pointefleche_x)**2 + (boss_y+50-pointefleche_y)**2)<50*20 and not boss_mort:
                    tirfleche = False
                    sprite_fleche = 0
                    vie_boss -= degat_arc
                    if( vie_boss <= 0 ):
                        if not boss_mort:
                            barredevie = viemax
                            gemme += 1000
                        boss_mort = True

        #Affichez le monstre si pas mort
        for i in range (0,3) :
            if not monstres_mort[i] and monstresmap[i]==fond:
                if(monstresimage[i] == monstre3):
                    screen.blit(monstresimage[i][time%8],(monstrescoordonnées[i][0]-ZJ_xdecor,monstrescoordonnées[i][1]-ZJ_ydecor))
                else :
                    screen.blit(monstresimage[i][time%len(monstresimage[i])],(monstrescoordonnées[i][0]-ZJ_xdecor,monstrescoordonnées[i][1]-ZJ_ydecor))


    ##Affichez link et les differents style graphique


        if( etatlink != EtatEpeeDroite and etatlink != EtatEpeeGauche and etatlink != EtatEpeeAvant and etatlink != EtatEpeeArriere ):
            sprite_epee = 0
            coup = False

        if( sprite_epee >= 3 ):
            coup = False
            sprite_epee = 0

        if( sprite_fleche >= 15 ):
            tirfleche = False
            sprite_fleche = 0

        if commence :
            if not dansMagasin :
                if etatlink == EtatStop :
                    screen.blit(marchearriere[2],(link_x,link_y))

                if etatlink == EtatMarcheDroite :
                    screen.blit(marchedroite[time%len(marchedroite)],(link_x,link_y))

                if etatlink == EtatMarcheGauche :
                    screen.blit(marchegauche[time%len(marchegauche)],(link_x,link_y))

                if etatlink == EtatMarcheArriere :
                    screen.blit(marchearriere[time%len(marchearriere)],(link_x,link_y))

                if etatlink == EtatMarcheAvant :
                    screen.blit(marcheavant[time%len(marcheavant)],(link_x,link_y))

                if etatlink == EtatEpeeDroite :
                    screen.blit(epee_droit[int(sprite_epee)],(link_x,link_y))
                    sprite_epee += 0.25

                if etatlink == EtatEpeeGauche :
                    screen.blit(epee_gauche[int(sprite_epee)],(link_x,link_y))
                    sprite_epee += 0.25

                if etatlink == EtatEpeeAvant :
                    screen.blit(epee_avant[int(sprite_epee)],(link_x,link_y))
                    sprite_epee += 0.25

                if etatlink == EtatEpeeArriere :
                    screen.blit(epee_arriere[int(sprite_epee)],(link_x,link_y))
                    sprite_epee += 0.25

                if etatlink == EtatArcDroit :

                    if int(sprite_fleche<3) :
                        screen.blit(arc_droit[int(sprite_fleche)],(link_x,link_y))
                        sprite_fleche += 0.25

                    elif fondcolision.get_at((int(ZJ_xdecor+fleche_x+20),int(ZJ_ydecor+fleche_y+2)))==(255,255,255) :
                        fleche_x+=3
                        screen.blit(fleche,(fleche_x,fleche_y))
                        screen.blit(arc_droit[0],(link_x,link_y))
                        sprite_fleche += 0.25
                    else :
                        sprite_fleche=0
                        tirfleche = False
                        son_arc=pygame.mixer.music.load(os.path.join(assets4,"bruit-de-fleche.mp3"))
                        pygame.mixer.music.play()

                if etatlink == EtatArcGauche :

                    if int(sprite_fleche<3) :
                        screen.blit(arc_gauche[int(sprite_fleche)],(link_x,link_y))
                        sprite_fleche += 0.25

                    elif fondcolision.get_at((int(ZJ_xdecor+fleche_x),int(ZJ_ydecor+fleche_y+2)))==(255,255,255):
                        fleche_x-=3
                        screen.blit(pygame.transform.flip(fleche, True, False),(fleche_x,fleche_y))
                        screen.blit(arc_gauche[0],(link_x,link_y))
                        sprite_fleche += 0.25
                    else :
                        sprite_fleche = 0
                        tirfleche = False
                        son_arc=pygame.mixer.music.load(os.path.join(assets4,"bruit-de-fleche.mp3"))
                        pygame.mixer.music.play()

                if etatlink == EtatArcHaut :

                    if int(sprite_fleche<3) :
                        screen.blit(arc_avant[int(sprite_fleche)],(link_x,link_y))
                        sprite_fleche += 0.25

                    elif fondcolision.get_at((int(ZJ_xdecor+fleche_x+2),int(ZJ_ydecor+fleche_y)))==(255,255,255):
                        fleche_y-=3
                        screen.blit(fleche_vertical,(fleche_x,fleche_y))
                        screen.blit(arc_avant[0],(link_x,link_y))
                        sprite_fleche += 0.25
                    else :
                        sprite_fleche = 0
                        tirfleche = False
                        son_arc=pygame.mixer.music.load(os.path.join(assets4,"bruit-de-fleche.mp3"))
                        pygame.mixer.music.play()

                if etatlink == EtatArcBas:

                    if int(sprite_fleche<3) :
                        screen.blit(arc_arriere[int(sprite_fleche)],(link_x,link_y))
                        sprite_fleche += 0.25

                    elif fondcolision.get_at((int(ZJ_xdecor+fleche_x+2),int(ZJ_ydecor+fleche_y+20)))==(255,255,255):
                        fleche_y+=3
                        screen.blit(pygame.transform.flip(fleche_vertical, False, True),(fleche_x,fleche_y))
                        screen.blit(arc_arriere[0],(link_x,link_y))
                        sprite_fleche += 0.25
                    else :
                        sprite_fleche = 0
                        tirfleche = False
                        son_arc=pygame.mixer.music.load(os.path.join(assets4,"bruit-de-fleche.mp3"))
                        pygame.mixer.music.play()

            #affichebarredevie
            for i in range(0,viemax):
                if(i<barredevie) :
                    screen.blit(vie,(0+i*32, screenHeight-vie.get_height()))
                else:
                    screen.blit(nonvie,(0+i*32, screenHeight-vie.get_height()))

            #affichage barre de vie du monstre
            monstre_proche = dist_min( (ZJ_xdecor + link_x), (ZJ_ydecor + link_y) )
            if monstre_proche != -1 :
                if((ZJ_xdecor+link_x - monstrescoordonnées[monstre_proche][0])**2 + (ZJ_ydecor+link_y - monstrescoordonnées[monstre_proche][1])**2) < 125**2 :
                    if not monstreestproche :
                        son1.set_volume(0)
                        sonmechant.set_volume(0.8)
                        monstreestproche = True
                    dec =0
                    if monstresimage[monstre_proche]==monstre3 or monstresimage[monstre_proche]==monstre2:
                        dec = 30
                    screen.blit(monstresimage[monstre_proche][0],(0, 0))
                    for i in range(0,monstresviemax[monstre_proche]):
                        if(i<monstresvie[monstre_proche]) :
                            screen.blit(scale(vie,(15,15)),(40+dec+i*15, 20+dec))
                        else:
                            screen.blit(scale(nonvie,(15,15)),(40+dec+i*15, 20+dec))
                elif monstreestproche :
                    monstreestproche = False
                    sonmechant.set_volume(0)
                    son1.set_volume(0.3)
            elif monstreestproche :
                monstreestproche = False
                sonmechant.set_volume(0)
                son1.set_volume(0.3)

            #affichage barre de vie du boss
            if salleboss and not boss_mort :
                screen.blit(monstre4[0],(0, 0))
                for i in range(0,vie_max_boss):
                    if(i<vie_boss) :
                        screen.blit(scale(vie,(15,15)),(40+i*15, 20))
                    else:
                        screen.blit(scale(nonvie,(15,15)),(40+i*15, 20))

            # afficher objets et prix dans le magasin
            if dansMagasin :
                for i in range(0,3) :
                    if  not itemsmagasin[i] :
                        screen.blit(scale(itemssprite[i],(100,100)),(210+i*130,75))
                        police = pygame.font.SysFont("Arial", 20)
                        zone = police.render( str(itemsprix[i]), True, WHITE)
                        screen.blit(zone,(252+i*130, 160))


            # afficher l'item actif
            screen.blit(carreitem, (730, 10))
            if(itemactif>=0) :
                screen.blit(scale(itemssprite[itemactif],(50,50)), (730,8))

            # afficher le nombre de gemmes
            if gemme >= 200 :
                screen.blit(scale(gemmerouge,(15,30)), (660,20))
            elif gemme >= 100 :
                screen.blit(scale(gemmebleu,(15,30)), (660,20))
            else :
                screen.blit(scale(gemmeverte,(15,30)), (660,20))
            police = pygame.font.SysFont("Arial", 25)
            zone = police.render( str(gemme), True, WHITE)
            screen.blit(zone,(680, 20))

            #afficher le message du tresor
            if(tresoracote()>=0) and not inventaire and not aide:
                police = pygame.font.SysFont("Aharoni", 40)
                zone = police.render("APPUYER SUR 'E' POUR OUVRIR LE TRESOR", True, WHITE)
                screen.blit(zone,(10, 10))




            #SALLE DU BOSS
            if salleboss :
                #affiche les coeurs qu'on peut ramasser
                for i in range (0,2):
                    screen.blit(scale(coeur1,(20,20)),(LISTcoeur[i][0],LISTcoeur[i][1]))
                if not boss_mort:
                    #affiche le boss
                    screen.blit(scale(monstre4[int(time/4)%len(monstre4)],(200,200)), (boss_x,boss_y))
                    #toutes 2 les  secondes créationnouvelle boule de feu
                    if (time+compteur_creation)%20 == 0 :
                            compteur_creation += 1
                            new_feu = {}
                            new_feu['x']  = boss_x +35
                            new_feu['y']  = boss_y+40

                            new_feu['fini'] = False
                            dx = link_x - new_feu['x']
                            dy = link_y - new_feu['y']
                            norme = math.sqrt(dx**2 + dy**2)
                            new_feu['dx'] = dx/norme
                            new_feu['dy'] = dy/norme
                            feuLIST.append(new_feu)
                            sonfeu = pygame.mixer.music.load(os.path.join(assets4, "boule-de-feu.mp3"))
                            pygame.mixer.music.play()
                    for onefeu in feuLIST :
                        onefeu['x']+= onefeu['dx']*2
                        onefeu['y']+= onefeu['dy']*2
                        if (onefeu['x'] >= 636) or (onefeu['x']<= 132) or (onefeu['y'] >= 318) or (onefeu['y']<= 79) :
                            onefeu['fini'] = True
                        elif ((onefeu['x']+20-link_x-LARG/2)**2 + (onefeu['y']+20-link_y-LARG/2)**2) <= (30)**2 and not onefeu['fini']:
                            onefeu['fini'] = True
                            barredevie-=1
                            degat=pygame.mixer.music.load(os.path.join(assets4, "degat.wav"))
                            pygame.mixer.music.play()

                    for onefeu in feuLIST :
                        if not onefeu['fini'] :
                            screen.blit(feusprite,(onefeu['x'],onefeu['y']))

                    if boss_x != boss_x1 :
                        t += 0.001
                        boss_x =t*boss_x1 + (1-t)*boss_x
                    else :
                        boss_x1 = random.randint(115,590)
                        t = 0

                    if boss_y != boss_y1 :
                        t += 0.001
                        boss_y =t*boss_y1 + (1-t)*boss_y
                    else :
                        boss_y1 = random.randint(50,245)
                        t = 0
                elif sprite_explosion<=6 :
                    if sprite_explosion == 0 :
                        sonboss.set_volume(0)
                        sonexplosion = pygame.mixer.music.load(os.path.join(assets4, "explosion.wav"))
                        pygame.mixer.music.play()

                    screen.blit(scale(explosion[int(sprite_explosion)],(100,100)),(boss_x,boss_y))
                    sprite_explosion += 0.25
                elif not avoirtriforce :
                    sonvictoireboss = pygame.mixer.music.load(os.path.join(assets4, "victoireboss.mp3"))
                    pygame.mixer.music.play()
                    avoirtriforce = True
                    triforce_x = boss_x+35
                    triforce_y = boss_y+45
                else :
                    screen.blit(scale(triforce_sprite,(30,30)),(triforce_x,triforce_y))

            #Affiche l'item recu ( magasin ou tresor )
            if afficheimage >= 0 :
                screen.blit(itemsimage[afficheimage],(200,120))


            #affiche le boost vitesse ou force
            if boostvitesse :
                police = pygame.font.SysFont("Aharoni", 30)
                zone = police.render("VITESSE X 2 : "+str(int(20-(T1-T0)))+" S ", True, BLEU)
                screen.blit(zone,(600, 380))
            if boostforce :
                police = pygame.font.SysFont("Aharoni", 30)
                zone = police.render("DEGAT X 2 : "+str(int(20-(T1force-T0force)))+" S ", True, RED)
                screen.blit(zone,(600, 359))

            if etatlink == EtatStop :
                #INVENTAIRE
                if inventaire :
                    screen.blit(inventaire_sprite, (screenWidth/2-inventaire_sprite.get_width()/2,screenHeight/2-inventaire_sprite.get_height()/2))
                    if(itemactif >= 0) :
                        a = 215
                        b = screenHeight/2-inventaire_sprite.get_height()/2+100
                        pygame.draw.rect(screen, GREEN, (a+itemactif*75, b,75, 100))

                    for i in range(0,5) :
                        a = screenWidth/2-inventaire_sprite.get_width()/2+20
                        b = screenHeight/2-inventaire_sprite.get_height()/2+100

                        if itemsbool[i] :
                            screen.blit(scale(itemssprite[i],(100,100)),(a+75*i,b))

                        else :
                            screen.blit(scale(nonitemssprite[i],(100,100)),(a+75*i,b))
                #AIDE
                if aide :
                    screen.blit(aide_sprite, (0,0))

            #GAME OVER
            if barredevie==0 :
                if not fini :
                    son1.set_volume(0)
                    sonmechant.set_volume(0)
                    sonboss.set_volume(0)
                    songameover = pygame.mixer.music.load(os.path.join(assets4, "gameover.mp3"))
                    pygame.mixer.music.play()
                    fini = True
                screen.blit(GAMEOVER,(0,0))

            #VICTOIRE
            if GAGNER :
                screen.blit(image_de_fin,(0,0))
                fini = True

    #Actualise le jeu

    clock.tick(30)
    pygame.display.flip()

#Quitte le jeu
pygame.quit()