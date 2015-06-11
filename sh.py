#!/usr/bin/python
#+'"


import shelve # for persistant storage

import sh_map # The class controlling maps and rooms.
import sh_item # The class controlling items.
import sh_entity # A base character class for mobs, npcs & the hero.
import sh_hero # The class controlling the hero (the player)
import sh_utils # Some helper functions


#The location to load the data from.
datafile = "data/mymap.dat"

start_loc = (0,0)
gamemap   = sh_map.Map(datafile)
hero      = sh_hero.Hero(gamemap, start_loc)

output =  "Welcome!"

while input not in ('QUIT','Q'):
  sh_utils.clearscreen()
  print "========================================================="
  print hero.map.display(hero.loc)
  print "========================================================="
  print hero.look()
  print "========================================================="
  print "\n>> " + output
  input = str(raw_input(": ")).upper()
  output = hero.parse(input)
  

