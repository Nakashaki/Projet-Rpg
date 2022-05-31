import pygame
import sys
from pygame.locals import *
import random
import launch_after_combat
from pygame import mixer


player=[ 10,     #degat
        25,     #PV
        1      #magie
]





def draw_text(text, font, color, surface, locate ):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (locate)
    surface.blit(textobj, textrect)



def Pmonster (player,monster):
    
    
    #en fonction de la difficulté du monstre
    if monster==0:
        monsterHP=25
        monsterATK=2
    elif monster==1:
        monsterHP=35
        monsterATK=3


    monsterHPM=monsterHP
    playerHP=player[1]
    

    pygame.init() 
    mixer.music.load('sound/battle.wav')
    mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.10)
    def barHP(monsterHP,monsterHPM,playerHP,playerHPM):  #fonction pour créer la barre de vie
        #positionnement, epaisseur de la jauge de vie x,y,hp,epaisseur en fonction du montre ou si c'est le joueur
        #position de la barre de vie du monstre
        
        bar_position=(460,290,monsterHP,10)
        bar_back_position=(460,290,monsterHPM,10)
        
        
        #couleur de la bar de vie 
        bar_color=(111,210,46)
        back_bar_color=(230,0,0)
        
        #dessiner l'arriere de la bar
        pygame.draw.rect(screen,back_bar_color,bar_back_position)
        #dessiner la barre
        pygame.draw.rect(screen,bar_color,bar_position)
       
        #barHP du joueur 
        bar_position=(80,290,playerHP,10)
        bar_back_position=(80,290,playerHPM,10)
        pygame.draw.rect(screen,back_bar_color,bar_back_position)

        pygame.draw.rect(screen,bar_color,bar_position)
    
    


    



    #taille de l'ecran  
    res = (580,480) 
  
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption('Projet RPG')
    #implanter une image 
    image = pygame.image.load("sprites/testforet.jpg")
    playerI = pygame.image.load("sprites/Joueur.png")
    monsterI =pygame.image.load("sprites/rpgmonstre.png")
    #choisir le positionnement de la photo,ou des images de personnages
    def picture():
        screen.blit(image, ((580*0),(480*0)))
       
    


    #definition des couleurs  
    color = (255,255,255) 
  
    color_light = (170,170,170) 
  
    color_dark = (100,100,100) 
    color_text=(240,195,0)
  
    width = screen.get_width() 
  
    height = screen.get_height() 
    #choisir la taille de l'ecriture  
    smallfont = pygame.font.SysFont('Corbel',35)
    smallfont2=pygame.font.SysFont('Corbel',33) 
    smallfont3=pygame.font.SysFont('Franklin Gothic',15)
    smallfont4=pygame.font.SysFont('Corbel',25)
    

    #l'ecriture et la taille du text des boutons  
    
    textbox=smallfont3.render('Choisi la compétence que tu veux utiliser',True,color)   #cas particulier car c'est un texte qui doit changer
    
    #fonction qui ecris les text dans les boutons, avec la police, couleur, la position du texte dans la page
   
        
    



    #variable qui permet de créer une "clock" pour ce soigner 
    turn=0
    stun=0
    end=True
    


    #creation de la boucle pour lancer la page 
    while end: 
        
      
        for ev in pygame.event.get(): 
            
        
          
            if ev.type == pygame.QUIT: 
                end=False 
              
            #l'action de cliquer sur le bouton de la sourie 
            if ev.type == pygame.MOUSEBUTTONDOWN: 

                ATKE="Le monstre attaque et t'inflige " + str(monsterATK) + " degats"   #variable pour afficher les degats du monstre
              
            
                #action qui permet quand tu clique sur le bouton de quitter
                if width/1.4 <= mouse[0] <= width/1.4+140 and height/1.2 <= mouse[1] <= height/1.2+40:    #quit
                    pygame.quit() 
                if width/20 <= mouse[0] <= width/20+140 and height/1.4 <= mouse[1] <= height/1.4+40:       #attaquer
                    monsterHP=monsterHP-player[0]
                    textbox=smallfont3.render(ATKE,True,(0,0,0))
                    turn=turn+1
                    if playerHP<=0:
                        endscreen(0)
                    elif monsterHP<=0:
                        endscreen(1)
                    if stun>=1:
                        textbox=smallfont3.render("Le monstre est STUN, il n'attaquera pas",True,(0,0,0))
                        
                        stun=stun-1
                    else:
                        playerHP=playerHP-monsterATK
                        textbox=smallfont3.render(ATKE,True,(0,0,0))
                if width/20 <= mouse[0] <= width/20+140 and height/1.2 <= mouse[1] <= height/1.2+40:   #potion
                    if turn>=0:
                        playerHP=playerHP+5     #si le joueur a attendu suffisament il peut ce soigner sinon il ne ce passe rien
                        turn=-3
                        if stun>=1:
                            textbox=smallfont3.render("Le monstre est STUN, il n'attaquera pas",True,(0,0,0))
                            stun=stun-1
                            
                        else:
                            playerHP=playerHP-monsterATK
                            
                            textbox=smallfont3.render(ATKE,True,(0,0,0))
                    else :
                        playerHP=playerHP
                if width/2.6 <= mouse[0] <= width/2.6+140 and height/1.4 <= mouse[1] <= height/1.4+40:    #magie
                    stun=stun+1
                    textbox=smallfont3.render("Le monstre est STUN pendant 2 tours",True,(0,0,0))
                if width/1.4 <= mouse[0] <= width/1.4+140 and height/1.4 <= mouse[1] <= height/1.4+40:    #defence
                    playerHP=playerHP-(monsterATK-2)
                    ATKE="Le monstre attaque et t'inflige " + str(monsterATK-2) + " degats"
                    textbox=smallfont3.render(ATKE,True,(0,0,0))
                elif monsterHP<=0:
                        endscreen(1,screen)
            if ev.type == KEYDOWN :
                if ev.key == K_i:
                    end=False
                
                    


                    
                      
        #remplir l'image d'une couleur
        screen.fill((60,25,60))
        picture()
        screen.blit(playerI,(50,185))
        screen.blit(monsterI,(425,185))
        barHP(monsterHP,monsterHPM,playerHP,player[1])
    
        pygame.draw.rect(screen,color_text,(20,10,205,30))
        screen.blit(textbox,(20,20))
    
        #avoir la position de la souris dans une variable
        mouse = pygame.mouse.get_pos() 
      
    
        #le bouton quit
        if width/1.4 <= mouse[0] <= width/1.4+140 and height/1.2 <= mouse[1] <= height/1.2+40: 
            pygame.draw.rect(screen,color_light,[width/1.4,height/1.2,140,40]) 
          
        else: 
            pygame.draw.rect(screen,color_dark,[width/1.4,height/1.2,140,40]) 
        draw_text('Abandon',smallfont2,color,screen,(width/1.5+40,height/1.19))


    
        #le bouton attaquer
        if width/20 <= mouse[0] <= width/20+140 and height/1.4 <= mouse[1] <= height/1.4+40: 
            pygame.draw.rect(screen,color_light,[width/20,height/1.4,140,40]) 
          
        else: 
            pygame.draw.rect(screen,color_dark,[width/20,height/1.4,140,40])
        #poistionner le texte dans le rectangle    
        draw_text('Attaquer',smallfont2,color,screen,(width/300+40,height/1.39))
      
        #bouton magie

        if width/2.6 <= mouse[0] <= width/2.6+140 and height/1.4 <= mouse[1] <= height/1.4+40: 
            pygame.draw.rect(screen,color_light,[width/2.6,height/1.4,140,40]) 
          
        else: 
            pygame.draw.rect(screen,color_dark,[width/2.6,height/1.4,140,40])
        
        draw_text('Magie',smallfont,color,screen,(width/2.6+30,height/1.39))

        #bouton defence 

        if width/1.4 <= mouse[0] <= width/1.4+140 and height/1.4 <= mouse[1] <= height/1.4+40: 
            pygame.draw.rect(screen,color_light,[width/1.4,height/1.4,140,40]) 
          
        else: 
            pygame.draw.rect(screen,color_dark,[width/1.4,height/1.4,140,40])
        
        draw_text('Défense',smallfont,color,screen,(width/1.49+30,height/1.39))

        #le bouton potion
        if width/20 <= mouse[0] <= width/20+140 and height/1.2 <= mouse[1] <= height/1.2+40: 
            pygame.draw.rect(screen,color_light,[width/20,height/1.2,140,40]) 
          
        else: 
            pygame.draw.rect(screen,color_dark,[width/20,height/1.2,140,40])
        
        draw_text('Potion',smallfont,color,screen,(width/35+40,height/1.19))


        #le bouton fuir
        '''if width/2.6 <= mouse[0] <= width/2.6+140 and height/1.2 <= mouse[1] <= height/1.2+40: 
            pygame.draw.rect(screen,color_light,[width/20,height/1.2,140,40]) 
          
        else: 
            pygame.draw.rect(screen,color_dark,[width/2.6,height/1.2,140,40])
        screen.blit(run,(width/2.6+40,height/1.19))'''
        pygame.display.update() 
    #mettre a jour l'image  
        def endscreen(event):
            
            mouse1 = pygame.mouse.get_pos() 
            if event==0:  #si le joueur perd
                while True:
                    screen.fill((0,0,0))
                    
                    for ev in pygame.event.get(): 
                        if ev.type == pygame.QUIT:
                            pygame.quit()
                        if ev.type == KEYDOWN :
                            if ev.key == K_ESCAPE:
                                pygame.quit()

                    draw_text('Tu as perdu ce combat ! Mais pas la guerre reviens affronter ce monstre plus tard !',smallfont,color,screen,(20,20))
                    draw_text('Pour quitter appuie sur la touche echape !',smallfont4,color,screen,(30,100))
                    pygame.display.update()
            elif event==1: #si le joueur gagne
                while True:
                    screen.fill((0,0,0))
                    
                    for ev in pygame.event.get(): 
                        if ev.type == pygame.QUIT:
                            pygame.quit()
                        if ev.type == KEYDOWN :
                            if ev.key == K_ESCAPE:
                                mixer.music.load('sound/background.wav')
                                mixer.music.play(-1)
                                pygame.mixer.music.set_volume(0.10)
                                pygame.quit()
                                launch_after_combat.after_combat()


                    draw_text('Tu as gagné ce combat trop fort !',smallfont,color,screen,(30,20))
                    draw_text('Pour quitter appuie sur la touche echape !',smallfont4,color,screen,(30,100))
                    
                    pygame.display.update()