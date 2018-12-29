import tkinter as tk
import winsound as ws
import random 
from tkinter import messagebox
from collections import OrderedDict


root = tk.Tk()
root.title("Interval Ear Trainging")
frame = tk.Frame(root)
frame.grid()
scale = {'C5': 0,'C#5': 1, 'D5' : 2,'D#5' : 3,'E5': 4, 'F5' : 5,  'F#5': 6, 'G5' : 7,'G#5': 8, 'A5' : 9, 'A#5': 10, 'B5' : 11}
x = ["C5.wav","C#5.wav", "D5.wav","D#5.wav","E5.wav","F5.wav", "F#5.wav","G5.wav","G#5.wav","A5.wav", "A#5.wav","B5.wav"]
ordered =  OrderedDict()
ordered["Unison"] = 0
ordered["Minor 2nd"] = 1
ordered["Major 2nd"] = 2
ordered["Minor 3rd"] = 3
ordered["Major 3rd"] = 4
ordered["Perfect 4th"] = 5
ordered["Diminished 5th"] = 6
ordered["Perfect 5th"] = 7
ordered["Minor 6th"] = 8
ordered["Major 6th"] = 9
ordered["Minor 7th"] = 10
ordered["Major 7th"] = 11

def mapper(x):
	if x == 2 or x == 3 or x == 4:
		x = 2
	if x == 5 or x == 6 or x == 7:
		x = 3
	if x == 8 or x == 9 or x == 10:
		x = 4
	if x == 11 or x == 12 or x == 13:
		x = 5
	return x
def genBut(x):
	rand1 = random.randint(0,len(x) - 1)
	rand2 = random.randint(0,len(x) - 1)
	play1 = lambda : ws.PlaySound(x[rand1], ws.SND_FILENAME)
	play2 = lambda : ws.PlaySound(x[rand2], ws.SND_FILENAME)
	button1 = tk.Button(frame, text = "note 1", command = play1, height = 1, width = 12).grid(row = 0, column = 0)
	button2 = tk.Button(frame, text = "note 2", command = play2, height = 1, width = 12).grid(row = 0, column = 1)
	a = x[rand1].split('.')
	b = x[rand2].split('.')
	return a[0], b[0]
def genAns(x,y,z):
	inter = abs(scale[y] - scale[z])
	i = 0
	r = 2
	c = 0 
	answer = ""
	def trump():
		messagebox.showinfo("Wrong","idiot")
	def yup():
		messagebox.showinfo("Right", "nice")
		quit()
	for i in range(0,3):
		button = tk.Label(frame,text = '   ---   ').grid(row = 1, column = i)
	for key in x:
		if inter == x[key]:
			button = tk.Button(frame, text = key, command = yup, height = 1, width = 12).grid(row = mapper(r), column = c % 3)
			passer = key.split('.')
			answer = passer[0]
		else:
			button = tk.Button(frame, text = key, command = trump, height = 1, width = 12).grid(row = mapper(r), column = c % 3)
		r += 1
		c += 1
	for i in range(0,3):
		button = tk.Label(frame,text = '   ---   ').grid(row = 6, column = i)
	def quitter():
		messagebox.showinfo("Shame", answer)
	button = tk.Button(frame, text = "Give Up", command = quitter, height = 1, width = 12).grid(row =7, column = 0)
def doStuff(x,y):
	s,t = genBut(x)
	genAns(ordered,s,t)
doStuff(x,ordered)
root.mainloop()