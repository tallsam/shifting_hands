#!/usr/bin/python
#+'"

import shelve # for loading the map data.
import sh_map # The class controlling maps and rooms.
import sh_item # The class controlling items.


datafile = "data/mymap.dat"

gold  = sh_item.Item("gold",
"This is a gold coin. It has a picture of a mountain\n" + \
  "on one side and a dragon on the other.",
"gold",
"money",
"200",
"1",
["spend", "count"]
)

short_sword = sh_item.Item("sword",
"This short sword has a large diamond embeded in the hilt\n" +\
    "and looks very, very sharp.",
"silver",
"weapon",
"5000",
"300",
["swing", "wield", "sheath", "throw"]
)

kitchen_knife = sh_item.Item("knife",
"A simple kitchen knife. It is quite sharp.",
"stainless steel",
"weapon",
"200",
"12",
["cut"]
)

tomato = sh_item.Item("tomato",
"A shiny red tomato.",
"vegetable",
"food",
"100",
"1",
["cut", "throw", "squash"]
)

hall = sh_map.Room(
  (0, 0),
  "The Hallway",
  "A skinny hallway connecting the house together.",
  ("N", "S", "W"),
  [gold],
  ["Charles"],
  [])
hall.save(datafile)

kitchen = sh_map.Room(
  (-1,0),
  "The Kitchen",
  "You can make food in here. There is a stove and a fridge.",
  ("E"),
  [kitchen_knife, tomato],
  [],
  [])
kitchen.save(datafile)

front = sh_map.Room(
  (0,-1),
  "The Front Room",
  "A blue room with some nice windows",
  ("N"),
  [gold, short_sword],
  [],
  ["Beggar"])
front.save(datafile)

back = sh_map.Room(
  (0, 1),
  "The Backroom",
  "A dingy room",
  ("S"),
  [gold],
  ["Storeman Al", "Pete"],
  [])
back.save(datafile)





