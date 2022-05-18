from tkinter import *

from math import *
from xml.dom.pulldom import END_DOCUMENT
root = Tk()
root.title('Scientific Calculator')
root.iconbitmap('C:/Users/USER/Documents/GitHub/scientific-calculator/images/icon.jpeg')

button_bg = '#dddddd' #set color of text on button
button_fg = '#444444'   #set button background color
x_size = '22'   #set width of button
y_size = '10'   #set height of button

#column numbers and row numbers
col0 = 0
col1 = 1
col2 = 2
col3 = 3
col4 = 4
row1 = 1
row2 = 2
row3 = 3
row4 = 4
row5 = 5
row6 = 6
row7 = 7

"""functions for buttons"""
def button_click(number):    
    current = entry.get()
    entry.delete(0, END) 
    entry.insert(0, (str(current) + str(number)))

def fxn_squ_root():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'squ_root'
    entry.delete(0, END)

def fxn_squared():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'squared'
    entry.delete(0, END)

def fxn_pow_x():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'pow_x'
    entry.delete(0, END)

def fxn_logarithm():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'logarithm'
    entry.delete(0, END)

def fxn_log_a_b():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'log_a_b'
    entry.delete(0, END)

def fxn_sine():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'sine'
    entry.delete(0, END)

def fxn_cosine():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'cosine'
    entry.delete(0, END)
    
def fxn_tangent():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'tangent'
    entry.delete(0, END)
    
def fxn_arcsine():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'arcsine'
    entry.delete(0, END)
    
def fxn_arccos():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'arccos'
    entry.delete(0, END)
    
def fxn_arctan():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'arctan'
    entry.delete(0, END)
    
def fxn_inverse():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'inverse'
    entry.delete(0, END)
    
def fxn_ln():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'ln'
    entry.delete(0, END)
    
def fxn_exponential():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'exponential'
    entry.delete(0, END)
    
def fxn_factorial():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'factorial'
    entry.delete(0, END)
    

