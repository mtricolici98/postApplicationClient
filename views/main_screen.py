from functools import partial
from tkinter import Tk, Label, StringVar, Button

from postClient.PostApplicationClient import PostApplicationClient


def show_main_screen(postAppClient: PostApplicationClient):
    tkWindow = Tk()
    tkWindow.geometry('400x150')
    tkWindow.title('Main Screen')

    tkWindow.mainloop()
