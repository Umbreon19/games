#source activate game to run
import pygame
from pygame.constants import QUIT
pygame.init()
clock = pygame.time.Clock()
FPS= 60
#game window

BOTTOM_PANEL = 150
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400 + BOTTOM_PANEL

ACTION_IDLE = 0 
ACTION_ATK = 1
ACTION_HURT = 2
ACTION_DEATH =3

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Battle')

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
    draw_text(f'{knight.name} HP : {knight.hp}', font,red, 100, SCREEN_HEIGHT-BOTTOM_PANEL+10 )



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
            if self.action == ACTION_ATK:
                self.idle()
        
    def draw(self):
        screen.blit(self.image, self.rect)

    def attack(self):
        if self.action != ACTION_ATK:
            self.action = ACTION_ATK
            self.frame_index = 0
            pygame.display.set_caption('Attack')

    def idle(self):
        self.action = ACTION_IDLE
        pygame.display.set_caption('Battle')


knight =  Fighter(200, 260, 'Knight', 30, 10, 3)
bandit1 = Fighter(550, 270,'Bandit', 20, 6, 1)
bandit2 = Fighter(700, 270,'Bandit', 20, 6, 1)
bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)
run= True

while run:
    clock.tick(FPS)
    draw_bg()
    draw_panel()
    knight.update()
    knight.draw()
    for bandit in bandit_list: 
        bandit.update()
        bandit.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
        if event.type == pygame.KEYDOWN:
            if event.mod == pygame.KMOD_NONE:
                if event.key == pygame.K_j:
                    knight.attack()
    pygame.display.update()        

pygame.quit()
