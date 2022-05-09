from tkinter import *

from matplotlib.pyplot import title

root = Tk()
root.title('Scientific Calculator')

button_bg = '#dddddd' #set color of text on button
button_fg = '#444444'   #set button background color
x_size = '22'   #set width of button
y_size = '10'   #set height of button
other_x = '35'

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

entry = Entry(root, width=70, fg='blue', bg='#77eebb', borderwidth=5) #create entry field

#create each button on calculator
#row 1
squ_root = Button(root, text='sqrt(x)', padx=x_size, pady=y_size, fg=button_fg, bg=button_bg)
squared = Button(root, text='x^2', padx='37', pady=y_size, fg=button_fg, bg=button_bg)
pow_x = Button(root, text='x^y', padx='40', pady=y_size, fg=button_fg, bg=button_bg)
logarithm = Button(root, text='log(x)', padx='35', pady=y_size, fg=button_fg, bg=button_bg)
log_a_b = Button(root, text='logb(a)', padx='33', pady=y_size, fg=button_fg, bg=button_bg)

#row 2
sine = Button(root, text='sin(x)', padx='24', pady=y_size, fg=button_fg, bg=button_bg)
cosine = Button(root, text='cos(x)', padx='30', pady=y_size, fg=button_fg, bg=button_bg)
tangent = Button(root, text='tan(x)', padx='35', pady=y_size, fg=button_fg, bg=button_bg)
arcsin = Button(root, text='asin(x)', padx='33', pady=y_size, fg=button_fg, bg=button_bg)
arccos = Button(root, text='acos(x)', padx='33', pady=y_size, fg=button_fg, bg=button_bg)

#row 3
arctan = Button(root, text='atan(x)', padx='19.5', pady=y_size, fg=button_fg, bg=button_bg)
inverse = Button(root, text='x^-1', padx='34', pady=y_size, fg=button_fg, bg=button_bg)
ln = Button(root, text='ln(x)', padx='38.5', pady=y_size, fg=button_fg, bg=button_bg)
exponential = Button(root, text='e^x', padx='40', pady=y_size, fg=button_fg, bg=button_bg)
factorial = Button(root, text='x!', padx='47', pady=y_size, fg=button_fg, bg=button_bg)

#row 4
b7 = Button(root, text='7', padx='35.5', pady=y_size, fg=button_fg, bg=button_bg)
b8 = Button(root, text='8', padx='43', pady=y_size, fg=button_fg, bg=button_bg)
b9 = Button(root, text='9', padx='46.5', pady=y_size, fg=button_fg, bg=button_bg)
back_space = Button(root, text='Del', padx='43', pady=y_size, fg=button_fg, bg=button_bg)
clear = Button(root, text='AC', padx='43', pady=y_size, fg=button_fg, bg=button_bg)

#row 5
b4 = Button(root, text='4', padx='35.5', pady=y_size, fg=button_fg, bg=button_bg)
b5 = Button(root, text='5', padx='44', pady=y_size, fg=button_fg, bg=button_bg)
b6 = Button(root, text='6', padx='47', pady=y_size, fg=button_fg, bg=button_bg)
mult = Button(root, text='x', padx='48', pady=y_size, fg=button_fg, bg=button_bg)
divided = Button(root, text='/', padx='49', pady=y_size, fg=button_fg, bg=button_bg)

#row 6
b1 = Button(root, text='1', padx='35.5', pady=y_size, fg=button_fg, bg=button_bg)
b2 = Button(root, text='2', padx='44', pady=y_size, fg=button_fg, bg=button_bg)
b3 = Button(root, text='3', padx='48', pady=y_size, fg=button_fg, bg=button_bg)
plus = Button(root, text='+', padx='48', pady=y_size, fg=button_fg, bg=button_bg)
minus = Button(root, text='-', padx='48', pady=y_size, fg=button_fg, bg=button_bg)

#row 7
zero = Button(root, text='0', padx='35.5', pady=y_size, fg=button_fg, bg=button_bg)
dot = Button(root, text='.', padx='44', pady=y_size, fg=button_fg, bg=button_bg)
ten_exponent = Button(root, text='x10^a', padx=other_x, pady=y_size, fg=button_fg, bg=button_bg)
pie = Button(root, text='pi', padx='46', pady=y_size, fg=button_fg, bg=button_bg)
equal = Button(root, text='=', padx='47', pady=y_size, fg=button_fg, bg=button_bg)


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

root.mainloop()