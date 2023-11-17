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





win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))

background = scale(load("background.jpg"), (win_width, win_height))


player = GameSprite("hero.png", 5, win_height - 80, 5)
gyborg = GameSprite("cyborg.png", win_width - 100, win_height - 300,  2)



game = True
clock = time.Clock()
FPS = 60


mixer.init()
mixer.music.load("jungles.ogg")

mixer.music.play()


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    player.reset()
    gyborg.reset()
    display.update()

    clock.tick(FPS)