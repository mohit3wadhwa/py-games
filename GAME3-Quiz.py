import pgzrun
from random import randint
import time
'''
First bug is an actor(object) and the 2nd bug in " " is name of the image.
image should be kept in images folder, else code won't work.
'''

WIDTH  = 1280
HEIGHT = 720

main_box    =  Rect(0, 0, 850, 240)
timer_box   =  Rect(0, 0, 240, 240)
answer_box1 =  Rect(0, 0, 550, 165)
answer_box2 =  Rect(0, 0, 550, 165)
answer_box3 =  Rect(0, 0, 550, 165)
answer_box4 =  Rect(0, 0, 550, 165)


main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(685, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(685, 538)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
score = 0
time_left = 5
game_over_flag = False

q1 = ["India's Capital?", "Bangalore","Mumbai","New Delhi","Kolkata",3]
q2 = ["USA's Capital?", "DC","Phoenix","SFO","Chicago",1]
q3 = ["UK's Capital?", "Brighton","Burgess Hill","Eastbourne","London",4]
q4 = ["Australia's Capital?", "Sydney","Melbourne","Canberra","Adelaide",3]

questions = [q1, q2, q3, q4]
question = questions.pop(0)
lengthy = len(questions)


def draw():
    screen.fill("dim grey")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")

    screen.draw.textbox(str(time_left), timer_box, color=("black"))
    screen.draw.textbox(question[0], main_box, color=("black"))

    index  = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index += 1

def game_over(var):
    global game_over_flag
    global time_left
    # if var == 'Y':
    #     question[0] = "Game Over! Your Final score is: " + str(score)
    #     game_over_flag = True
    # else:
    #     question[0] = "You are a winner! Your Final Score is: " + str(score)
    
    question[0] = "Game Over! Your Final score is: " + str(score)

    for i in range(1,6):
        question[i] = "-"
    time_left = 0


def correct_answer():
    global score
    global time_left
    global question
  
    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 5
    else:
        game_over("N")

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if question[5] == index:
                correct_answer()
            else:
                game_over("Y")
        index += 1


def update_time_left():
    global game_over_flag
    global time_left
    if time_left != 0:
        time_left -= 1
    else:
       game_over("Y")

clock.schedule_interval(update_time_left, 1.0)
pgzrun.go()
