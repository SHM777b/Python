import tkinter
from tkinter import END

# MAIN WINDOW
mainWindow = tkinter.Tk()
mainWindow.title('Calculator')
mainWindow.geometry('320x320-100-100')
mainWindow.config(padx=10, pady=10)

mainWindow.grid_columnconfigure(0, weight=1)
mainWindow.grid_columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)
mainWindow.grid_columnconfigure(3, weight=1)

mainWindow.grid_rowconfigure(0, weight=1)
mainWindow.grid_rowconfigure(1, weight=1)
mainWindow.grid_rowconfigure(2, weight=1)
mainWindow.grid_rowconfigure(3, weight=1)
mainWindow.grid_rowconfigure(4, weight=1)
mainWindow.grid_rowconfigure(5, weight=1)

# ENTRY WINDOW
entry_window = tkinter.Entry(mainWindow)
entry_window.grid(row=0, column=0, columnspan=4, sticky='news')

# LIST OF ENTRIES
entries = []
exp = str()


# WRITING TO ENTRY
def input_new(value):
    i = entry_window.get()
    if i == '+' or i == '-' or i == '*' or i == '/':
        entry_window.delete(0, END)
    entry_window.insert(END, value)


def symbol(val):
    entry_window.delete(0, END)
    entry_window.insert(0, val)


def calculation(exp):
    res = eval(exp)
    entry_window.delete(0, END)
    entry_window.insert(0, res)
    # return str(res)


def callback(val):
    global exp
    i = entry_window.get()
    if val == 'C':
        entry_window.delete(len(i)-1, END)
    elif val == 'CE':
        entry_window.delete(0, END)
    elif val == '+':
        exp += i + '+'
        print(exp)
        symbol('+')
    elif val == '-':
        exp += i + '-'
        print(exp)
        symbol('-')
    elif val == '*':
        exp += i + '*'
        print(exp)
        symbol('*')
    elif val == '/':
        exp += i + '/'
        print(exp)
        symbol('/')
    elif val == '=':
        exp += i
        print(exp)
        calculation(exp)
        exp = ''
    else:
        if i == '0':
            entry_window.delete(0, END)
        input_new(val)


# BUTTONS
button_1 = tkinter.Button(mainWindow, text='1', command=lambda: callback(1)).grid(row=4, column=0, sticky='news')
button_2 = tkinter.Button(mainWindow, text='2', command=lambda: callback(2)).grid(row=4, column=1, sticky='news')
button_3 = tkinter.Button(mainWindow, text='3', command=lambda: callback(3)).grid(row=4, column=2, sticky='news')
button_4 = tkinter.Button(mainWindow, text='4', command=lambda: callback(4)).grid(row=3, column=0, sticky='news')
button_5 = tkinter.Button(mainWindow, text='5', command=lambda: callback(5)).grid(row=3, column=1, sticky='news')
button_6 = tkinter.Button(mainWindow, text='6', command=lambda: callback(6)).grid(row=3, column=2, sticky='news')
button_7 = tkinter.Button(mainWindow, text='7', command=lambda: callback(7)).grid(row=2, column=0, sticky='news')
button_8 = tkinter.Button(mainWindow, text='8', command=lambda: callback(8)).grid(row=2, column=1, sticky='news')
button_9 = tkinter.Button(mainWindow, text='9', command=lambda: callback(9)).grid(row=2, column=2, sticky='news')
button_0 = tkinter.Button(mainWindow, text='0', command=lambda: callback(0)).grid(row=5, column=0, sticky='news')
button_plus = tkinter.Button(mainWindow, text='+', command=lambda: callback('+')).grid(row=2, column=3, sticky='news')
button_minus = tkinter.Button(mainWindow, text='-', command=lambda: callback('-')).grid(row=3, column=3, sticky='news')
button_divide = tkinter.Button(mainWindow, text='/', command=lambda: callback('/')).grid(row=4, column=3, sticky='news')
button_multiply = tkinter.Button(mainWindow, text='*', command=lambda: callback('*')).grid(row=5, column=3, sticky='news')
button_equal = tkinter.Button(mainWindow, text='=', command=lambda: callback('=')).grid(row=5, column=1, columnspan=2, sticky='news')
button_c = tkinter.Button(mainWindow, text='C', command=lambda: callback('C')).grid(row=1, column=0, sticky='news')
button_ce = tkinter.Button(mainWindow, text='CE', command=lambda: callback('CE')).grid(row=1, column=1, sticky='news')

mainWindow.mainloop()
