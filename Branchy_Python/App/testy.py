#Import the required Libraries
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import threading
import time
import sys
from pathlib import Path
import winsound

##########

class myGlobal():
    # variable for killing process in the end
    main_stays_alive = True

    # Set up first directory of the story
    Uri_story_start = "../Yuki_Sleeps_Adventure/"  # the first directory of the story
    Uri_story_current = ""  # the subdirectory inside the story
    current_count_int = 1  # the current page or the node


# define the event handlers for moving left-right
def spacebar_pressed(event):
    print("spacebar_pressed")
    myGlobal.current_count_int = (myGlobal.current_count_int % 3) + 1
    Show_Story_Page(myGlobal.Uri_story_start + myGlobal.Uri_story_current, myGlobal.current_count_int)

def one_pressed(event):
    print("one_pressed")
    myGlobal.current_count_int = 1
    myGlobal.Uri_story_current = myGlobal.Uri_story_current + "1/"
    Show_Story_Page(myGlobal.Uri_story_start+ myGlobal.Uri_story_current, myGlobal.current_count_int)

def two_pressed(event):
    print("two_pressed")
    myGlobal.current_count_int = 1
    myGlobal.Uri_story_current = myGlobal.Uri_story_current + "2/"
    Show_Story_Page(myGlobal.Uri_story_start+ myGlobal.Uri_story_current, myGlobal.current_count_int)


def three_pressed(event):
    print("three_pressed")
    myGlobal.current_count_int = 1
    myGlobal.Uri_story_current = myGlobal.Uri_story_current + "3/"
    Show_Story_Page(myGlobal.Uri_story_start+ myGlobal.Uri_story_current, myGlobal.current_count_int)



def Show_Story_Page(node, page_number):
  print("Hello from a Show_Story_Page")
  print("page=>" + node + " . " + str(page_number) )
  #
  # # Show text, image, and play voice
  Show_text(node, page_number)
  Show_image(node, page_number)
  # Play_Voice(node, page_number)

##################


def Show_text(node, page_number):
      x = node + "text_" + "{:02d}".format(page_number) + ".txt"
      print(x)




def Show_image(node, page_number):
    x = node + "pic_" + "{:02d}".format(page_number) + ".png"
    print(x)
    image = Image.open(x)
    tk_image = ImageTk.PhotoImage(image)
    canvas.create_image(1,1,anchor=NW, image=tk_image)
    canvas.pack()
    canvas.update()
    root.update()


def Play_Voice(node, page_number):
    x = node + "voice_" + "{:02d}".format(page_number) + ".wav"
    print(x)
    winsound.PlaySound(x, winsound.SND_FILENAME)















####################
#Create an instance of tkinter frame
root = Tk()

#Set the geometry of tkinter frame
root.geometry("750x250")

text_instructions = tk.Text(root, height=1, width=100,font=("Helvetica", 18))
text_instructions.place(relwidth=0, relheight=0)
text_instructions.pack()
text_instructions.insert(tk.END, "Press key 1, 2 or 3 to select a path.")

#Create a canvas
canvas= Canvas(root, width= 1000, height= 500)
canvas.pack()

#Load an image in the script
img= ImageTk.PhotoImage(Image.open("pic_01.png"))

#Add image to the Canvas Items
canvas.create_image(0,0,anchor=NW,image=img)



# Bind arrow keys to functions
root.bind('<space>', spacebar_pressed)
root.bind('1', one_pressed)
root.bind('2', two_pressed)
root.bind('3', three_pressed)


###############


current_directory = Path.cwd()
print("Current Dir => " + str(current_directory))


Show_Story_Page(myGlobal.Uri_story_start, 1)


root.mainloop()
##############

root.mainloop()