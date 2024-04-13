from tkinter import *
import random
root = Tk()
root.title("MOO ICT")
root.geometry("250x150")
secret_number = "none"
# function and events
def StartGame():
    global secret_number
    for button in button_list:
        button.config(text=str(random.randint(0, 100)))
    
    randomButton = random.choice(button_list)
    secret_number = randomButton.cget("text")
    print("Secret Number is: ", secret_number)
def OnClick(event):
    btn = event.widget
    buttonText = btn.cget("text")
    if secret_number == buttonText:
        answer_label.config(text="Yes it was " + secret_number)
        StartGame()
# gui components
title_label = Label(root, text="Guess the Secret Number", font=("Helvetical 12"), pady = 8, justify="center")
button_one = Button(root, text="00", font=("Helvetical 15"), width=6, pady=15, bg="palegreen")
button_two = Button(root, text="00", font=("Helvetical 15"), width=6, pady=15, bg="skyblue")
button_three = Button(root, text="00", font=("Helvetical 15"), width=6, pady=15, bg="coral")
button_list = [button_one, button_two, button_three]
answer_label = Label(root, text="Answer", font=("Helvetical 15"), pady=9, fg="purple", justify="center")
title_label.grid(row = 0, column=0, columnspan=3)
button_one.grid(row=1, column=0)
button_two.grid(row=1, column=1)
button_three.grid(row=1, column=2)
answer_label.grid(row = 2, column=0, columnspan=3)
button_one.bind("<Button-1>", OnClick)
button_two.bind("<Button-1>", OnClick)
button_three.bind("<Button-1>", OnClick)
StartGame()
root.mainloop()
