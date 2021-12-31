import pygame
import os
from bullet import Bullet
import parameters
import math
import random 

class Player:
    def __init__(self, id, WIN, is_enemy, player_type, life, x, y, photo, alive, damage):
        self.id = id
        self.WIN=WIN
        self.is_enemy = is_enemy
        self.player_type = player_type
        self.life = life
        self.x = x
        self.y = y
        self.photo = photo
        self.alive = True
        self.bullet = 0
        self.damage = damage 


    def aim(self):
        black= (0,0,0)
        mx,my = pygame.mouse.get_pos()
        mouse=[mx, my]
        if mouse[0]<self.x+300 and mouse[1]>300:
            pygame.draw.polygon(self.WIN,black, ((self.x+25,515), (self.x+25, 520), (mouse[0], mouse[1]+5),(mouse[0]-5, mouse[1])))
            aim= pygame.image.load(os.path.join("images","aim.png"))
            aim=pygame.transform.scale(aim,(65, 55))
            self.WIN.blit(aim,(mouse[0]-30,mouse[1]-30 ))

    def setBullet(self):
        
        if self.player_type == parameters.player_type[1]:
            shoot1 = pygame.image.load(os.path.join("images","bullet2.png"))
            shoot1=pygame.transform.scale(shoot1,(50, 50))
            shoot1= Bullet(shoot1, self.x, self.y,0,0, False)
            self.bullet = shoot1

        elif self.player_type == parameters.player_type[2]:
            shoot1 = pygame.image.load(os.path.join("images","arrow.png"))
            shoot1=pygame.transform.scale(shoot1,(50, 50))
            shoot1= Bullet(shoot1, self.x, self.y, 0, 0, False)
            self.bullet = shoot1

        elif  self.player_type == parameters.player_type[3]:
            shoot1 = pygame.image.load(os.path.join("images","granade.png"))
            shoot1=pygame.transform.scale(shoot1,(50, 50))
            shoot1= Bullet(shoot1, self.x, self.y, 0, 0, False)
            self.bullet = shoot1
        

    def ballpath(self):
        power= self.bullet.power
        angle= self.bullet.angle
        time= self.bullet.time
        #using suvat equations
        velX=math.cos(angle) * power # horizontal velocity
        velY= math.sin(angle) * power # vertical velocity
        distX=  velX * time  # constant velocity 
        distY= (velY * time) + ((-4.9 * (time)**2)) # -4.9 is the gravity/2

        newX= round(distX+ self.bullet.x)
        newY = round(self.bullet.y- distY)
        return (newX, newY)   #this is a tuple
    
    def findAngle(self):
        if self.is_enemy== False:
            mx,my = pygame.mouse.get_pos()
            mouse=[mx, my]
        elif self.is_enemy == True: 
            mx,my = pygame.mouse.get_pos()
            mouse=[mx, my]
        aX= self.x
        aY= self.y
        if aX == mouse[0]:
            angle=math.pi / 2
        else: 
            angle= math.atan((aY - mouse[1]) / (aX - mouse[0]))# atan give you an angle, the line will give you the angle of the player and the aming
        #pendiente ,diferencia de y / diferencia de x
        if mouse[1] > aY and mouse[0]> aX: #first cuadrantant
            angle = (math.pi * 2) -angle
        elif mouse[1] > aY and mouse[0] < aX: #second cuadrant 
            angle= math.pi + abs(angle)
        elif mouse[1] < aY and mouse[0] < aX: #third cuadrant
            angle=math.pi - abs(angle)
        elif mouse[1] < aY and mouse[0] > aX: #forth cuadrant
            angle= abs(angle)
        return angle
    
    def bulletPosition(self):
        if self.bullet.shoot == True:
            if self.bullet.y < 600 and self.bullet.x < 1200 and self.bullet.x > 0 :
                pygame.time.delay(15)
                self.bullet.time+= 0.05
                position= self.ballpath()
                self.bullet.x= position[0]
                self.bullet.y= position[1]
                #print("(", self.bullet.x, ",", self.bullet.y, ")")
            else: 
                self.bullet.shoot = False
                self.bullet.x = self.x
                self.bullet.y = self.y
                self.bullet.time= 0

    # self.WIN.blit(shoot1.image,(self.x, self.y))
    def anglePower(self):
        if self.bullet.shoot== False:
            self.bullet.shoot=True
            x= self.bullet.x
            y= self.bullet.y
            if self.is_enemy== False:
                mx,my = pygame.mouse.get_pos()
                mouse=[mx, my]
            else:
                randomX= random.randrange(self.x-300, self.x-100)
                randomY= random.randrange(self.y-150, self.y-50)
                mouse=[randomX, randomY]

            self.bullet.power = math.sqrt((mouse[1]-y)**2+ (mouse[0]-x)**2)/8
            #distance between 2 roots: square root of changing x + changing y    / ((x2-x1)+(y2-y1))**1/2
            if x == mouse[0]:
                angle=math.pi / 2
            else: 
                angle= math.atan((y - mouse[1]) / ( x - mouse[0])) # atan give you an angle, the line will give you the angle of the player and the aming
            if mouse[1] > y and mouse[0]> x: #first cuadrantant
                angle = (math.pi * 2) -angle
            elif mouse[1] > y and mouse[0] < x: #second cuadrant 
                angle= math.pi + abs(angle)
            elif mouse[1] < y and mouse[0] < x: #third cuadrant
                angle=math.pi - abs(angle)
            elif mouse[1] < y and mouse[0] > x: #forth cuadrant
                angle= abs(angle)
            self.bullet.angle = angle


    def got_hit(self):# the damge is the atribute of the player shooting
        if self.x-20 <self.bullet.x < self.x+20 and  self.y -20 < self.bullet.y < self.y -20:
            self.life -= damage
            if self.life <= 0:
                self.alive = True
            else:
                self.alive= False