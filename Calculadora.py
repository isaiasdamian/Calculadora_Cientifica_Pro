from tkinter import Button, Tk, Frame,Entry,END
import math
"""Código elaborado por Isaias Damian Martinez Rivera"""
"""Calculadora cientifica desarrollada en Python"""
ventana = Tk()
ventana.geometry('276x491')
ventana.config(bg= "black")
ventana.resizable(0,0)
ventana.title('Calculadora')
#Añadir que no pueda poner el usuario otro punto listo
#añadir que se pueda elevar a cualquier potencia listo
#añadir que se pueda sacar cualquier raiz listo
#añadir porcentajes que se pueda sacar el 5 por ciento de 100 etc listo

class HoverButton(Button):
	def __init__(self, master, **kw):
		Button.__init__(self,master=master,**kw)
		self.defaultBackground = self["background"]
		self.bind("<Enter>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self, e):
		self["background"] = self["activebackground"]

	def on_leave(self, e):
		self["background"] = self.defaultBackground

def letraHexadecimal(x):
    if x == 10:
        return 'A'
    elif x ==11:
        return 'B'
    elif x ==12:
        return 'C'
    elif x ==13:
        return 'D'
    elif x ==14:
        return 'E'
    elif x ==15:
        return 'F'

    if x == 'A':
        return 10
    elif x == 'B':
        return 11
    elif x == 'C':
        return 12
    elif x =='D':
        return 13
    elif x =='E':
        return 14
    elif x == 'F':
        return 15

def fromaBase10(base: int):
    n = abs(int(Resultado.get()))
    residuos = []

    while True:
        residuo = n % base
        if residuo > 9: residuo = letraHexadecimal(residuo)
        residuos.append(str(residuo))
        n = int(n / base)
        if n == 0: break

    Resultado.delete(0,END)
    Resultado.insert(0, ''.join(reversed(residuos)))


def agregar_potencia():
    Resultado.insert(END, "^")

def agregar_raiz():
    Resultado.insert(END, "√")

def agregar_porcentaje():
    Resultado.insert(END, "%")

def toBase10(base: int):
    lista = [*Resultado.get()]
    resultadox = 0
    exponente = 0
    for n in reversed(lista):
        if n.isalpha(): n = letraHexadecimal(n)
        resultadox += int(n) * base ** exponente
        exponente += 1
    Resultado.delete(0, END)
    Resultado.insert(0, resultadox)

i=0
def obtener(dato):
    global i
    nueva_cadena = Resultado.get()
    if dato == '.' and '.' in nueva_cadena:
        return
    i+=1
    Resultado.insert(i, dato)
	
def operacion():
    global i

    ecuacion = Resultado.get()
    if i != 0:
        if "^" in ecuacion:
            base, exponente = ecuacion.split("^")
            try:
                base = float(base.strip())
                exponente = float(exponente.strip())
                resultado = base ** exponente
                Resultado.delete(0, END)
                Resultado.insert(0, resultado)
                longitud = len(str(resultado))
                i = longitud
                return  
            except ValueError:
                pass 

        if "√" in ecuacion:
            indice, numero = ecuacion.split("√", 1)
            try:
                indice = float(indice.strip())
                numero = float(numero.strip())
                resultado = pow(numero, 1 / indice)
                Resultado.delete(0, END)
                Resultado.insert(0, resultado)
                longitud = len(str(resultado))
                i = longitud
                return  
            except ValueError:
                pass  
        if "%" in ecuacion:
            valor, porcentaje = ecuacion.split("%")
            try:
                valor = float(valor.strip())
                porcentaje = float(porcentaje.strip())
                resultado = (valor * porcentaje) / 100
                Resultado.delete(0, END)
                Resultado.insert(0, resultado)
                longitud = len(str(resultado))
                i = longitud
                return  
            except ValueError:
                pass  

        try:
            result = str(eval(ecuacion))
            Resultado.delete(0, END)
            Resultado.insert(0, result)
            longitud = len(result)
            i = longitud
        except:
            result = 'ERROR'
            Resultado.delete(0, END)
            Resultado.insert(0, result)
    else:
        pass


def borrar_uno():
	global i 
	if i==-1:
		pass
	else:
		Resultado.delete(i,last =None)
		i-=1
		
def borrar_todo():
	Resultado.delete(0, END)	
	i=0

def calcular_factorial():
    try:
        numero = int(Resultado.get())
        resultado = math.factorial(numero)
        Resultado.delete(0, END)
        Resultado.insert(0, resultado)
    except ValueError:
        Resultado.delete(0, END)
        Resultado.insert(0, "ERROR")



def calcular_absoluto():
    try:
        numero = float(Resultado.get())
        resultado = abs(numero)
        Resultado.delete(0, END)
        Resultado.insert(0, resultado)
    except ValueError:
        Resultado.delete(0, END)
        Resultado.insert(0, "ERROR")

def calcular_log10():
    try:
        numero = float(Resultado.get())
        resultado = math.log10(numero)
        Resultado.delete(0, END)
        Resultado.insert(0, resultado)
    except ValueError:
        Resultado.delete(0, END)
        Resultado.insert(0, "ERROR")




frame = Frame(ventana, bg ='#999AB8', relief = "raised")
frame.grid(column=0, row=0, padx=6, pady=3)

Resultado = Entry(frame,bg='#A8BCAC', width=18, relief='groove', font = 'Montserrat 16',justify = 'right')
Resultado.grid(columnspan=4 , row=0, pady=3,padx=1, ipadx=1, ipady=1) 

#fila 1

Button_DecimalAHexadecimal = HoverButton(frame, text= "D->H", borderwidth=2, height=2, width=5,
                                        font= ('Comic sens MC',12,'bold'), relief = "raised",
                                        activebackground="#B2BBBF", bg='#000000', fg='#FFFFFF',
                                        anchor="center",command=lambda: fromaBase10(16))  

Button_DecimalAHexadecimal.grid(column = 0, row=1, pady=1, padx=3)

Button_DecimalABinario = HoverButton(frame, text= "D->B", borderwidth=2, height=2, width=5,
                                    font= ('Comic sens MC',12,'bold'), relief = "raised",
                                    activebackground="#B2BBBF", bg='#000000', fg='#FFFFFF', 
                                    anchor="center",command=lambda: fromaBase10(2))  

Button_DecimalABinario.grid(column = 1, row=1, pady=1,padx=1)

Button_BinarioADecimal = HoverButton(frame, text= "B->D", borderwidth=2, height=2, width=5,
                                    font= ('Comic sens MC',12,'bold'), relief = "raised",
                                    activebackground="#B2BBBF", bg='#000000', fg='#FFFFFF',
                                    anchor="center",command=lambda: toBase10(2))  

Button_BinarioADecimal.grid(column = 2, row=1, pady=1,padx=1)

Button_DecimalAOctagonal = HoverButton(frame, text= "D->O", borderwidth=2, height=2, width=5,
                                        font= ('Comic sens MC',12,'bold'), relief = "raised",
                                        activebackground="#B2BBBF", bg='#000000', fg='#FFFFFF',
                                        anchor="center",command=lambda: fromaBase10(8)) 
 
Button_DecimalAOctagonal.grid(column = 3, row=1, pady=2,padx=2)


#fila 2

Button_log10 = HoverButton(frame, text= "log10", borderwidth=2, height=2, width=5,
                            font= ('Comic sens MC',12,'bold'),relief = "raised",
                            activebackground="#B2BBBF",bg='#000000', fg='#FFFFFF',
                            anchor="center", command=lambda: calcular_log10())  

Button_log10.grid( column= 0 ,row=2, pady=1,padx=3)


Button_agregar_potencia = HoverButton(frame, text= "^", height=2, width=5,
                                    font=('Comic sens MC', 12, 'bold'), borderwidth=2, relief="raised",
                                    activebackground="#B2BBBF", bg='#000000', fg='#FFFFFF',
                                    anchor="center", command=lambda: agregar_potencia())

Button_agregar_potencia.grid(column=1, row=2, pady=1, padx=1)
 

Button_OctagonalADecimal = HoverButton(frame, text= "O->D", borderwidth=2, height=2, width=5,
                                        font= ('Comic sens MC',12,'bold'),relief = "raised",
                                        activebackground="#B2BBBF", bg='#000000', fg='#FFFFFF', 
                                        anchor="center", command=lambda: toBase10(8)) 
 
Button_OctagonalADecimal.grid(column= 2 ,row=2, pady=1,padx=1)

Button_HexadecimalADecimal = HoverButton(frame, text= "H->D", borderwidth=2, height=2, width=5,
                                        font= ('Comic sens MC',12,'bold'),relief = "raised",
                                        activebackground="#B2BBBF", bg='#000000', fg='#FFFFFF', 
                                        anchor="center", command=lambda: toBase10(16))  

Button_HexadecimalADecimal.grid(column= 3 ,row=2, pady=2,padx=2)

#fila 3

Button_factorial = HoverButton(frame, text= "n!", borderwidth=2, height=2, width=5,
                                font= ('Comic sens MC',12,'bold'),relief = "raised",
                                activebackground="#B2BBBF",bg='#000000', fg='#FFFFFF',
                                anchor="center", command=lambda: calcular_factorial())  

Button_factorial.grid( column= 0 ,row=3, pady=1,padx=1)

Button_agregar_raiz = HoverButton(frame, text="√", height=2, width=5,
                                  font=('Comic sens MC', 12, 'bold'), borderwidth=2, relief="raised",
                                  activebackground="#B2BBBF", bg='#000000', fg='#FFFFFF',
                                  anchor="center", command=agregar_raiz)

Button_agregar_raiz.grid(column=1, row=3, pady=1, padx=1)

Button_porcentaje = HoverButton(frame, text= "%", height=2, width=5,
                                font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                                activebackground="#B2BBBF",bg='#000000', fg='#FFFFFF',
                                anchor="center",command=lambda: agregar_porcentaje())  

Button_porcentaje.grid(column =2, row=3, pady=1,padx=1)

Button_absoluto = HoverButton(frame, text= "ABS", height=2, width=5,
                              font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                              activebackground="#B2BBBF", bg='#000000', fg='#FFFFFF',   
                              anchor="center",command=lambda: calcular_absoluto())   

Button_absoluto.grid(column =3, row=3, pady=2,padx=2)


#fila 4
Button1 = HoverButton(frame, text= "1", borderwidth=2, height=2, width=5, 
                      font= ('Comic sens MC',12,'bold'),relief = "raised", 
                      activebackground="#B2BBBF", bg ='#68777D', fg='#FFFFFF', 
                      anchor="center", command=lambda: obtener(1))  

Button1.grid( column= 0 ,row=4, pady=1,padx=3)

Button2 = HoverButton(frame, text= "2", height=2, width=5, 
                      font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                      activebackground="#B2BBBF",bg ='#68777D', fg='#FFFFFF', 
                      anchor="center",command=lambda: obtener(2))  

Button2.grid(column =1 , row=4, pady=1,padx=1)

Button3 = HoverButton(frame, text= "3", height=2, width=5,
                      font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                      activebackground="#B2BBBF", bg ='#68777D', fg='#FFFFFF', 
                      anchor="center",command=lambda: obtener(3))  

Button3.grid(column =2, row=4, pady=1,padx=1)

Button_borrar = HoverButton(frame, text= "⌫", height=2, width=5,
                            font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                            activebackground="#B2BBBF", bg='#D80D0D', fg='#FFFFFF',   
                            anchor="center",command=lambda: borrar_uno())  

Button_borrar.grid(column =3, row=4, pady=2,padx=2)

#fila 5
Button4 = HoverButton(frame, text= "4",height=2, width=5,
                      font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                      activebackground="#B2BBBF", bg ='#68777D', fg='#FFFFFF', 
                      anchor="center",command=lambda: obtener(4))  

Button4.grid( column= 0 ,row=5, pady=1,padx=1)

Button5 = HoverButton(frame, text= "5", height=2, width=5,
                      font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                      activebackground="#B2BBBF",bg ='#68777D', fg='#FFFFFF', 
                      anchor="center",command=lambda: obtener(5))  

Button5.grid(column =1 , row=5, pady=1,padx=1)

Button6 = HoverButton(frame, text= "6", height=2, width=5,
                      font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                      activebackground="#B2BBBF",bg ='#68777D',  fg='#FFFFFF', 
                      anchor="center",command=lambda: obtener(6))  

Button6.grid(column =2, row=5, pady=1,padx=1)

Button_mas = HoverButton(frame, text= "+", height=2, width=5,
                         font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                         activebackground="#B2BBBF", bg='#000000', fg='#FFFFFF',   
                         anchor="center",command=lambda: obtener('+'))  

Button_mas.grid(column =3, row=5, pady=2,padx=2)

#fila 6
Button7 = HoverButton(frame, text= "7",height=2, width=5, 
                      font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                      activebackground="#B2BBBF",bg ='#68777D',  fg='#FFFFFF', 
                      anchor="center",command=lambda: obtener(7))  

Button7.grid( column= 0 ,row=6, pady=1,padx=1)

Button8 = HoverButton(frame, text= "8", height=2, width=5,
                      font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                      activebackground="#B2BBBF",bg ='#68777D', fg='#FFFFFF', 
                      anchor="center",command=lambda: obtener(8))  

Button8.grid(column =1 , row=6, pady=1,padx=1)

Button9 = HoverButton(frame, text= "9", height=2, width=5,
                      font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                      activebackground="#B2BBBF",bg ='#68777D',  fg='#FFFFFF', 
                      anchor="center",command=lambda: obtener(9))  

Button9.grid(column =2, row=6, pady=1,padx=1)

Button_menos = HoverButton(frame, text= "-", height=2, width=5,
                           font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                           activebackground="#B2BBBF", bg='#000000', fg='#FFFFFF',   
                           anchor="center",command=lambda: obtener('-')) 
 
Button_menos.grid(column =3, row=6, pady=2,padx=2)
#68777D
#999AB8
#fila 7
Button0 = HoverButton(frame, text= "0",height=5, width=5,
                      font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                      activebackground="#B2BBBF",bg ='#68777D',  fg='#FFFFFF', 
                      anchor="center",command=lambda: obtener(0)) 
 
Button0.grid( column= 0, rowspan=2, row=7, pady=1,padx=1)

Button_punto = HoverButton(frame, text= ".", height=2, width=5,
                           font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                           activebackground="#B2BBBF",bg ='#68777D', fg='#FFFFFF', 
                           anchor="center",command=lambda: obtener('.'))  

Button_punto.grid(column =1 , row=7, pady=1,padx=1)

Button_entre = HoverButton(frame, text= "÷", height=2, width=5,
                           font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                           activebackground="#B2BBBF",bg='#000000', fg='#FFFFFF',  
                           anchor="center",command=lambda: obtener('/'))  

Button_entre.grid(column =2, row=7, pady=1,padx=1)

Button_por = HoverButton(frame, text= "x", height=2, width=5,
                         font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                         activebackground="#B2BBBF", bg='#000000', fg='#FFFFFF',  
                         anchor="center",command=lambda: obtener('*'))  

Button_por.grid(column =3, row=7, pady=2,padx=2)



#fila 8
Button_igual = HoverButton(frame, text= "=", height=2, width=12,
                           font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", 
                           activebackground="#B2BBBF", bg='#000000', fg='#FFFFFF', 
                           anchor="center",command=lambda: operacion())  

Button_igual.grid(column =1 ,columnspan=2, row=8, pady=1,padx=1)


Button_borrar = HoverButton(frame, text= "C", height=2, width=5,
                            font= ('Comic sens MC',12,'bold'), borderwidth=2, relief = "raised", 
                            activebackground="#B2BBBF", bg='#FD5603', fg='#FFFFFF', 
                            anchor="center",command=lambda: borrar_todo()) 

Button_borrar.grid(column =3, row=8, pady=2,padx=2)

ventana.mainloop()