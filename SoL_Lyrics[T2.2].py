#Example (Hello, World):
from codeop import CommandCompiler
from distutils.command.config import config
from distutils.dir_util import create_tree
from os import terminal_size
import tkinter
from tkinter import messagebox #in python 3.x: tkinter wird kleingeschrieben
import webbrowser

tk = tkinter.Tk()

frame = tkinter.Frame(tk, relief="ridge", borderwidth=5)
frame.pack(fill="both",expand=1)
label = tkinter.Label(frame, text="v.0.0.1")
label.pack(expand=2)
label2 = tkinter.Label(frame, text="Streets of London Lyrics [Teil 2/2]")
label2.pack(expand=2)
label3 = tkinter.Label(frame, text="----------------------------------------------------------------------------------------------------- ")
label3.pack(expand=2)
############################################
label4 = tkinter.Label(frame, text="In the all night cafe")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="At a quarter past eleven")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="Same old man")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="Sitting there on his own")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="Looking at the world")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="Over the rim of his tea cup")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="Each tea lasts an hour")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="And he wanders home alone")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="So, how can you tell me you're lonely?")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="Don't say for you that the sun don't shine")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="Let me take you by the hand")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="And lead you through the streets of London")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="Show you something to make you change your mind")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="Have you seen the old man")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="Outside the seaman's mission")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="Memory fading with")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="The medal ribbons that he wears?")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="n our winter city")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="The rain cries a little pity")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="For one more forgotten hero")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="And a world that doesn't care")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="So, how can you tell me you're lonely")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="And say for you that the sun don't shine?")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="Let me take you by the hand")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="And lead you through the streets of London")
label4.pack(expand=2)
label4 = tkinter.Label(frame, text="I'll show you something to make you change your mind")
label4.pack(expand=2)
label3 = tkinter.Label(frame, text="----------------------------------------------------------------------------------------------------- ")
label3.pack(expand=2)







button = tkinter.Button(frame,text="Exit",command=tk.destroy) #.destroy
button.pack(side="bottom")

tk.mainloop()