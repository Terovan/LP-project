from tkinter import *
from tkinter import ttk
import csv
import plotly.express as px
import pandas as pd
root = Tk()

title = Label(root, text="Cultura si Culte").pack()
myLabel1 = Label(root, text="Alegeti setul de date:").pack(anchor=W)
r = IntVar()
def grafic1():
    lines=[]
    with open('cultura.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            lines.append(line)
    basic_plot = px.line(x=lines[1], y=lines[0], title=' ')
    basic_plot.show()
def grafic2():
    lines=[]
    with open('cultura.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            lines.append(line)
    basic_plot = px.line(x=lines[2], y=lines[0], title=' ')
    basic_plot.show()
def grafic3():
    lines=[]
    with open('cultura.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            lines.append(line)
    basic_plot = px.line(x=lines[3], y=lines[0], title=' ')
    basic_plot.show()
def grafic4():
    lines=[]
    with open('cultura.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            lines.append(line)
    basic_plot = px.line(x=lines[4], y=lines[0], title=' ')
    basic_plot.show()
def grafic5():
    lines=[]
    with open('cultura.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            lines.append(line)
    basic_plot = px.line(x=lines[5], y=lines[0], title=' ')
    basic_plot.show()
def grafic6():
    lines=[]
    with open('cultura.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            lines.append(line)
        print(lines[3])
    basic_plot = px.line(x=lines[6], y=lines[0], title=' ')
    basic_plot.show()


def afisare1():
    basic_plot = px.line(x=grafic1(), y=lines[0], title=' ')
    basic_plot.show()
def afisare2():
    basic_plot = px.line(x=grafic2(), y=lines[0], title=' ')
    basic_plot.show()
def afisare3():
    basic_plot = px.line(x=grafic3(), y=lines[0], title=' ')
    basic_plot.show()
def afisare4():
    basic_plot = px.line(x=grafic4(), y=lines[0], title=' ')
    basic_plot.show()
def afisare5():
    basic_plot = px.line(x=grafic5(), y=lines[0], title=' ')
    basic_plot.show()
def afisare6():
    basic_plot = px.line(x=grafic6(), y=lines[0], title=' ')
    basic_plot.show()


def but1():
    Button(root, text='Afiseaza graficul',command=afisare1).pack()
def but2():
    Button(root, text='Afiseaza graficul',command=afisare2).pack()
def but3():
    Button(root, text='Afiseaza graficul',command=afisare3).pack()
def but4():
    Button(root, text='Afiseaza graficul',command=afisare4).pack()
def but5():
    Button(root, text='Afiseaza graficul',command=afisare5).pack()
def but6():
    Button(root, text='Afiseaza graficul',command=afisare6).pack()

Radiobutton(root, text="Numar de biblioteci", variable=r, value=1, command=but1).pack(anchor=W)
Radiobutton(root, text="Numar de biblioteci publice", variable=r, value=2, command=but2).pack(anchor=W)
Radiobutton(root, text="Numar utilizatori activi in biblioteci", variable=r, value=3, command=but3).pack(anchor=W)
Radiobutton(root, text="Numar colectii detinute in biblioteci", variable=r, value=4, command=but4).pack(anchor=W)
Radiobutton(root, text="Numar angajati in biblioteci", variable=r, value=5, command=but5).pack(anchor=W)
Radiobutton(root, text="Numar muzee", variable=r, value=6, command=but6).pack(anchor=W)
root.mainloop()
