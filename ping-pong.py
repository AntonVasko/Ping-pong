from random import randint
from pygame import *
import time as tm

init() #! инициализация ресурсов библиотеки
resolution = (600,700)
window = display.set_mode(resolution, SCALED, vsync=1)
display.set_caption("Ping-pong")
background = transform.scale(image.load("ping-pong_field.png"),resolution)

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,w,h,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


class Player1(GameSprite):
    def control(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y< 500:
            self.rect.y += self.speed
class Player2(GameSprite):
    def control(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y< 500:
            self.rect.y += self.speed


class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, w, h, ball_speed_x, ball_speed_y):
        super().__init__(player_image, player_x, player_y, w, h, player_speed = ball_speed_x)
        self.ball_speed_y = ball_speed_y
    def ball_control(self):
        self.rect.x += self.speed
        self.rect.y += self.ball_speed_y
        if self.rect.colliderect(player1.rect) or self.rect.colliderect(player2.rect):
            self.speed *= -1
            self.ball_speed_y *= 1
        if self.rect.y < 5 or self.rect.y > 650:
            self.ball_speed_y *= -1
#! у player1 мяч отбивается от задней грани(исправить)!!!

player1 = Player1("board.png",26,330,25,200,5)
player2 = Player2("board.png",550,330,25,200,5)
ball = Ball("ball.png",300,350,50,50,3, 3)
'''
mixer.music.load("space.ogg")
mixer.music.set_volume(0.05)
mixer.music.play()'''

font1 = font.Font(None,36)
font2 = font.Font(None,25)
font3 = font.Font(None,30)
lose = font1.render("YOU LOSE!",True,(255,0,0))
pause = font3.render("Pause...",True,(255,255,255))
restart = font2.render("Do you want to start over?Yes(y) or No(n)",True,(255,255,255))

clock = time.Clock()

finish = False
game = True
while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False                
    if finish:
        keys = key.get_pressed()
        if keys[K_r]:
            finish = False
            ball.rect.x = 300
            ball.rect.y = 350
    if finish != True:
        if ball.rect.x < 20 or ball.rect.x > 550:
            finish = True
        window.blit(background,(0,0))
        player1.reset()
        player2.reset()
        ball.reset()
        player1.control()
        player2.control()
        ball.ball_control()
    clock.tick(60)
    display.flip()