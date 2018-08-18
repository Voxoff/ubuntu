#!/usr/bin/python
# -*- coding: utf-8 -*-
from gi.repository import Gtk, GObject
from datetime import datetime
from time import strftime

class MainWindow(Gtk.Window):
  def __init__(self):
    Gtk.Window.__init__(self, title="app")

    self.box = Gtk.Box(spacing=6)
    self.add(self.box)

    self.label = Gtk.Label()
    self.box.pack_start(self.label, True, True, 0)
    global starttime
    starttime = datetime.now()
    # Ini a time here and store it globally

  # Displays Timer
  def displayclock(self):
    #  we need to return "True" to ensure the timer continues to run, otherwise it will only run once.
    calctime = datetime.now() - starttime
    self.label.set_label(str(calctime.seconds) + " Seconds")
    # calc new time minus start time.
    return True

  # Initialize Timer
  def startclocktimer(self):
    #  checks for keypress and mouse
    GObject.timeout_add(1000, self.displayclock)

win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
win.startclocktimer()
Gtk.main()
