# Designed and Developed by Muhammad Umair Yaqub.
# Made in P A K I S T A N

import tkinter

class Drag(tkinter.Tk):
    
    def __init__(self):
        super().__init__()
        
        # remove the title bar of the window
        super().overrideredirect(True)
        
        # set initial offsets for dragging the window
        self._offsetx = 0
        self._offsety = 0
        
        # bind mouse events to window functions
        super().bind("<Button-1>", self.clickwin)
        super().bind("<B1-Motion>", self.dragwin)

    def dragwin(self, event):
        # calculate the new window position based on the mouse drag distance
        x = super().winfo_pointerx() - self._offsetx
        y = super().winfo_pointery() - self._offsety
        
        # move the window to the new position
        super().geometry(f"+{x}+{y}")

    def clickwin(self, event):
        # calculate the initial offset between the mouse click and the window position
        self._offsetx = super().winfo_pointerx() - super().winfo_rootx()
        self._offsety = super().winfo_pointery() - super().winfo_rooty()

# Create a window object and set its properties
window = Drag()  # It's unclear what 'Drag' is or if it's a class provided by tkinter, please clarify.

window.geometry("290x400")  # Set the size of the window
window.overrideredirect(1)  # Remove the window border
window.title("Calculator")  # Set the window title
window.attributes('-alpha', 0.9)  # Set the window transparency
window.eval( 'tk::PlaceWindow . center')  # Center the window on the screen

# Define functions for the calculator buttons
def btn_click(item):
    global expression  # Use of global variables should be minimized, consider using a class or a function to encapsulate state.
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    result = str(eval(expression))  # Using eval can be risky, consider using a safer way to evaluate expressions.
    input_text.set(result)
    expression = ""

# Create the calculator interface
close_btn  = Frame(window, width=50, height=50, bg="#ededed")  # Add a close button to the window.
close_btn.pack(anchor='e')

expression = ""
input_text = StringVar()  # Initialize the input field as a tkinter string variable.

# Create the input field
input_frame = Frame(window, width=300, height=100, bd=0, highlightbackground="#ededed", highlightcolor="#ededed", highlightthickness=1)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('Cascadia Code', 30, 'normal'), textvariable=input_text, width=40, fg="#737373", bg="#ededed", bd=0, justify=RIGHT)  # Set the properties of the input field.
input_field.grid(row=1, column=1)
input_field.pack(ipady=10)

# Create the calculator buttons
btns_frame = Frame(window, width=400, height=500, bg="#ededed")
btns_frame.pack()

# Create buttons for digits and operations
close        = Button(close_btn, text = "✕", anchor='e', justify = RIGHT, font = ('Cascadia Code', "10", 'bold'), fg = "#737373", width = 2, height = 1, bd = 0, bg = "#ededed", cursor = "hand2", command = window.destroy).grid(row = 0,   column = 0, padx = 2, pady = 1)
zero         = Button(btns_frame, text = "0", font = ('Cascadia Code', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 5,   column = 2, padx = 1, pady = 1)   # columnspan = 2,
one          = Button(btns_frame, text = "1", font = ('Cascadia Code', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 4,   column = 1, padx = 1, pady = 1)
two          = Button(btns_frame, text = "2", font = ('Cascadia Code', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 4,   column = 2, padx = 1, pady = 1)
three        = Button(btns_frame, text = "3", font = ('Cascadia Code', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 4,   column = 3, padx = 1, pady = 1)
four         = Button(btns_frame, text = "4", font = ('Cascadia Code', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 3,   column = 1, padx = 1, pady = 1)
five         = Button(btns_frame, text = "5", font = ('Cascadia Code', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 3,   column = 2, padx = 1, pady = 1)
six          = Button(btns_frame, text = "6", font = ('Cascadia Code', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 3,   column = 3, padx = 1, pady = 1) 
seven        = Button(btns_frame, text = "7", font = ('Cascadia Code', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 2,   column = 1, padx = 1, pady = 1) 
eight        = Button(btns_frame, text = "8", font = ('Cascadia Code', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 2,   column = 2, padx = 1, pady = 1) 
nine         = Button(btns_frame, text = "9", font = ('Cascadia Code', "20", 'normal'), fg = "#737373", width = 4, height = 1, bd = 0, bg = "#fcfcfc", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 2,   column = 3, padx = 1, pady = 1) 
clear        = Button(btns_frame, text = "C", font = ('Cascadia Code', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_clear()).grid(row = 1,    column = 1, padx = 1, pady = 1)   # columnspan = 3,
left_bracket = Button(btns_frame, text = "(", font = ('Cascadia Code', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_click("(")).grid(row = 1, column = 2, padx = 1, pady = 1)
left_bracket = Button(btns_frame, text = ")", font = ('Cascadia Code', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_click(")")).grid(row = 1, column = 3, padx = 1, pady = 1)
divide       = Button(btns_frame, text = "÷", font = ('Cascadia Code', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 1, column = 4, padx = 1, pady = 1)
multiply     = Button(btns_frame, text = "x", font = ('Cascadia Code', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 2, column = 4, padx = 1, pady = 1)
minus        = Button(btns_frame, text = "-", font = ('Cascadia Code', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 3, column = 4, padx = 1, pady = 1)
plus         = Button(btns_frame, text = "+", font = ('Cascadia Code', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 4, column = 4, padx = 1, pady = 1)
percentage   = Button(btns_frame, text = "%", font = ('Cascadia Code', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_click("%")).grid(row = 5, column = 3, padx = 1, pady = 1)
point        = Button(btns_frame, text = ".", font = ('Cascadia Code', "20", 'normal'), fg = "#00cbf6", width = 4, height = 1, bd = 0, bg = "#f5f5f5", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 5, column = 1, padx = 1, pady = 1)
equals       = Button(btns_frame, text = "=", font = ('Cascadia Code', "20", 'normal'), fg = "#ffffff", width = 4, height = 1, bd = 0, bg = "#00cbf6", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5,    column = 4, padx = 1, pady = 1)

window.mainloop()
