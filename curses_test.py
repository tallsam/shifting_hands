#!/usr/bin/python
#+'"

# Shifting Hands
# A Test Implementation of an ncurses interface.
# Sam Hassell

import curses
import curses.wrapper



class Curses_test():

  def __call__(self, stdscr):
   
    #create the map window
    begin_x = 0
    begin_y = 0
    height = 10
    width = 10
    mywin = stdscr.subwin(height, width, begin_y, begin_x)
    mywin.addstr(0,0,"HELLO\ndfsdd",curses.A_REVERSE) 
    mywin.refresh()
    curses.echo()
  
    # main loop
    while 1:

      c = stdscr.getstr(20,0)
      if c == 'q': break
      stdscr.addstr(11,0,c,curses.A_REVERSE)
      stdscr.addstr(20,0,'                                         ')
      stdscr.refresh()

# The wrapper function handles setting up and tearing down the ncurses environment.
mytest = Curses_test()
curses.wrapper(mytest)
