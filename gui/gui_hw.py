import tkinter as hrik

meulas = 10

def update_meulas_label():
    
    meulas_value_label.config(text= str(meulas))

def move_forward():
    
    global meulas
    if meulas >= 1:
        meulas -= 1
        update_meulas_label()
        message_label.config(text="Bot is moving Forward")
    else:
        message_label.config(text="Error: Not enough Meulas")

def move_back():
    
    global meulas
    if meulas >= 1:
        meulas -= 1
        update_meulas_label()
        message_label.config(text="Bot is moving Back")
    else:
        message_label.config(text="Error: Not enough Meulas")

def rotate_left():
 
    global meulas
    if meulas >= 2:
        meulas -= 2
        update_meulas_label()
        message_label.config(text="Bot is rotating Left")
    else:
        message_label.config(text="Error: Not enough Meulas")

def rotate_right():
   
    global meulas
    if meulas >= 2:
        meulas -= 2
        update_meulas_label()
        message_label.config(text="Bot is rotating Right")
    else:
        message_label.config(text="Error: Not enough Meulas")
        
def message():
	pass
def meula_remain():
	pass
	

def increase_meulas():
    """Simulates increasing meulas by rotating the bot."""
    global meulas
    meulas += 19
    update_meulas_label()
    


root =hrik.Tk()
root.title("Bot GUI")
root.geometry("800x300")



meulas_value_label = hrik.Label(root, text=str(meulas), font=('Helvetica', 12), relief=hrik.SUNKEN, width=10)
meulas_value_label.grid(row=1, column=9)


message_label = hrik.Label(root, text=" ", font=('Helvetica', 12))
message_label.grid(row=10, column=9)


forward_button = hrik.Button(root, text="Forward", command=move_forward)
forward_button.grid(row=2, column=2)

back_button = hrik.Button(root, text="Back", command=move_back)
back_button.grid(row=6, column=2)

left_button = hrik.Button(root, text="Left", command=rotate_left)
left_button.grid(row=4, column=1)

right_button = hrik.Button(root, text="Right", command=rotate_right)
right_button.grid(row=4, column=3)

button_meula= hrik.Button(root, text="Remaining Meulas:", command=meula_remain)
button_meula.grid(row=1, column=8)

button_message= hrik.Button(root, text="Message", command=message)
button_message.grid(row=9, column=9)



increase_meulas_button = hrik.Button(root, text="Increase Meulas", command=increase_meulas)
increase_meulas_button.grid(row=3, column=9)

root.mainloop()

