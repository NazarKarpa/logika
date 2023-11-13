import time

from pygame import *

window = display.set_mode((700, 500))

display.set_caption("Топ")


img = image.load("background.png")
background = transform.scale(img, (700, 500))


clock = time.Clock()
FPS = 60
SPEED = 6

sprite = transform.scale(image.load("sprite1.png"), (70, 70))

x1 = 200
y1 = 400

x2 = 400
y2 = 400


sprite1 = transform.scale(image.load("sprite2.png"), (70, 70))




game = True

while game:
    window.blit(background, (0, 0))
    window.blit(sprite, (x1, y1))
    window.blit(sprite1, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            game = False

    keys_presed = key.get_pressed()

    if keys_presed[K_LEFT] and x1 > 5:
        x1 -= SPEED
    if keys_presed[K_RIGHT] and x1 < 635:
        x1 += SPEED
    if keys_presed[K_DOWN] and y1 < 430:
        y1 += SPEED
    if keys_presed[K_UP] and y1 > 5:
        y1 -= SPEED
    if keys_presed[K_a] and x2 > 5:
        x2 -= SPEED
    if keys_presed[K_d] and x2 < 635:
        x2 += SPEED
    if keys_presed[K_s] and y2 < 430:
        y2 += SPEED
    if keys_presed[K_w] and y2 > 5:
        y2 -= SPEED


    display.update()
    clock.tick(FPS)

