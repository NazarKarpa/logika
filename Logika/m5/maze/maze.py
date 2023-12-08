#створи гру "Лабіринт"!
from pygame import *
from pygame.sprite import collide_rect
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, rect_x, rect_y, playeer_speed):
        super().__init__()
        self.image = scale(load(player_image), (65, 65))
        self.speed = playeer_speed


        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed


class Enemy(GameSprite):
    def __init__(self, player_image, rect_x, rect_y, playeer_speed, min_x):
        super().__init__(player_image, rect_x, rect_y, playeer_speed)
        self.min_x = min_x

        self.direction = "left"
    direction = "left"
    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        if self.rect.x <= self.min_x:
            self.direction = 'right'
        elif self.rect.x >= win_width - 80:
            self.direction = "left"

class Wall(sprite.Sprite):
    def __init__(self, wall_x, wall_y, wall_wight, wall_height):
        super().__init__()
        self.widht = wall_wight
        self.height = wall_height

        self.image = Surface((self.widht, self.height))
        self.image.fill((1,250,0))

        self.rect = self.image.get_rect()

        self.rect.x = wall_x

        self.rect.y = wall_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))

background = scale(load("background.jpg"), (win_width, win_height))

wall_player1 = Wall(0, 0, 2500, 20)
wall_player2 = Wall(250, 0, 20, 350)
wall_player3 = Wall(120, 200, 20, 350)
wall_player4 = Wall(430, 200, 20, 350)
wall_player5 = Wall(430, 300, 120, 20)
wall_player6 = Wall(700, 0, 20, 2002)
wall_player6 = Wall(700, 700, 2000, 27)

player = Player("hero.png", 5, win_height - 80, 5)
gyborg = Enemy("cyborg.png", win_width - 100, win_height - 300,  1.2, 500)
final = GameSprite("treasure.png", win_width - 80, win_height - 80, 0)
gyborg2 = Enemy("cyborg.png", win_width - 150, win_height - 150,  3, 450)


game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()

f = font.Font(None, 70)
win = f.render("You Win", True, (255,215,0))
lose = f.render("You lose", True, (255,0,0))

mixer.init()
mixer.music.load("jungles.ogg")

mixer.music.play()

money_sound = mixer.Sound("money.ogg")
kick_sound = mixer.Sound("kick.ogg")
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:

        window.blit(background, (0, 0))
        wall_player1.reset()
        wall_player2.reset()
        wall_player3.reset()
        wall_player4.reset()
        wall_player5.reset()
        wall_player6.reset()
        player.reset()
        gyborg.reset()
        final.reset()
        gyborg2.reset()

        gyborg2.update()
        gyborg.update()
        player.update()

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win,(200,200))
            money_sound.play()
        if sprite.collide_rect(player, gyborg) or sprite.collide_rect(player, wall_player1) or sprite.collide_rect(player, wall_player2) or sprite.collide_rect(player, wall_player3) or sprite.collide_rect(player, gyborg2) or sprite.collide_rect(player, wall_player5):

            finish = True
            window.blit(lose,(200,200))
            kick_sound.play()


    display.update()

    clock.tick(FPS)