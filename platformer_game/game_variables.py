from difflib import restore
from tkinter import Button
import pygame
from pygame import mixer

mixer.init()

screen_width=1000*0.8
screen_height=1000*0.8

clock=pygame.time.Clock()
fps=60

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Platformer')

#load images
sun_img=pygame.image.load('img/sun.png')
bg_img=pygame.image.load('img/sky.png')
restart_img=pygame.image.load('img/restart_btn.png')
run =True

white=(255,255,255)
#game variables
tile_size=50*0.8
game_over=0
#load sounds
jump_fx=pygame.mixer.Sound('img/jump.wav')
game_over_fx=pygame.mixer.Sound('img/game_over.wav')
background_music=pygame.mixer.Sound('img/music.wav')

def draw_grid():
    for line in range(0,int(screen_width/tile_size)):

        pygame.draw.line(screen,(white),(0,line*tile_size),(screen_width,line*tile_size))
        pygame.draw.line(screen,(white),(line*tile_size,0),(line*tile_size,screen_width))