def fxn_backspace():
    a = entry.get()
    entry.delete(0, END)
    entry.insert(0, float(a)//10)
    

def fxn_clear():
    entry.delete(0, END)

def fxn_mult():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'mult'
    entry.delete(0, END)
    
def fxn_divide():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'divide'
    entry.delete(0, END)

def fxn_plus():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'plus'
    entry.delete(0, END)
    
def fxn_minus():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'minus'
    entry.delete(0, END)
    
def fxn_dot():
    f_num = entry.get()
    entry.delete(0, END)
    entry.insert(0, f_num+'.')
    

def fxn_ten_exponent():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'ten_exponent'
    entry.delete(0, END)
    
def fxn_pi():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = 'pi'
    entry.delete(0, END)
    
def open_brac():
    pass

def close_brac():
    pass
    
def fxn_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if operation == 'squ_root':
        try:
            op = '{:.6f}'.format(pow(f_num, 0.5))
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')
    elif operation == 'squared':
        try:
            op = pow(f_num, 2)
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')
    elif operation == 'pow_x':
        try:
            op = '{:.6f}'.format(pow(f_num, float(second_number)))
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')
    elif operation == 'logarithm':
        try:
            op = '{:.6f}'.format(log10(f_num))
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')
    elif operation == 'log_a_b':
        try:
            op = '{:.6f}'.format(log(f_num, float(second_number)))
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')
    elif operation == 'sine':
        try:
            op = '{:.6f}'.format(sin(f_num))
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')
    elif operation == 'cosine':
        try:
            op = '{:.6f}'.format(cos(f_num))
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')
    elif operation == 'tangent':
        try:
            op = '{:.6f}'.forma (tan(f_num))
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')
    elif operation == 'arcsine':
        try:
            op = '{:.6f}'.format(asin(f_num)*180/pi)
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')
    elif operation == 'arccos':
        try:
            op = '{:.6f}'.format(acos(f_num)*180/pi)
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')
    elif operation == 'arctan':
        try:
            op = '{:.6f}'.format(atan(f_num)*180/pi)
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')
    elif operation == 'inverse':
        try:
            op = '{:.6f}'.format(1/f_num)
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')
    elif operation == 'ln':
        try:
            op = '{:.6f}'.format(log(f_num))
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')
    elif operation == 'exponential':
        try:
            op = '{:.6f}'.format(exp(f_num))
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')
    elif operation == 'factorial':
        try:
            if f_num == 0:
                entry.insert(0, 1)
            else:
                i = float(f_num)
                fact = 1
                while i > 0:
                    fact *= i
                    i -= 1
                entry.insert(0, int(fact))
        except:
            entry.insert(0, 'Error!')
    elif operation == 'mult':
        try:
            op = f_num*float(second_number)
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')
    elif operation == 'divide':
        try:
            op = '{:.6f}'.format(f_num/float(second_number))
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')
    elif operation == 'plus':
        try:
            op = f_num + float(second_number)
            entry.insert(0, int(op))
        except:
            entry.insert(0, 'Error!')
    elif operation == 'minus':
        try:
            op = f_num - float(second_number)
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')
    elif operation == 'ten_exponent':
        try:
            op = f_num*pow(10, float(second_number))
            entry.insert(0, op)
        except:
            entry.insert(0, 'Error!')


entry = Entry(root, width=70, fg='blue', bg='#77eebb', borderwidth=5) #create entry field
_exit = Button(root, text='Exit', command=root.quit) #create an exit button

#create each button on calculator
#row 1
squ_root = Button(root, text='sqrt(x)', padx=x_size, pady=y_size, fg=button_fg, bg=button_bg, command=lambda: fxn_squ_root())
squared = Button(root, text='x^2', padx='37', pady=y_size, fg=button_fg, bg=button_bg, command=lambda: fxn_squared())
pow_x = Button(root, text='x^a', padx='40', pady=y_size, fg=button_fg, bg=button_bg, command=lambda: fxn_pow_x())
logarithm = Button(root, text='log(x)', padx='35', pady=y_size, fg=button_fg, bg=button_bg, command=lambda: fxn_logarithm())
log_a_b = Button(root, text='logb(a)', padx='33', pady=y_size, fg=button_fg, bg=button_bg, command=lambda:fxn_log_a_b())

#row 2
sine = Button(root, text='sin(x)', padx='24', pady=y_size, fg=button_fg, bg=button_bg, command=lambda:fxn_sine())
cosine = Button(root, text='cos(x)', padx='30', pady=y_size, fg=button_fg, bg=button_bg, command=lambda:fxn_cosine())
tangent = Button(root, text='tan(x)', padx='35', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:fxn_tangent())
arcsin = Button(root, text='asin(x)', padx='33', pady=y_size, fg=button_fg, bg=button_bg, command=lambda:fxn_arcsine())
arccos = Button(root, text='acos(x)', padx='33', pady=y_size, fg=button_fg, bg=button_bg, command=lambda:fxn_arccos())

#row 3
arctan = Button(root, text='atan(x)', padx='19.5', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:fxn_arctan())
inverse = Button(root, text='x^-1', padx='34', pady=y_size, fg=button_fg, bg=button_bg, command=lambda:fxn_inverse())
ln = Button(root, text='ln(x)', padx='38.5', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:fxn_ln())
exponential = Button(root, text='e^x', padx='41', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:fxn_exponential())
factorial = Button(root, text='x!', padx='47', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:fxn_factorial())

#row 4
b7 = Button(root, text='7', padx='35.5', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:button_click(7))
b8 = Button(root, text='8', padx='43', pady=y_size, fg=button_fg, bg=button_bg, command=lambda:button_click(8))
b9 = Button(root, text='9', padx='47', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:button_click(9))
back_space = Button(root, text='Del', padx='43', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:fxn_backspace())
clear = Button(root, text='AC', padx='43', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:fxn_clear())

#row 5
b4 = Button(root, text='4', padx='35.5', pady=y_size, fg=button_fg, bg=button_bg, command=lambda: button_click(4))
b5 = Button(root, text='5', padx='44', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:button_click(5))
b6 = Button(root, text='6', padx='47', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:button_click(6))
mult = Button(root, text='*', padx='49', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:fxn_mult())
divided = Button(root, text='/', padx='48', pady=y_size, fg=button_fg, bg=button_bg, command=lambda:fxn_divide())

#row 6
b1 = Button(root, text='1', padx='35.5', pady=y_size, fg=button_fg, bg=button_bg, command=lambda:button_click(1))
b2 = Button(root, text='2', padx='44', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:button_click(2))
b3 = Button(root, text='3', padx='48', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:button_click(3))
plus = Button(root, text='+', padx='48', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:fxn_plus())
minus = Button(root, text='-', padx='48', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:fxn_minus())

#row 7
zero = Button(root, text='0', padx='35.5', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:button_click(0))
dot = Button(root, text='.', padx='44', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:fxn_dot())
ten_exponent = Button(root, text='x10^a', padx='35', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:fxn_ten_exponent())
pie = Button(root, text='pi', padx='46', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:button_click(pi))
equal = Button(root, text='=', padx='47', pady=y_size, fg=button_fg, bg=button_bg,command=lambda:fxn_equal())

#row 8
open_par = Button(root, text='(', padx=37, pady=20, fg=button_fg, bg=button_bg, command=lambda:open_brac())
close_par = Button(root, text=')', padx=44, pady=20, fg=button_fg, bg=button_bg, command=lambda:close_brac())
_exit = Button(root, text='Exit', padx=155, pady=20, fg=button_fg, bg=button_bg, command=root.quit) #create an exit button


#entry field (row zero)
entry.grid(row=0, column=0, columnspan=5, padx=30, pady=10)

#first row buttons
squ_root.grid(row=row1, column=col0)
squared.grid(row=row1, column=col1)
pow_x.grid(row=row1, column=col2)
logarithm.grid(row=row1, column=col3)
log_a_b.grid(row=row1, column=col4)

#second row buttons
sine.grid(row=row2, column=col0)
cosine.grid(row=row2, column=col1)
tangent.grid(row=row2, column=col2)
arcsin.grid(row=row2, column=col3)
arccos.grid(row=row2, column=col4)

#third row buttons
arctan.grid(row=row3, column=col0)
inverse.grid(row=row3, column=col1)
ln.grid(row=row3, column=col2)
exponential.grid(row=row3, column=col3)
factorial.grid(row=row3, column=col4)

#forth row buttons
b7.grid(row=row4, column=col0)
b8.grid(row=row4, column=col1)
b9.grid(row=row4, column=col2)
back_space.grid(row=row4, column=col3)
clear.grid(row=row4, column=col4)

#fifth row buttons
b4.grid(row=row5, column=col0)
b5.grid(row=row5, column=col1)
b6.grid(row=row5, column=col2)
mult.grid(row=row5, column=col3)
divided.grid(row=row5, column=col4)

#sixth row buttons
b1.grid(row=row6, column=col0)
b2.grid(row=row6, column=col1)
b3.grid(row=row6, column=col2)
plus.grid(row=row6, column=col3)
minus.grid(row=row6, column=col4)

#seventh row buttons
zero.grid(row=row7, column=col0)
dot.grid(row=row7, column=col1)
ten_exponent.grid(row=row7, column=col2)
pie.grid(row=row7, column=col3)
equal.grid(row=row7, column=col4)

#eigth row buttons
open_par.grid(row=8, column=0)
close_par.grid(row=8, column=1)
_exit.grid(row=8, column=2, columnspan=3)
root.mainloop()