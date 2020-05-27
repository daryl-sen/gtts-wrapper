from gtts import gTTS
from tkinter import *


constants = {
    'width': 200,
    }
# create window object
window = Tk()

# functions
def convert():
    target_text = text_entry.get('1.0', END)
    file = filename.get()
    tts = gTTS(target_text)
    tts.save(f'output/{file}.mp3')
    notif = Label(window, text = f"A new MP3 file ({file}.mp3) has been created. Please check the output folder.")
    notif.pack()

# widgets
welcome = Label(window, text = "gTTS - Text to MP3", font = "Helvetica 22 bold", pady = 50)
disclaimer = Label(window, text = "DISCLAIMER: This program is a GUI wrapper for gTTS made using the Python tkinter module, and compiled into an executable using the py2exe module. The author of this wrapper does not claim any credit for the functionality of these individual python modules.", padx = 50, width = constants['width'])
instructions_header = Label(window, text = "Instructions", font = "Helvetica 18 bold", pady = 10)
instructions = Label(window, text = "Enter text into the box below, then click on 'Create MP3'. Text inside the box will be converted into an MP3 file in the same directory as this program.", width = constants['width'])
text_entry = Text(window, width = constants['width'], height = 10)
filename_label = Label(window, text = "Please enter a name for your file (without any extensions)", width = constants['width'])
filename = Entry(window, width = constants['width'])

button = Button(window, text = "Create MP3", padx = 10, pady = 10, command = convert)

# pack into window
welcome.pack()
disclaimer.pack()
instructions_header.pack()
instructions.pack()
text_entry.pack()
filename_label.pack()
filename.pack()
button.pack()

# run the gui
window.mainloop()
