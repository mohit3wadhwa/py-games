import pgzrun

import keyboard
from random import randint
'''
First bug is an actor(object) and the 2nd bug in " " is name of the image.
image should be kept in images folder, else code won't work.
'''
man  = Actor("man")
man.pos = 100, 100
coin = Actor("coin")
coin.pos = 300, 300

game_over = False

WIDTH  = 500
HEIGHT = 500

count = 0
def draw():
    screen.clear()
    screen.draw.text("Coin: " + str(count) + "  |  Collect the Coin", topleft=(10, 10))
    man.draw()
    coin.draw()

    if game_over:
        screen.fill("red")
        screen.draw.text("GAME OVER \nTotal Coins collected: " + str(count), topleft=(10, 10))


def place_coin():
    coin.x = randint(30, (WIDTH  - 30))
    coin.y = randint(30, (HEIGHT - 30))

def time_up():
    global game_over
    game_over = True

def update():
    global count

    if keyboard.is_pressed('left'):
        man.x = man.x - 5
    elif keyboard.is_pressed('right'):
        man.x = man.x + 5
    elif keyboard.is_pressed('up'):
        man.y = man.y - 5
    elif keyboard.is_pressed('down'):
        man.y = man.y + 5

    coin_collected = man.colliderect(coin)
    
    if coin_collected:
        count += 1
        place_coin()

clock.schedule(time_up, 10.0)
place_coin()

pgzrun.go()
