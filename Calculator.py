# Designed and Developed by Muhammad Umair Yaqub.
# P A K I S T A N

from tkinter import *

window = Tk()
window.geometry("295x375")
# window.resizable( 0, 0)
window.overrideredirect(0)
window.title("Calculator")
# window.iconbitmap('C:/Users/umair/Downloads/circle_FeX_icon.ico')


def btn_click(item):
 
    global expression
    input_text.set(expression)
    expression = expression + str(item)
    

def btn_clear():
 
    global expression
    expression = ""
    input_text.set("")
 
def btn_equal():
 
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

def close():

    window.destroy()

expression  = ""
input_text  = StringVar()
input_frame = Frame(window, width = 300, height = 100, bd = 0, highlightbackground = "#ededed", highlightcolor = "#ededed", highlightthickness = 1)
input_frame.pack(side = TOP)
input_field = Entry(input_frame, font = ('Cascadia Mono', 30, 'normal'), textvariable = input_text, width = 50, bg = "#ededed", fg = "#737373", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)
btns_frame  = Frame(window, width = 400, height = 500, bg = "#ededed")
btns_frame.pack()

zero         = Button(btns_frame, text = "0", font = ('Cascadia Mono', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4,   column = 1, padx = 1, pady = 1)   # columnspan = 2,
one          = Button(btns_frame, text = "1", font = ('Cascadia Mono', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3,   column = 0, padx = 1, pady = 1)
two          = Button(btns_frame, text = "2", font = ('Cascadia Mono', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3,   column = 1, padx = 1, pady = 1)
three        = Button(btns_frame, text = "3", font = ('Cascadia Mono', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3,   column = 2, padx = 1, pady = 1)
four         = Button(btns_frame, text = "4", font = ('Cascadia Mono', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2,   column = 0, padx = 1, pady = 1)
five         = Button(btns_frame, text = "5", font = ('Cascadia Mono', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2,   column = 1, padx = 1, pady = 1)
six          = Button(btns_frame, text = "6", font = ('Cascadia Mono', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2,   column = 2, padx = 1, pady = 1) 
seven        = Button(btns_frame, text = "7", font = ('Cascadia Mono', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1,   column = 0, padx = 1, pady = 1) 
eight        = Button(btns_frame, text = "8", font = ('Cascadia Mono', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1,   column = 1, padx = 1, pady = 1) 
nine         = Button(btns_frame, text = "9", font = ('Cascadia Mono', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1,   column = 2, padx = 1, pady = 1) 
clear        = Button(btns_frame, text = "C", font = ('Cascadia Mono', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0,    column = 0, padx = 1, pady = 1)   # columnspan = 3,
left_bracket = Button(btns_frame, text = "(", font = ('Cascadia Mono', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_click("(")).grid(row = 0, column = 1, padx = 1, pady = 1)
left_bracket = Button(btns_frame, text = ")", font = ('Cascadia Mono', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_click(")")).grid(row = 0, column = 2, padx = 1, pady = 1)
divide       = Button(btns_frame, text = "÷", font = ('Cascadia Mono', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
multiply     = Button(btns_frame, text = "x", font = ('Cascadia Mono', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
minus        = Button(btns_frame, text = "-", font = ('Cascadia Mono', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
plus         = Button(btns_frame, text = "+", font = ('Cascadia Mono', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
percentage   = Button(btns_frame, text = "%", font = ('Cascadia Mono', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_click("%")).grid(row = 4, column = 2, padx = 1, pady = 1)
point        = Button(btns_frame, text = ".", font = ('Cascadia Mono', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 0, padx = 1, pady = 1)
equals       = Button(btns_frame, text = "=", font = ('Cascadia Mono', "20", 'normal'), fg = "#ffffff", width = 4, height = 1, bd = 0, bg = "#00cbf6", cursor = "hand2", command = lambda: btn_equal()).grid(row = 4,    column = 3, padx = 1, pady = 1)

window.mainloop()
