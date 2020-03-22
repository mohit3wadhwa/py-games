import pgzrun
from random import randint
'''
First bug is an actor(object) and the 2nd bug in " " is name of the image.
image should be kept in images folder, else code won't work.
'''
bug = Actor("bug")
count = 0
def draw():
    screen.clear()
    screen.draw.text("Score: " + str(count) + "    -Hit the Bug-", topleft=(10, 10))
    bug.draw()

def place_bug():
    bug.x = randint(100,450)
    bug.y = randint(200,500)

def on_mouse_down(pos):
    global count
    if bug.collidepoint(pos):
        count += 1
        print("Good Shot!")
    else:
        quit()
    screen.draw.text("Score: " + str(count), topleft=(10, 10))
    place_bug()

place_bug()
pgzrun.go()
