from tkinter import *

calculadora = Tk()
calculadora.configure(bg = '#333333')
calculadora.title("Calculadora")
calculadora.geometry("150x168")

equation = StringVar()

def press(btn):
    if btn == 'clear':
        equation.set('')
    else: 
        equation.set(equation.get() + str(btn))

def resultado():
    try:
        total = str(eval(equation.get()))
        equation.set(total)
    except:
        equation.set("ERROR")

pantalla = Entry(calculadora, textvariable = equation, state = 'disabled')
pantalla.grid(row = 0, columnspan = 4, sticky = 'nswe') #'sticky' es una instrucción la cual define el entry para ocupar todo el ancho y el largo del área disponible y el string 'nswe' es del inglés 'norte, sur, este y oeste'

#Operadores
suma = Button(calculadora, text = " + ", fg = "#fff", bg = "#fe9727", command = lambda: press("+"))
suma.grid(row = 1, column = 3, sticky = "nswe")

resta = Button(calculadora, text = " - ", fg = "#fff", bg = "#fe9727", command = lambda: press("-"))
resta.grid(row = 2, column = 3, sticky = "nswe")

mult = Button(calculadora, text = " * ", fg = "#fff", bg = "#fe9727", command = lambda: press("*"))
mult.grid(row = 3, column = 3, sticky = "nswe")

div = Button(calculadora, text = " / ", fg = "#fff", bg = "#fe9727", command = lambda: press("/"))
div.grid(row = 4, column = 3, sticky = "nswe")

igual = Button(calculadora, text = " = ", fg = "#fff", bg = "#fe9727", command = lambda: resultado())
igual.grid(row = 5, column = 3, sticky = "nswe")


#Numeros
#Fila 1
btn7 = Button(calculadora, text = " 7 ", fg = "#fff", bg = "#666", command = lambda: press(7))
btn7.grid(row = 1, column = 0, sticky = "nswe")

btn8 = Button(calculadora, text = " 8 ", fg = "#fff", bg = "#666", command = lambda: press(8))
btn8.grid(row = 1, column = 1, sticky = "nswe")

btn9 = Button(calculadora, text = " 9 ", fg = "#fff", bg = "#666", command = lambda: press(9))
btn9.grid(row = 1, column = 2, sticky = "nswe")

#Fila 2
btn4 = Button(calculadora, text = " 4 ", fg = "#fff", bg = "#666", command = lambda: press(4))
btn4.grid(row = 2, column = 0, sticky = "nswe")

btn5 = Button(calculadora, text = " 5 ", fg = "#fff", bg = "#666", command = lambda: press(5))
btn5.grid(row = 2, column = 1, sticky = "nswe")

btn6 = Button(calculadora, text = " 6 ", fg = "#fff", bg = "#666", command = lambda: press(6))
btn6.grid(row = 2, column = 2, sticky = "nswe")

#Fila 3
btn1 = Button(calculadora, text = " 1 ", fg = "#fff", bg = "#666", command = lambda: press(1))
btn1.grid(row = 3, column = 0, sticky = "nswe")

btn2 = Button(calculadora, text = " 2 ", fg = "#fff", bg = "#666", command = lambda: press(2))
btn2.grid(row = 3, column = 1, sticky = "nswe")

btn3 = Button(calculadora, text = " 3 ", fg = "#fff", bg = "#666", command = lambda: press(3))
btn3.grid(row = 3, column = 2, sticky = "nswe")


#Botones Fila 4
btn0 = Button(calculadora, text = " 0 ", fg = "#fff", bg = "#666", command = lambda: press(0))
btn0.grid(row = 4, columnspan = 2, sticky = "nswe")

btn_point = Button(calculadora, text = " . ", fg = "#fff", bg = "#666", command = lambda: press('.'))
btn_point.grid(row = 4, column = 2, sticky = "nswe")

btn_clear = Button(calculadora, text = " clear ", fg = "#fff", bg = "#999", command = lambda: press("clear"))
btn_clear.grid(row = 5, column = 2, sticky = "nswe")

calculadora.mainloop()