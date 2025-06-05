__author__ = 'Russ'

#################  main.py  ##################

#
# Install python 3.5 ... python-3.5.0a1-amd64.exe
# Install PyCharm ... pycharm-educational-1.0.1.exe (or pro version)
#

# built-in module imports
from tkinter import messagebox
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import threading
import time
import sys
from pathlib import Path
import winsound

class myGlobal():
    # variable for killing process in the end
    main_stays_alive = True

    # Set up first directory of the story
    Uri_story_start = "../Yuki_Sleeps_Adventure/"  # the first directory of the story
    Uri_story_current = ""  # the subdirectory inside the story
    current_count_int = 1  # the current page or the node

    image = Image.open("blank.png")
    tk_image = None  #ImageTk.PhotoImage(image)


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


# kill every object and mainline
def end_game(event):
    myGlobal.main_stays_alive = False
    print("exiting....")

def Show_Story_Page(node, page_number):
  print("Hello from a Show_Story_Page")
  print("page=>" + node + " . " + str(page_number) )

  # Show text, image, and play voice
  Show_text(node, page_number)
  Show_image(node, page_number)
  Play_Voice(node, page_number)



def Show_text(node, page_number):
      x = node + "text_" + "{:02d}".format(page_number) + ".txt"
      print(x)

      # get the story text
      try:
        f = open(x)
        story_text = f.read()
        f.close()
      except Exception as e:
          print(f"An unexpected error occurred: {e}")
          story_text = "...and that is the end of the story! Goodbye."
          print("@@@@@@@@@" + story_text)
          text_story.delete("1.0", tk.END)
          text_story.insert(tk.END, story_text)
          text_story.pack()
          root.update()
          time.sleep(5)
          exit()

      print("@@@@@@@@@" + story_text)
      text_story.delete("1.0", tk.END)
      text_story.insert(tk.END, story_text)
      text_story.pack()


def Show_image(node, page_number):
    x = node + "pic_" + "{:02d}".format(page_number) + ".png"
    print(x)
    image = Image.open(x)
    myGlobal.tk_image = ImageTk.PhotoImage(image)
    # canvas.configure(None)
    canvas.create_image(1,1,anchor=NW, image=myGlobal.tk_image)
    # canvas.configure(image=tk_image)
    canvas.pack()
    canvas.update()
    root.update()


def Play_Voice(node, page_number):
    x = node + "voice_" + "{:02d}".format(page_number) + ".wav"
    print(x)
    winsound.PlaySound(x, winsound.SND_FILENAME)


# create (and pack) the main window
root = tk.Tk()
root.geometry("1200x660")  # Set window size
root.title("Welcome to My App")  # Set window title

text_instructions = tk.Text(root, height=1, width=100,font=("Helvetica", 18))
text_instructions.place(relwidth=0, relheight=0)
text_instructions.pack()
text_instructions.insert(tk.END, "Press key 1, 2 or 3 to select a path.")

canvas= tk.Canvas(root, width= 1000, height= 500)
image = Image.open("blank.png")
myGlobal.tk_image = ImageTk.PhotoImage(image)
canvas.create_image(1, 1, anchor=NW, image=myGlobal.tk_image)
# canvas.place(x = 100, y = 50)
# canvas.focus_set()
canvas.pack()

# myGlobal.tk_image = ImageTk.PhotoImage(image)


text_story = tk.Text(root, height=5, width=100, font=("Helvetica", 18))
# text_story.place(relwidth=1, relheight=1)
text_story.pack()


root.update()


# Bind arrow keys to functions
root.bind('<space>', spacebar_pressed)
root.bind('1', one_pressed)
root.bind('2', two_pressed)
root.bind('3', three_pressed)


# now loop forever...
# the story starts in a node, from there drops into a subdirectory named 1,2,or 3
# The story has 3 pages on each node (for now). Page 01, 02, 03.
# The user sees the first node, presses "space" to see each page
# and then presses either 1,2,or 3 to select the story to continue in
# one of the subdirectories

# show first page


current_directory = Path.cwd()
print("Current Dir => " + str(current_directory))


Show_Story_Page(myGlobal.Uri_story_start, 1)


root.mainloop()



















