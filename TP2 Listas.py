from tkinter import*
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

window = Tk()
window.title("Programación II - Notas de un Curso")
window.geometry('1560x780')

notas_Alumnos =  [0,0,0,0,0,0,0,0,0,0,0,0]
#FUNCIONES
def cambiar_Nota_Est1():
    ventanaIngresar = tk.Toplevel(window)
    ventanaIngresar.title("Ingresar Datos")
    ventanaIngresar.geometry("240x180")
    Label_1 = Label(ventanaIngresar, text="Ingrese la nueva calificacion\ndel Alumno")
    Label_1.grid (column = 0, row = 0,sticky = 'n')
    Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_1.grid (column = 0, row = 1)
    Entry_1.focus()
    btn = Button (ventanaIngresar,text = 'AGREGAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
    btn.grid (column = 0, row = 2)
    def agregar():
        while getdouble(Entry_1.get()) >= 0 and getdouble(Entry_1.get()) <= 5:
            notas_Alumnos.pop(0)
            nva_Nota = getdouble(Entry_1.get())
            notas_Alumnos.insert(0,nva_Nota)
            lbl_fila1C3.configure(text=(getdouble(nva_Nota)))
            ventanaIngresar.destroy()
        else:
            messagebox.showinfo(title ='ATENCION',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
            Entry_1.focus()

def cambiar_Nota_Est2():
    ventanaIngresar = tk.Toplevel(window)
    ventanaIngresar.title("Ingresar Datos")
    ventanaIngresar.geometry("240x180")
    Label_1 = Label(ventanaIngresar, text="Ingrese la nueva calificacion\ndel Alumno")
    Label_1.grid (column = 0, row = 0,sticky = 'n')
    Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_1.grid (column = 0, row = 1)
    Entry_1.focus()
    btn = Button (ventanaIngresar,text = 'AGREGAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
    btn.grid (column = 0, row = 2)
    def agregar():
        if getdouble(Entry_1.get()) >= 0 and getdouble(Entry_1.get()) <= 5:
            notas_Alumnos.pop(1)
            nva_Nota = getdouble(Entry_1.get())
            notas_Alumnos.insert(1,nva_Nota)
            lbl_fila2C3.configure(text=getdouble(nva_Nota))
            ventanaIngresar.destroy()
        else:
            messagebox.showinfo(title ='ATENCION',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
            Entry_1.focus()

def cambiar_Nota_Est3():
    ventanaIngresar = tk.Toplevel(window)
    ventanaIngresar.title("Ingresar Datos")
    ventanaIngresar.geometry("240x180")
    Label_1 = Label(ventanaIngresar, text="Ingrese la nueva calificacion\ndel Alumno")
    Label_1.grid (column = 0, row = 0,sticky = 'n')
    Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_1.grid (column = 0, row = 1)
    Entry_1.focus()
    btn = Button (ventanaIngresar,text = 'AGREGAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
    btn.grid (column = 0, row = 2)
    def agregar():
        if getdouble(Entry_1.get()) >= 0 and getdouble(Entry_1.get()) <= 5:
            notas_Alumnos.pop(0)
            nva_Nota = getdouble(Entry_1.get())
            notas_Alumnos.insert(0,nva_Nota)
            lbl_fila3C3.configure(text=(getdouble(nva_Nota)))
            ventanaIngresar.destroy()
        else:
            messagebox.showinfo(title ='ATENCION',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
            Entry_1.focus()

def cambiar_Nota_Est4():
    ventanaIngresar = tk.Toplevel(window)
    ventanaIngresar.title("Ingresar Datos")
    ventanaIngresar.geometry("240x180")
    Label_1 = Label(ventanaIngresar, text="Ingrese la nueva calificacion\ndel Alumno")
    Label_1.grid (column = 0, row = 0,sticky = 'n')
    Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_1.grid (column = 0, row = 1)
    Entry_1.focus()
    btn = Button (ventanaIngresar,text = 'AGREGAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
    btn.grid (column = 0, row = 2)
    def agregar():
        if getdouble(Entry_1.get()) >= 0 and getdouble(Entry_1.get()) <= 5:
            notas_Alumnos.pop(0)
            nva_Nota = getdouble(Entry_1.get())
            notas_Alumnos.insert(0,nva_Nota)
            lbl_fila4C3.configure(text=(getdouble(nva_Nota)))
            ventanaIngresar.destroy()
        else:
            messagebox.showinfo(title ='ATENCION',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
            Entry_1.focus()

def cambiar_Nota_Est5():
    ventanaIngresar = tk.Toplevel(window)
    ventanaIngresar.title("Ingresar Datos")
    ventanaIngresar.geometry("240x180")
    Label_1 = Label(ventanaIngresar, text="Ingrese la nueva calificacion\ndel Alumno")
    Label_1.grid (column = 0, row = 0,sticky = 'n')
    Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_1.grid (column = 0, row = 1)
    Entry_1.focus()
    btn = Button (ventanaIngresar,text = 'AGREGAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
    btn.grid (column = 0, row = 2)
    def agregar():
        if getdouble(Entry_1.get()) >= 0 and getdouble(Entry_1.get()) <= 5:
            notas_Alumnos.pop(0)
            nva_Nota = getdouble(Entry_1.get())
            notas_Alumnos.insert(0,nva_Nota)
            lbl_fila5C3.configure(text=(getdouble(nva_Nota)))
            ventanaIngresar.destroy()
        else:
            messagebox.showinfo(title ='ATENCION',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
            Entry_1.focus()

def cambiar_Nota_Est6():
    ventanaIngresar = tk.Toplevel(window)
    ventanaIngresar.title("Ingresar Datos")
    ventanaIngresar.geometry("240x180")
    Label_1 = Label(ventanaIngresar, text="Ingrese la nueva calificacion\ndel Alumno")
    Label_1.grid (column = 0, row = 0,sticky = 'n')
    Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_1.grid (column = 0, row = 1)
    Entry_1.focus()
    btn = Button (ventanaIngresar,text = 'AGREGAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
    btn.grid (column = 0, row = 2)
    def agregar():
        if getdouble(Entry_1.get()) >= 0 and getdouble(Entry_1.get()) <= 5:
            notas_Alumnos.pop(0)
            nva_Nota = getdouble(Entry_1.get())
            notas_Alumnos.insert(0,nva_Nota)
            lbl_fila6C3.configure(text=(getdouble(nva_Nota)))
            ventanaIngresar.destroy()
        else:
            messagebox.showinfo(title ='ATENCION',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
            Entry_1.focus()

def cambiar_Nota_Est7():
    ventanaIngresar = tk.Toplevel(window)
    ventanaIngresar.title("Ingresar Datos")
    ventanaIngresar.geometry("240x180")
    Label_1 = Label(ventanaIngresar, text="Ingrese la nueva calificacion\ndel Alumno")
    Label_1.grid (column = 0, row = 0,sticky = 'n')
    Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_1.grid (column = 0, row = 1)
    Entry_1.focus()
    btn = Button (ventanaIngresar,text = 'AGREGAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
    btn.grid (column = 0, row = 2)
    def agregar():
        if getdouble(Entry_1.get()) >= 0 and getdouble(Entry_1.get()) <= 5:
            notas_Alumnos.pop(0)
            nva_Nota = getdouble(Entry_1.get())
            notas_Alumnos.insert(0,nva_Nota)
            lbl_fila7C3.configure(text=(getdouble(nva_Nota)))
            ventanaIngresar.destroy()
        else:
            messagebox.showinfo(title ='ATENCION',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
            Entry_1.focus()

def cambiar_Nota_Est8():
    ventanaIngresar = tk.Toplevel(window)
    ventanaIngresar.title("Ingresar Datos")
    ventanaIngresar.geometry("240x180")
    Label_1 = Label(ventanaIngresar, text="Ingrese la nueva calificacion\ndel Alumno")
    Label_1.grid (column = 0, row = 0,sticky = 'n')
    Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_1.grid (column = 0, row = 1)
    Entry_1.focus()
    btn = Button (ventanaIngresar,text = 'AGREGAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
    btn.grid (column = 0, row = 2)
    def agregar():
        if getdouble(Entry_1.get()) >= 0 and getdouble(Entry_1.get()) <= 5:
            notas_Alumnos.pop(0)
            nva_Nota = getdouble(Entry_1.get())
            notas_Alumnos.insert(0,nva_Nota)
            lbl_fila8C3.configure(text=(getdouble(nva_Nota)))
            ventanaIngresar.destroy()
        else:
            messagebox.showinfo(title ='ATENCION',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
            Entry_1.focus()

def cambiar_Nota_Est9():
    ventanaIngresar = tk.Toplevel(window)
    ventanaIngresar.title("Ingresar Datos")
    ventanaIngresar.geometry("240x180")
    Label_1 = Label(ventanaIngresar, text="Ingrese la nueva calificacion\ndel Alumno")
    Label_1.grid (column = 0, row = 0,sticky = 'n')
    Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_1.grid (column = 0, row = 1)
    Entry_1.focus()
    btn = Button (ventanaIngresar,text = 'AGREGAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
    btn.grid (column = 0, row = 2)
    def agregar():
        if getdouble(Entry_1.get()) >= 0 and getdouble(Entry_1.get()) <= 5:
            notas_Alumnos.pop(0)
            nva_Nota = getdouble(Entry_1.get())
            notas_Alumnos.insert(0,nva_Nota)
            lbl_fila9C3.configure(text=(getdouble(nva_Nota)))
            ventanaIngresar.destroy()
        else:
            messagebox.showinfo(title ='ATENCION',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
            Entry_1.focus()

def cambiar_Nota_Est10():
    ventanaIngresar = tk.Toplevel(window)
    ventanaIngresar.title("Ingresar Datos")
    ventanaIngresar.geometry("240x180")
    Label_1 = Label(ventanaIngresar, text="Ingrese la nueva calificacion\ndel Alumno")
    Label_1.grid (column = 0, row = 0,sticky = 'n')
    Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_1.grid (column = 0, row = 1)
    Entry_1.focus()
    btn = Button (ventanaIngresar,text = 'AGREGAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
    btn.grid (column = 0, row = 2)
    def agregar():
        if getdouble(Entry_1.get()) >= 0 and getdouble(Entry_1.get()) <= 5:
            notas_Alumnos.pop(0)
            nva_Nota = getdouble(Entry_1.get())
            notas_Alumnos.insert(0,nva_Nota)
            lbl_fila10C3.configure(text=(getdouble(nva_Nota)))
            ventanaIngresar.destroy()
        else:
            messagebox.showinfo(title ='ATENCION',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
            Entry_1.focus()

def cambiar_Nota_Est11():
    ventanaIngresar = tk.Toplevel(window)
    ventanaIngresar.title("Ingresar Datos")
    ventanaIngresar.geometry("240x180")
    Label_1 = Label(ventanaIngresar, text="Ingrese la nueva calificacion\ndel Alumno")
    Label_1.grid (column = 0, row = 0,sticky = 'n')
    Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_1.grid (column = 0, row = 1)
    Entry_1.focus()
    btn = Button (ventanaIngresar,text = 'AGREGAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
    btn.grid (column = 0, row = 2)
    def agregar():
        if getdouble(Entry_1.get()) >= 0 and getdouble(Entry_1.get()) <= 5:
            notas_Alumnos.pop(0)
            nva_Nota = getdouble(Entry_1.get())
            notas_Alumnos.insert(0,nva_Nota)
            lbl_fila11C3.configure(text=(getdouble(nva_Nota)))
            ventanaIngresar.destroy()
        else:
            messagebox.showinfo(title ='ATENCION',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
            Entry_1.focus()

def cambiar_Nota_Est12():
    ventanaIngresar = tk.Toplevel(window)
    ventanaIngresar.title("Ingresar Datos")
    ventanaIngresar.geometry("240x180")
    Label_1 = Label(ventanaIngresar, text="Ingrese la nueva calificacion\ndel Alumno")
    Label_1.grid (column = 0, row = 0,sticky = 'n')
    Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_1.grid (column = 0, row = 1)
    Entry_1.focus()
    btn = Button (ventanaIngresar,text = 'AGREGAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
    btn.grid (column = 0, row = 2)
    def agregar():
        if getdouble(Entry_1.get()) >= 0 and getdouble(Entry_1.get()) <= 5:
            notas_Alumnos.pop(0)
            nva_Nota = getdouble(Entry_1.get())
            notas_Alumnos.insert(0,nva_Nota)
            lbl_fila12C3.configure(text=(getdouble(nva_Nota)))
            ventanaIngresar.destroy()
        else:
            messagebox.showinfo(title ='ATENCION',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
            Entry_1.focus()


def Promedio_de_Notas ():
    num = 0
    for notas in notas_Alumnos:
        num += notas
    Promedio = round( num / len(notas_Alumnos),2)
    return Promedio
def Show_Promedio ():
    messagebox.showinfo(title ='PROMEDIO',message = str(Promedio_de_Notas()), icon = 'info')



def nota_Mayor():
    contador = 0
    for notas in notas_Alumnos:
        if notas > Promedio_de_Notas() :
            contador += 1
    messagebox.showinfo(title ='Estudiantes Mayores al Promedio',message = str(contador), icon = 'info')


ventana = Frame(window)
ventana.grid(column = 0, row = 0,sticky = 'w')
ventana.config(bd=5,relief="ridge")


image = Image.open (r"C:\Users\Pablo\Pictures\alumnos.jpg")
new_image = image.resize((620,525))
background_image = ImageTk.PhotoImage(new_image)
background_label = tk.Label(ventana,image=background_image,height = 525, width = 620)
background_label.grid(column = 0, row =0)


ventana_Estudiantes = Frame(window)
ventana_Estudiantes.grid(column = 1, row = 0,sticky = 'w')
ventana_Estudiantes.config(bd=5,relief="ridge")


lbl_fila1 = Label(ventana_Estudiantes, text = 'Estudiante 1:\n', font= ('Arial',10))
lbl_fila1.grid (column = 1, row = 2, sticky = 'w')

lbl_fila2 = Label(ventana_Estudiantes, text = 'Estudiante 2:\n', font= ('Arial',10))
lbl_fila2.grid (column = 1, row = 3, sticky = 'w')

lbl_fila3 = Label(ventana_Estudiantes, text = 'Estudiante 3:\n', font= ('Arial',10))
lbl_fila3.grid (column = 1, row = 4, sticky = 'w')

lbl_fila4 = Label(ventana_Estudiantes, text = 'Estudiante 4:\n', font= ('Arial',10))
lbl_fila4.grid (column = 1, row = 5, sticky = 'w')

lbl_fila5 = Label(ventana_Estudiantes, text = 'Estudiante 5:\n', font= ('Arial',10))
lbl_fila5.grid (column = 1, row = 6, sticky = 'w')

lbl_fila6 = Label(ventana_Estudiantes, text = 'Estudiante 6:\n', font= ('Arial',10))
lbl_fila6.grid (column = 1, row = 7, sticky = 'w')

lbl_fila7 = Label(ventana_Estudiantes, text = 'Estudiante 7:\n', font= ('Arial',10))
lbl_fila7.grid (column = 1, row = 8, sticky = 'w')

lbl_fila8 = Label(ventana_Estudiantes, text = 'Estudiante 8:\n', font= ('Arial',10))
lbl_fila8.grid (column = 1, row = 9, sticky = 'w')

lbl_fila9 = Label(ventana_Estudiantes, text = 'Estudiante 9:\n', font= ('Arial',10))
lbl_fila9.grid (column = 1, row = 10, sticky = 'w')

lbl_fila10 = Label(ventana_Estudiantes, text = 'Estudiante 10:\n', font= ('Arial',10))
lbl_fila10.grid (column = 1, row = 11, sticky = 'w')

lbl_fila11 = Label(ventana_Estudiantes, text = 'Estudiante 11:\n', font= ('Arial',10))
lbl_fila11.grid (column = 1, row = 12, sticky = 'w')

lbl_fila12 = Label(ventana_Estudiantes, text = 'Estudiante 12:\n', font= ('Arial',10))
lbl_fila12.grid (column = 1, row = 13, sticky = 'w')
###################################################################################################################
#columna 3 Labels con las Notas de los estudiantes

lbl_fila1C3 = Label(ventana_Estudiantes, text = '0', font= ('Arial',12,'bold'),fg = 'blue',bg = 'whitesmoke',relief = 'flat', bd = 3, height = 1, width = 20)
lbl_fila1C3.grid (column = 2, row = 2, sticky = 'n')

lbl_fila2C3 = Label(ventana_Estudiantes, text = '0', font= ('Arial',12,'bold'),fg = 'blue',bg = 'whitesmoke',relief = 'flat', bd = 3, height = 1, width = 20)
lbl_fila2C3.grid (column = 2, row = 3, sticky = 'n')

lbl_fila3C3 = Label(ventana_Estudiantes, text = '0', font= ('Arial',12,'bold'),fg = 'blue',bg = 'whitesmoke',relief = 'flat', bd = 3, height = 1, width = 20)
lbl_fila3C3.grid (column = 2, row = 4, sticky = 'n')

lbl_fila4C3 = Label(ventana_Estudiantes, text = '0', font= ('Arial',12,'bold'),fg = 'blue',bg = 'whitesmoke',relief = 'flat', bd = 3, height = 1, width = 20)
lbl_fila4C3.grid (column = 2, row = 5, sticky = 'n')

lbl_fila5C3 = Label(ventana_Estudiantes, text = '0', font= ('Arial',12,'bold'),fg = 'blue',bg = 'whitesmoke',relief = 'flat', bd = 3, height = 1, width = 20)
lbl_fila5C3.grid (column = 2, row = 6, sticky = 'n')

lbl_fila6C3 = Label(ventana_Estudiantes, text = '0', font= ('Arial',12,'bold'),fg = 'blue',bg = 'whitesmoke',relief = 'flat', bd = 3, height = 1, width = 20)
lbl_fila6C3.grid (column = 2, row = 7, sticky = 'n')

lbl_fila7C3 = Label(ventana_Estudiantes, text = '0', font= ('Arial',12,'bold'),fg = 'blue',bg = 'whitesmoke',relief = 'flat', bd = 3, height = 1, width = 20)
lbl_fila7C3.grid (column = 2, row = 8, sticky = 'n')

lbl_fila8C3 = Label(ventana_Estudiantes, text = '0', font= ('Arial',12,'bold'),fg = 'blue',bg = 'whitesmoke',relief = 'flat', bd = 3, height = 1, width = 20)
lbl_fila8C3.grid (column = 2, row = 9, sticky = 'n')

lbl_fila9C3 = Label(ventana_Estudiantes, text = '0', font= ('Arial',12,'bold'),fg = 'blue',bg = 'whitesmoke',relief = 'flat', bd = 3, height = 1, width = 20)
lbl_fila9C3.grid (column = 2, row = 10, sticky = 'n')

lbl_fila10C3 = Label(ventana_Estudiantes, text = '0', font= ('Arial',12,'bold'),fg = 'blue',bg = 'whitesmoke',relief = 'flat', bd = 3, height = 1, width = 20)
lbl_fila10C3.grid (column = 2, row = 11, sticky = 'n')

lbl_fila11C3 = Label(ventana_Estudiantes, text = '0', font= ('Arial',12,'bold'),fg = 'blue',bg = 'whitesmoke',relief = 'flat', bd = 3, height = 1, width = 20)
lbl_fila11C3.grid (column = 2, row = 12, sticky = 'n')

lbl_fila12C3 = Label(ventana_Estudiantes, text = '0', font= ('Arial',12,'bold'),fg = 'blue',bg = 'whitesmoke',relief = 'flat', bd = 3, height = 1, width = 20)
lbl_fila12C3.grid (column = 2, row = 13, sticky = 'n')

#botones
btn1 = Button (ventana_Estudiantes,text = 'Cambiar',relief = 'raised',bg = 'lavender',bd = 3,height = 1, width = 15,command = lambda : [cambiar_Nota_Est1()])
btn1.grid (column = 3, row = 2,sticky = 'e')

btn2 = Button (ventana_Estudiantes,text = 'Cambiar',relief = 'raised',bg = 'lavender',bd = 3,height = 1, width = 15,command = lambda : [cambiar_Nota_Est2()])
btn2.grid (column = 3, row = 3,sticky = 'e')

btn3 = Button (ventana_Estudiantes,text = 'Cambiar',relief = 'raised',bg = 'lavender',bd = 3,height = 1, width = 15,command = lambda : [cambiar_Nota_Est3()])
btn3.grid (column = 3, row = 4,sticky = 'e')

btn4 = Button (ventana_Estudiantes,text = 'Cambiar',relief = 'raised',bg = 'lavender',bd = 3,height = 1, width = 15,command = lambda : [cambiar_Nota_Est4()])
btn4.grid (column = 3, row = 5,sticky = 'e')

btn5 = Button (ventana_Estudiantes,text = 'Cambiar',relief = 'raised',bg = 'lavender',bd = 3,height = 1, width = 15,command = lambda : [cambiar_Nota_Est5()])
btn5.grid (column = 3, row = 6,sticky = 'e')

btn6 = Button (ventana_Estudiantes,text = 'Cambiar',relief = 'raised',bg = 'lavender',bd = 3,height = 1, width = 15,command = lambda : [cambiar_Nota_Est6()])
btn6.grid (column = 3, row = 7,sticky = 'e')

btn7 = Button (ventana_Estudiantes,text = 'Cambiar',relief = 'raised',bg = 'lavender',bd = 3,height = 1, width = 15,command = lambda : [cambiar_Nota_Est7()])
btn7.grid (column = 3, row = 8,sticky = 'e')

btn8 = Button (ventana_Estudiantes,text = 'Cambiar',relief = 'raised',bg = 'lavender',bd = 3,height = 1, width = 15,command = lambda : [cambiar_Nota_Est8()])
btn8.grid (column = 3, row = 9,sticky = 'e')

btn9 = Button (ventana_Estudiantes,text = 'Cambiar',relief = 'raised',bg = 'lavender',bd = 3,height = 1, width = 15,command = lambda : [cambiar_Nota_Est9()])
btn9.grid (column = 3, row = 10,sticky = 'e')

btn10 = Button (ventana_Estudiantes,text = 'Cambiar',relief = 'raised',bg = 'lavender',bd = 3,height = 1, width = 15,command = lambda : [cambiar_Nota_Est10()])
btn10.grid (column = 3, row = 11,sticky = 'e')

btn11 = Button (ventana_Estudiantes,text = 'Cambiar',relief = 'raised',bg = 'lavender',bd = 3,height = 1, width = 15,command = lambda : [cambiar_Nota_Est11()])
btn11.grid (column = 3, row = 12,sticky = 'e')

btn12 = Button (ventana_Estudiantes,text = 'Cambiar',relief = 'raised',bg = 'lavender',bd = 3,height = 1, width = 15,command = lambda : [cambiar_Nota_Est12()])
btn12.grid (column = 3, row = 13,sticky = 'e')
###########################################################################################################################################################
#Calculos Princupales

ventana_Calculos = Frame(window)
ventana_Calculos.grid(column = 0, row = 1,sticky = 'w')
ventana_Calculos.config(bd=5,relief="ridge")

btn1_Principal = Button (ventana_Calculos,text = 'Promedio',relief = 'raised',bg = 'lavender',bd = 3,height = 1, width = 18,command = lambda : [Show_Promedio()] )
btn1_Principal.grid (column = 0, row = 14, sticky = 'w')

btn2_Principal = Button (ventana_Calculos,text = '#Mayor Promedio',relief = 'raised',bg = 'lavender',bd = 3,height = 1, width = 18,command = lambda : [nota_Mayor()])
btn2_Principal.grid (column = 1, row = 14, sticky = 'n')

btn3_Principal = Button (ventana_Calculos,text = 'Opcion 1',relief = 'raised',bg = 'lavender',bd = 3,height = 1, width = 18,state = 'disabled')
btn3_Principal.grid (column = 2, row = 14,sticky = 'n')

btn4_Principal = Button (ventana_Calculos,text = 'Opcion 2',relief = 'raised',bg = 'lavender',bd = 3,height = 1, width = 18,state = 'disabled')
btn4_Principal.grid (column = 3, row = 14,sticky = 'w')


window.mainloop()
