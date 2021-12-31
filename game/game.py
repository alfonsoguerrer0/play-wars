import pygame
import os
from player import Player
from parameters import player_type
import parameters
import time

class Game:
    def __init__(self, background, level):
        WIDTH , HEIGHT= 1200,600
        self.WHITE=(255,255,255)
        self.WIN = pygame.display.set_mode((WIDTH , HEIGHT))#display the window
        self.players = []
        self.enemies = []
        self.background = background
        self.level = level
        self.initial_x_p = 100
        self.initial_y_p = 500
        self.initial_x_e = 900
        self.initial_y_e = 500
        self.life_placing = 490
        self.shooter_aiming = 0
        self.playerTurn= True

    def draw_player(self, player):
        if player.is_enemy == False:
            self.WIN.blit(player.photo,(self.initial_x_p, self.initial_y_p))
            #self.WIN.blit(player.life_picture,(self.initial_x_p, self.life_placing))
            self.initial_x_p += 80
        elif player.is_enemy == True:
            self.WIN.blit(player.photo,(self.initial_x_e, self.initial_y_e))
            #self.WIN.blit(player.life_picture,(self.initial_x_e, self.life_placing))
            self.initial_x_e += 60

    def set_players(self):
            playerPNG= pygame.image.load(os.path.join("images","player.png"))
            playerImage=pygame.transform.scale(playerPNG,(65, 55))
            player1= Player(0, self.WIN, False, player_type[1], 100, self.initial_x_p, self.initial_y_p, playerImage, True, 10)
            player1.setBullet()
            self.draw_player(player1)

            playerPNG= pygame.image.load(os.path.join("images","archer.png"))
            playerImage=pygame.transform.scale(playerPNG,(65, 55))
            player2= Player(1, self.WIN, False, player_type[2], 100, self.initial_x_p, self.initial_y_p, playerImage, True, 10)
            player2.setBullet()
            self.draw_player(player2)

            playerPNG= pygame.image.load(os.path.join("images","armor.png"))
            playerImage=pygame.transform.scale(playerPNG,(65, 55))
            player3= Player(2, self.WIN, False, player_type[3], 100, self.initial_x_p, self.initial_y_p, playerImage, True, 10)
            player3.setBullet()
            self.draw_player(player3)

            enemyPNG=  pygame.image.load(os.path.join("images","enemy1.png"))
            enemyImage=pygame.transform.scale(enemyPNG,(65, 55))
            enemy1= Player(0, self.WIN, True, player_type[1], 100, self.initial_x_e, self.initial_y_e, enemyImage, True, 10)
            enemy1.setBullet()
            self.draw_player(enemy1)
            
            enemyPNG=  pygame.image.load(os.path.join("images","enemy1.png"))
            enemyImage=pygame.transform.scale(enemyPNG,(75, 55))
            enemy2= Player(1, self.WIN, True, player_type[2], 100, self.initial_x_e, self.initial_y_e, enemyImage, True, 10)
            enemy2.setBullet()
            self.draw_player(enemy2)

            self.players.append(player1)
            self.players.append(player2)
            self.enemies.append(enemy1)
            self.enemies.append(enemy2)
            self.players.append(player3)


    
    def draw_window(self):
        self.WIN.fill(self.WHITE) #give the window a colour (blank in this case). look RGP to change it  to another colour
        #use to update any change, if you dont yopu will not see any changes  when you run it
        self.WIN.blit(self.background,(0,0))



    def redraw_window(self):
        self.WIN.fill(self.WHITE) 
        self.WIN.blit(self.background,(0,0))
        for player in self.players:
            self.WIN.blit(player.photo,(player.x, player.y))
            if player.id == self.shooter_aiming  and player.bullet.shoot == True:
                self.WIN.blit(player.bullet.image,(player.bullet.x, player.bullet.y))
            
        for enemy in self.enemies:
            self.WIN.blit(enemy.photo,(enemy.x, enemy.y))
            if enemy.bullet.shoot == True  and enemy.id == self.shooter_aiming:
                self.WIN.blit(enemy.bullet.image,(enemy.bullet.x, enemy.bullet.y))

            

    def playerChoice(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.shooter_aiming >0 :
            self.shooter_aiming -= 1
            pygame.time.delay(100)
        elif keys[pygame.K_RIGHT] and self.shooter_aiming <2 :
            self.shooter_aiming += 1
            pygame.time.delay(100)
        



    def got_hit(self):# the damge is the atribute of the player shooting
        if self.playerTurn == True:
            for enemy in self.enemies:
                if enemy.x-50 < self.players[self.shooter_aiming].bullet.x < enemy.x+50 and  enemy.y - 50 < self.players[self.shooter_aiming].bullet.y < enemy.y +50:
                    enemy.life -= self.players[self.shooter_aiming].damage
                    print("nice shoot",enemy.life)
                    if enemy.life <= 0:
                        enemy.alive = True
                    else:
                        enemy.alive= False

        elif self.playerTurn == False:
            for player in self.players:
                #if player.x-50 < self.enemies[self.shooter_aiming].bullet.x < enemy.x+50 and  enemy.y - 50 < self.players[self.shooter_aiming].bullet.y < enemy.y +50: 
                    



    def animation():
        a=q


