# SPLASH SCREEN EXAMPLE
# Written by Samoe
# samoe.me/code
# v1.1

from tkinter import *
from PIL import Image, ImageTk

#########################################################
# IF USING A LOCALLY STORED IMAGE, USE THIS BLOCK OF CODE

# import os
# assetPath = os.path.dirname(__file__) + '/assets/' # POINTS TO /SCRIPT LOCATION/assets

#########################################################
#########################################################
# IF LOADING AN IMAGE FROM A WEB URL, USE THIS BLOCK OF CODE

import urllib.request
import io
splashUrl = 'https://samoe.me/img/img_splash.png'

#########################################################

global screen_width
global screen_height

def center(window, size, yoffset = 0):

    x = (screen_width / 2) - size[0] / 2
    y = (screen_height / 2) - size[1] / 2 - yoffset

    # GEOMETRY FORMAT HAS TO BE "+X+Y"
    window.geometry('+' + str(int(x)) + '+' + str(int(y)))

    # FASTER WAY OF WRITING IT, X AND Y ARE INSERTED AT %d
    # window.geometry("+%d+%d" % (x, y))

def initMainWindow():

    splash.destroy()
    root = Tk()
    root.title("SPLASH SCREEN EXAMPLE - MAIN WINDOW")

    # AUTOMATICALLY SET WINDOW SIZE AND POSITION BASED ON SCREEN RESOLUTION
    rootSize = (int(screen_width / 1.25), int(screen_height / 1.25))
    root.geometry(str(rootSize[0]) + 'x' + str(rootSize[1]))

    center(root, rootSize, yoffset = int(screen_height / 32))

######################################################################

# FIRST THING THAT EXECUTES:
if __name__ == '__main__' :

    # INIT SPLASH SCREEN
    splash = Tk()

    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()

    splashSize = (int(screen_width / 4), int(screen_width / 8)) # DEFINE SPLASH SIZE BASED ON SCREEN RESOLUTION
    splash.geometry(str(splashSize[0]) + 'x' + str(splashSize[1])) # SET SPLASH SIZE
    splash.overrideredirect(True) # REMOVE WINDOW BORDER

    # DISPLAY SPLASH IMAGE - CAN BE REPLACED BY TEXT OR WHATEVER ELSE YOU WANT

    # LOCAL IMAGE
    # splashImg = Image.open(assetPath + 'img_splash.png').resize(splashSize)
    # splashImgRef = ImageTk.PhotoImage(splashImg)

    # WEB IMAGE
    splashImgData = urllib.request.urlopen(splashUrl).read()
    splashImg = Image.open(io.BytesIO(splashImgData)).resize(splashSize)
    splashImgRef = ImageTk.PhotoImage(splashImg)

    splashImage = Label(splash, image = splashImgRef)
    splashImage.pack(fill = 'both', expand = 'yes', anchor = 'c')

    center(splash, splashSize) # CENTER SPLASH

    ##### PUT THE CODE YOU NEED TO RUN DURING THE SPLASH SCREEN HERE #####
    # ex: INITIALIZE DATABASE
    # ex: ORGANIZE DATA FILES
    # ex: LOAD LARGE IMAGE FILES
    ######################################################################

    splash.after(3000, initMainWindow)
    
    mainloop()