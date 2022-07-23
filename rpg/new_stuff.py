#source activate game to run
import random
import pygame
from pygame.constants import QUIT
pygame.init()
clock = pygame.time.Clock()
FPS= 60
#game window

BOTTOM_PANEL = 150
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400 + BOTTOM_PANEL

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Battle')

#def variables
current_fighter = 1
total_fighters = 3
action_cooldown = 0
action_wait_time = 90

#Fonts!
font =  pygame.font.SysFont('Times New Roman', 26)
red = (255, 0,0)
green = (0, 255, 0)

#to keep the window running make sure to load assets outside of game loop
background_img=pygame.image.load('rpg/Assets/Background/background.png').convert_alpha()

panel_img=pygame.image.load('rpg/Assets/icons/panel.png').convert_alpha()


def draw_text(text,font,text_color, x, y):
    img = font.render(text, True,text_color )
    screen.blit(img, (x, y))


def draw_bg():
    screen.blit(background_img,(0,0))


def draw_panel():
    screen.blit(panel_img,(0,SCREEN_HEIGHT-BOTTOM_PANEL))
    draw_text(f'{knight.name} HP : {knight.hp}', font, red, 100, SCREEN_HEIGHT-BOTTOM_PANEL+10 )
    for count, i in enumerate(bandit_list):
        draw_text(f'{i.name} HP : {i.hp}', font, red, 550, (SCREEN_HEIGHT-BOTTOM_PANEL+10)+count*60)


class Fighter():
    """class Fighter 
    """
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp =  max_hp
        self.hp = max_hp
        self.strength =  strength
        self.start_potions =  potions
        self.potions = potions
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0 # 0: idle 1:atk 2:hurt 3:death
        self.update_time = pygame.time.get_ticks()
        #idle
        temp_list = []
        for i in range (8):
            img = pygame.image.load(f'rpg/Assets/{self.name}/Idle/{i}.png')
            img = self.image = pygame.transform.scale(img,(img.get_width()*3, img.get_height()*3 ))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        #attack    
        temp_list = []
        for i in range (8):
            img = pygame.image.load(f'rpg/Assets/{self.name}/Attack/{i}.png')
            img = self.image = pygame.transform.scale(img,(img.get_width()*3, img.get_height()*3 ))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (2):
            img = pygame.image.load(f'rpg/Assets/{self.name}/Hurt/{i}.png')
            img = self.image = pygame.transform.scale(img,(img.get_width()*3, img.get_height()*3 ))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (10):
            img = pygame.image.load(f'rpg/Assets/{self.name}/Death/{i}.png')
            img = self.image = pygame.transform.scale(img,(img.get_width()*3, img.get_height()*3 ))
            temp_list.append(img)
        self.animation_list.append(temp_list)        
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        animation_cooldown = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
        

    def attack(self,target):
        rand = random.randint(-5,5)
        damage = self.strength + rand
        target.hp -= damage
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        
    def draw(self):
        screen.blit(self.image, self.rect)
    

    def idle(self):
        self.action = ACTION_IDLE
        pygame.display.set_caption('Battle')


class HealthBar():
    def __init__(self, x, y, hp, max_hp ):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw (self, hp):
        self.hp = hp
        ratio = self.hp/self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20)) 
        pygame.draw.rect(screen, green, (self.x, self.y, 150*ratio, 20)) 

knight =  Fighter(200, 260, 'Knight', 30, 10, 3)
bandit1 = Fighter(550, 270,'Bandit', 20, 6, 1)
bandit2 = Fighter(700, 270,'Bandit', 20, 6, 1)
bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)
knight_health_bar = HealthBar(100, SCREEN_HEIGHT-BOTTOM_PANEL+40, knight.hp, knight.max_hp )
bandit1_health_bar = HealthBar(550, SCREEN_HEIGHT-BOTTOM_PANEL+40, bandit1.hp, bandit1.max_hp )
bandit2_health_bar = HealthBar(550, SCREEN_HEIGHT-BOTTOM_PANEL+100, bandit2.hp, bandit2.max_hp )

run= True

while run:
    clock.tick(FPS)
    draw_bg()
    draw_panel()
    knight_health_bar.draw(knight.hp)
    bandit1_health_bar.draw(bandit1.hp)
    bandit2_health_bar.draw(bandit2.hp)
    knight.update()
    knight.draw()
    if knight.alive == True:
        if current_fighter == 1:
            action_cooldown +=1
            if action_cooldown >= action_wait_time:
                knight.attack(bandit1)
                current_fighter += 1
                action_cooldown = 0
    for bandit in bandit_list: 
        bandit.update()
        bandit.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
    pygame.display.update()        

pygame.quit()
