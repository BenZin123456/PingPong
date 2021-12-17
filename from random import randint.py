from random import randint
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
background = transform.scale(image.load('desert.jpg'),(1100, 900))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x += self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed 
class Ball (GameSprite):
    def hod(self):
        self.rect.x += self.speed
        self.rect.y += self.speed        
window = display.set_mode((1100,900))
display.set_caption('Shooter')
background = transform.scale(image.load('desert.jpg'),(1100, 900))
run = True
FPS = 60
clock = time.Clock()
finish = False
score = 0
rocket = Player('raket.png', 30, 50, 450)
rocket1 = Player('raket.png', 30, 1050, 450)
shar = Ball('bol.png', 40, 550, 450)
while run:
    for i in event.get():
        if e.type == QUIT:
           run = False
        rocket.reset()
        rocket1.reset()
    time.delay(50)