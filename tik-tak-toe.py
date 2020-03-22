import random
import tkinter as tk
from tkinter import messagebox

top = tk.Tk()

top.title(string="Welcome to TIC-TAC-TOC!!!")

flag = 0

def get_E2_name():
	return E2.get()

def get_E1_name():
	return E1.get()

def roll_coin():
	whos_turn = random.randint(0, 1)
	if whos_turn == 0:
		first_turn = 'X'
	else:
		first_turn = 'O'
	return first_turn

def get_name():
	whos_turn = random.randint(0, 1)
	if whos_turn == 0:
		first_turn = get_E1_name()
	else:
		first_turn = get_E2_name()
	return first_turn


def get_entry_val():
	global player
	global flag
	b1.config(state="active")
	b2.config(state="active")
	b3.config(state="active")
	b4.config(state="active")
	b5.config(state="active")
	b6.config(state="active")
	b7.config(state="active")
	b8.config(state="active")
	b9.config(state="active")

	block_dict[1] = "btn1_text"
	block_dict[2] = "btn2_text"
	block_dict[3] = "btn3_text"
	block_dict[4] = "btn4_text"
	block_dict[5] = "btn5_text"
	block_dict[6] = "btn6_text"
	block_dict[7] = "btn7_text"
	block_dict[8] = "btn8_text"
	block_dict[9] = "btn9_text"

	btn1_text.set("")
	btn2_text.set("")
	btn3_text.set("")
	btn4_text.set("")
	btn5_text.set("")
	btn6_text.set("")
	btn7_text.set("")
	btn8_text.set("")
	btn9_text.set("")

	if get_E1_name() == '' or get_E2_name() == '' :
		messagebox.showinfo("Error", "Please Enter Player Names!")
		E1.focus_set()
	elif get_E1_name() != '' and get_E2_name() != '' :
		lab_var.set(player)
		lab_var2.set("Next Turn:")
	# if flag == 0:
	# 	if player == 'X' and variable1.get() == 'X':
	# 		lab_var2.set(get_E1_name() + " plays X")
	# 	elif player == 'X' and variable1.get() == 'O':
	# 		lab_var2.set(get_E1_name() + " plays O")
	# 	elif player == 'O' and variable1.get() == 'X':
	# 	    lab_var2.set(get_E2_name() + " plays X")
	# 	else:
	# 	    lab_var2.set(get_E2_name() + " plays O")
	# 	flag = 1



def reset_val():
	global count1, count2, player
	b1.config(state="disabled")
	b2.config(state="disabled")
	b3.config(state="disabled")
	b4.config(state="disabled")
	b5.config(state="disabled")
	b6.config(state="disabled")
	b7.config(state="disabled")
	b8.config(state="disabled")
	b9.config(state="disabled")

	block_dict[1] = "btn1_text"
	block_dict[2] = "btn2_text"
	block_dict[3] = "btn3_text"
	block_dict[4] = "btn4_text"
	block_dict[5] = "btn5_text"
	block_dict[6] = "btn6_text"
	block_dict[7] = "btn7_text"
	block_dict[8] = "btn8_text"
	block_dict[9] = "btn9_text"

	btn1_text.set("")
	btn2_text.set("")
	btn3_text.set("")
	btn4_text.set("")
	btn5_text.set("")
	btn6_text.set("")
	btn7_text.set("")
	btn8_text.set("")
	btn9_text.set("")
	E1.delete(0, 'end')
	E2.delete(0, 'end')
	E1.focus_set()
	lab_var.set("")
	lab_var2.set("")
	count1 = 0
	count2 = 0
	lab_var_pl1.set(count1)
	lab_var_pl2.set(count2)
	flag = 0

la_dt = tk.Label(top, text="Player Names:")
la_dt.grid(row=0, column=0)

lb3 = tk.Label(top, text="Scoreboard:")
lb3.grid(row=0, column=2)


variable1 = tk.StringVar(top)
variable1.set("Plays X") # default value
w = tk.OptionMenu(top, variable1, "Plays X", "Plays O")
w.grid(row=1, column=1)

E1 = tk.Entry(top)
E1.focus_set()
E1.grid(row=1, column=0)

variable2 = tk.StringVar(top)
variable2.set("Plays O") # default value
w = tk.OptionMenu(top, variable2, "Plays X", "Plays O")
w.grid(row=2, column=1)

E2 = tk.Entry(top)
E2.grid(row=2, column=0)

count1 = 0
count2 = 0
lab_var_pl1 = tk.StringVar()
lab_var_pl1.set(count1)
lbpl1 = tk.Label(top, textvariable=lab_var_pl1)
lbpl1.grid(row=1, column=2)

