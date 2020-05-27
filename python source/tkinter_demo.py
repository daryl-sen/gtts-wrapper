from tkinter import *

# create window object
window = Tk()

welcome = Label(window, text = "gTTS - Text to MP3", font = "Helvetica 22 bold", pady = 50)
disclaimer = Label(window, text = "DISCLAIMER: This program is a GUI wrapper for gTTS made using the Python tkinter module, and compiled into an executable using the py2exe module. The author of this wrapper does not claim any credit for the functionality of these individual python modules.", padx = 50)
instructions_header = Label(window, text = "Instructions", font = "Helvetica 18 bold", pady = 10)
instructions = Label(window, text = "Enter text into the box below, then click on 'Create MP3'. Text inside the box will be converted into an MP3 file in the same directory as this program.")
text_entry = Text(window, width = 200, height = 10)

button = Button(window, text = "Create MP3", padx = 10, pady = 10)


welcome.pack()
disclaimer.pack()
instructions_header.pack()
instructions.pack()
text_entry.pack()
button.pack()

# run the gui
window.mainloop()
