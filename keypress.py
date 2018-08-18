from __future__ import print_function

# Libraries we need
import pyxhook
import time


# This function is called every time a key is presssed
def kbevent(event):
    global running
    # print key info
    print(event)

    # If the ascii value matches spacebar, terminate the while loop
    if event.Ascii == 32:
        running = False


# Create hookmanager
hookman = pyxhook.HookManager()
# Define our callback to fire when a key is pressed down
hookman.KeyDown = kbevent
# Hook the keyboard
hookman.HookKeyboard()
# Start our listener
hookman.start()

# Create a loop to keep the application running
running = True
while running:
    time.sleep(0.1)

# Close the listener when we are done
hookman.cancel()








# from Tkinter import *
# import sys
# import Tkinter

# class App(Tkinter.Tk):

#     def __init__(self):
#         Tkinter.Tk.__init__(self)
#         menubar = Tkinter.Menu(self)
#         fileMenu = Tkinter.Menu(menubar, tearoff=False)
#         menubar.add_cascade(label="File", underline=0, menu=fileMenu)
#         fileMenu.add_command(label="doThat", underline=1,
#                              command=quit, accelerator="Ctrl+v")
#         fileMenu.add_command(label="doThis", underline=1,
#                              command=quit, accelerator="Tab")
#         self.config(menu=menubar)

#         self.bind_all("<Control-v>", self.doThat)
#         self.bind_all("<Tab>", self.doThis)

#     def doThat(self, event):
#         print("Control v is pressed ...")

#     def doThis(self, event):
#         print("Tab is pressed...")

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()