lab_var_pl2 = tk.StringVar()
lab_var_pl2.set(count2)
lbpl2 = tk.Label(top, textvariable=lab_var_pl2)
lbpl2.grid(row=2, column=2)


player = roll_coin()
lab_var = tk.StringVar()
#lab_var.set(player)
lab_var.set("")

play_btn = tk.Button(top, text="Play", width=10, height=2, command=lambda: get_entry_val())
play_btn.grid(row=3, column=1)

reset_btn = tk.Button(top, text="Reset", width=10, height=2, command=lambda: reset_val())
reset_btn.grid(row=4, column=1)

#player = roll_coin()
#player = ""
player_name = get_name()

lab_var2 = tk.StringVar()
#lab_var2.set("")
lx = tk.Label(top, textvariable=lab_var2)
lx.grid(row=5, column=0)

l2 = tk.Label(top, textvariable=lab_var, width=10)
l2.grid(row=5, column=1)

block_dict = {
			  1: "btn1_text", 2: "btn2_text", 3: "btn3_text",
			  4: "btn4_text", 5: "btn5_text", 6: "btn6_text",
			  7: "btn7_text", 8: "btn8_text", 9: "btn9_text"
			  }

list2 = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9']


	#print("play is: " + play)
	global player, player_name
	get_index = list2.index(var) + 1
	globals()[var].config(state="disabled")
	if play == 'X':
		globals()[block_dict[get_index]].set("X")
		block_dict[get_index] = 'X'
		player = "O"
		lab_var.set(player)
		#lab_var2.set(get_E2_name())
	elif play == 'O':
		globals()[block_dict[get_index]].set("O")
		block_dict[get_index] = 'O'
		player = "X"
		lab_var.set(player)
		#lab_var2.set(get_E1_name())
	else:
		print("Value being passed other than X, O")

	win_status = check_win()

	if win_status == True:
		b1.config(state="disabled")
		b2.config(state="disabled")
		b3.config(state="disabled")
		b4.config(state="disabled")
		b5.config(state="disabled")
		b6.config(state="disabled")
		b7.config(state="disabled")
		b8.config(state="disabled")
		b9.config(state="disabled")
		global count1, count2
		if play == 'X':
			#lab_var2.set(get_E1_name())
			count1 = count1 + 1
			lab_var_pl1.set(count1)
		elif play == 'O':
			#lab_var2.set(get_E2_name())
			count2 = count2 + 1
			lab_var_pl2.set(count2)

		lab_var.set(play + " Wins.")
		lab_var2.set("")



btn1_text = tk.StringVar()
btn2_text = tk.StringVar()
btn3_text = tk.StringVar()
btn4_text = tk.StringVar()
btn5_text = tk.StringVar()
btn6_text = tk.StringVar()
btn7_text = tk.StringVar()
btn8_text = tk.StringVar()
btn9_text = tk.StringVar()

btn1_text.set("")
btn2_text.set("")
btn3_text.set("")
btn4_text.set("")
btn5_text.set("")
btn6_text.set("")
btn7_text.set("")
btn8_text.set("")
btn9_text.set("")

b1 = tk.Button(top, textvariable=btn1_text, width=22, height=12, command=lambda: callback("b1", player))
b2 = tk.Button(top, textvariable=btn2_text, width=22, height=12, command=lambda: callback("b2", player))
b3 = tk.Button(top, textvariable=btn3_text, width=22, height=12, command=lambda: callback("b3", player))
b4 = tk.Button(top, textvariable=btn4_text, width=22, height=12, command=lambda: callback("b4", player))
b5 = tk.Button(top, textvariable=btn5_text, width=22, height=12, command=lambda: callback("b5", player))
b6 = tk.Button(top, textvariable=btn6_text, width=22, height=12, command=lambda: callback("b6", player))
b7 = tk.Button(top, textvariable=btn7_text, width=22, height=12, command=lambda: callback("b7", player))
b8 = tk.Button(top, textvariable=btn8_text, width=22, height=12, command=lambda: callback("b8", player))
b9 = tk.Button(top, textvariable=btn9_text, width=22, height=12, command=lambda: callback("b9", player))

b1.grid(row=6, column=0)
b2.grid(row=6, column=1)
b3.grid(row=6, column=2)
b4.grid(row=7, column=0)
b5.grid(row=7, column=1)
b6.grid(row=7, column=2)
b7.grid(row=8, column=0)
b8.grid(row=8, column=1)
b9.grid(row=8, column=2)


b1.config(state="disabled")
b2.config(state="disabled")
b3.config(state="disabled")
b4.config(state="disabled")
b5.config(state="disabled")
b6.config(state="disabled")
b7.config(state="disabled")
b8.config(state="disabled")
b9.config(state="disabled")


top.mainloop()
