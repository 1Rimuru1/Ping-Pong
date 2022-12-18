from pygame import *
#mixer.init()
#mixer.music.load("space.ogg")
font.init()
from random import randint
font1 = font.Font(None, 36)
window  = display.set_mode((700,500))
display.set_caption("Шутер")

background = transform.scale(
    image.load("Kosmo.jpg.jpg"),
    (700, 500)
)


finish = False
clock = time.Clock()
FPS = 999

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (100, 100))
        self.speed = 4
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
class Player2(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

speed_y = 3
speed_x = 3

win_width = 700
win_height = 500

ball = GameSprite('asteroid.png', 20, 290, 200)
player2 = Player2('rocket.png', 20, 600, 400)
player = Player('rocket.png', 20, 30, 400)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        if ball.rect.y > 5:
            speed_y *= -1
        if ball.rect.y < 400:
            speed_y *= -1
        if ball.rect.x > 5:
            #проигрыш 1
            pass
        if ball.rect.x < 620:
            #проигрыш 2
            pass
        player.reset()
        player.update()
        player2.reset()
        player2.update()
        ball.reset()
        ball.update()
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x > win_width - 50 or ball.rect.x < 0:
            speed_x *= -1
        clock.tick(FPS)
        display.update()