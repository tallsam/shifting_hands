#!/usr/bin/python
#+'"


import shelve # for persistant storage.
import curses # for the ncurses cli-based interface.
import curses.wrapper # simplifies setting up and tearing down ncurses.

import sh_map # The class controlling maps and rooms.
import sh_item # The class controlling items.
import sh_hero # The class controlling the hero (the player)
import sh_utils # Some helper functions


class Curses_sw():

  def __init__(self):
    # The location to load the data from.
    self.datafile = "data/mymap.dat"

    # 0,0 is the center of the map. 
    # I should move this to saved data so it can be customised.
    self.start_loc = (0,0) 
    
    # The map object.
    self.gamemap   = sh_map.Map(self.datafile)
    
    # The hero,holding the map, standing at 0,0.
    self.hero      = sh_hero.Hero(self.gamemap, self.start_loc) 
    
    self.output    = "Welcome!"
    

  def __call__(self, stdscr):

    # Create the ncurses map window.
    map_win_begin_x = 0
    map_win_begin_y = 0
    map_win_height  = 12
    map_win_width   = 40
    map_win   = stdscr.subwin(map_win_height, 
                              map_win_width, 
                              map_win_begin_y, 
                              map_win_begin_x)
    
    # Create the inventory window
    inv_win_begin_x = 40
    inv_win_begin_y = 0
    inv_win_height  = 12
    inv_win_width   = 30
    inv_win   = stdscr.subwin(inv_win_height, 
                              inv_win_width, 
                              inv_win_begin_y, 
                              inv_win_begin_x)

    # Create the ncurses description window.
    desc_win_begin_x = 0
    desc_win_begin_y = 12
    desc_win_height  = 10
    desc_win_width   = 70
    desc_win   = stdscr.subwin(desc_win_height, 
                               desc_win_width, 
                               desc_win_begin_y, 
                               desc_win_begin_x)    

    # Create the message window.
    msg_win_begin_x = 0
    msg_win_begin_y = 22
    msg_win_height  = 5
    msg_win_width   = 70
    msg_win   = stdscr.subwin(msg_win_height, 
                               msg_win_width, 
                               msg_win_begin_y, 
                               msg_win_begin_x)    
    
    # Create the input window
    input_win_begin_x = 0
    input_win_begin_y = 27
    input_win_height  = 3
    input_win_width   = 70
    input_win   = stdscr.subwin(input_win_height, 
                                input_win_width, 
                                input_win_begin_y, 
                                input_win_begin_x)    
 
    # Draw everything onto the screen
    self.draw_screen(map_win, desc_win, msg_win, input_win, inv_win)
    stdscr.refresh()
    
    curses.echo()

    # Main input loop
    while 1:
    
      # Get the users input
      input = input_win.getstr(1,4).upper()

      # Check for quit.
      if input == 'Q': break
      
      # Update the hero.
      self.output = self.hero.parse(input)
      
      # Update all the windows.
      stdscr.clear()
      self.draw_screen(map_win, desc_win, msg_win, input_win, inv_win)

           
      # Refresh the whole screen.
      stdscr.refresh()
      
  def draw_screen(self, map_win, desc_win, msg_win, input_win, inv_win):

      map_win.addstr(1, 1, '** Map **\n' + self.hero.map.display(self.hero.loc))
      map_win.border()
      desc_win.addstr(0, 0, self.hero.look())
      desc_win.border()
      msg_win.addstr(1, 1, self.output)
      msg_win.border()
      input_win.addstr(1, 1, '>>')
      input_win.border()
      inv_win.addstr(1, 1, str(self.hero.inv)) 
      inv_win.border()
    

cursessw = Curses_sw()
curses.wrapper(cursessw)

