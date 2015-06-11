#!/usr/bin/python
#+'"

import shelve

class Item(object):

  def __init__(self, name, description, material, item_type, weight, base_value, actions):
    self.name        = name
    self.description = description
    self.material    = material  #wood, gold, silver, food, steel
    self.item_type   = item_type #weapon, armour, healing, food
    self.weight      = weight
    self.base_value  = base_value
    self.actions     = actions

  def __str__(self):
    rep  = "**You look at the " + self.name + "..\n"
    rep += self.description + "\n"
    rep += "It is made of " + self.material
    rep += " and weighs about " + self.weight + " grams.\n"
    return rep

  def save(self, datafile):
    item_data = {"material"   : self.material,
      "description": self.description,
      "item_type"  : self.item_type,
      "weight"     : self.weight,
      "base_value" : self.base_value,
      "actions"    : self.actions
    }

  key = str(self.loc[0]) + "," + str(self.loc[1])

  gamedata = shelve.open(datafile, "c")        
  gamedata[self.name] = item_data
  gamedata.sync()
  gamedata.close()


class Room():
  def __init__(self, loc, title, description, exits, items, npcs, mobs):
    self.loc         = loc
    self.title       = title
    self.description = description
    self.exits       = exits
    self.items       = items
    self.npcs        = npcs
    self.mobs        = mobs

  def __str__(self):
    rep  = "** " + self.title + " **\n"
    rep += self.description
    rep += "\n Exits: "
    for x in self.exits:
      rep += x
      rep += "\n Items: "
      item_list = ""
    if self.items:
      for x in self.items:
        item_list += x.name + ","
        rep += item_list[:-1]
    else:
      rep += "None" 
      rep += "\n NPCs: "
      npc_list = ""
    if self.npcs:            
      for x in self.npcs:
        npc_list += x + ","
        rep += npc_list[:-1]
    else:
      rep += "None"
      rep += "\n Mobs: "
      mob_list = ""
    if self.mobs:
      for x in self.mobs:
      mob_list += x + ","
      rep += mob_list[:-1]
    else:
      rep += "None"
    return "\n" + rep 

  def save(self, datafile):
    room = {"loc" : self.loc,
    "title" : self.title,
    "description" : self.description,
    "exits" : self.exits,
    "items" : self.items,
    "npcs"  : self.npcs,
    "mobs"  : self.mobs}
    key = str(self.loc[0]) + "," + str(self.loc[1])
    gamedata = shelve.open(datafile, "c")        
    gamedata[key] = room
    gamedata.sync()
    gamedata.close()

  def remove_item(self, item):
    if item in self.items:
    self.items.remove(item)

  def get_items(self):
    return self.items


class Map():

def __init__(self, datafile):
self.mapdata = {}
data = shelve.open(datafile, "r")
for key in data.keys():
loc = data[key]["loc"]
title = data[key]["title"]
description = data[key]["description"]
exits = data[key]["exits"]
items = data[key]["items"]
npcs = data[key]["npcs"]
mobs = data[key]["mobs"]
self.mapdata[key] = Room(loc, title, description,
                  exits, items, npcs, mobs)

def __str__(self):
rep = "Rooms\n\n"
for key in self.mapdata.keys():
print self.mapdata[key]

rep += "\n\n"
return rep

def move_ok(self, loc, dir):
if dir in self.mapdata[loc].exits:
return True
else:
return False

def get_room(self, loc):
return self.mapdata[loc]


class Hero():

def __init__(self, gamemap, loc):
self.loc = loc
self.loc_str = str(loc[0]) + "," + str(loc[1])
self.map = gamemap
self.inv = []

def __str__(self):
rep = "You are located at " + \
str(self.loc[0]) + \
"," + \
str(self.loc[1]) + \
"\n\n"
return rep

def parse_action(self, input):
'parses the user input and triggers the appropriate function.'
print
if input.upper() in (N, E, S, W):
hero.move(input)
elif input.upper() in ("LOC"):
print hero
elif input.upper() in ("I", "INV"):
print hero.show_inv()

elif input.upper() in ("HELP"):
print "n, e, s, w, loc, i, pu"

elif input.upper().split( )[0] in ("PU", "PICKUP"):
hero.pickup(input.lower().split( )[1])

elif input.upper().split( )[0] in ("EXAMINE"):
hero.examine(input.lower().split( )[1])

else:
print "I dont understand."




def look(self):
print self.map.get_room(self.loc_str)

def show_inv(self):
rep = "** Inventory **\n"
if self.inv:
for item in self.inv:
rep += item.capitalize() + "\n"
else:
rep += "Your inventory is empty!"
return rep

def pickup(self, item):
for room_item in self.map.mapdata[self.loc_str].items:
if room_item == item:
self.map.mapdata[self.loc_str].remove_item(item)
self.inv.append(item)
print "You picked up the " + item + "."

print "That item is not here."


def examine(self, item):
not_here = 1
for room_item in self.map.mapdata[self.loc_str].items:
if room_item.name == item:
print room_item
not_here = 0
break
if not_here == 1:
print "That item is not here."

#if item in self.map.mapdata[self.loc_str].items:
#     print item
#else:
#     print "That item is not here."

def move(self, dir):
if self.map.move_ok(self.loc_str, dir):
if dir == "N":
self.loc = (self.loc[0] -1, self.loc[1])
self.loc_str = str(self.loc[0]) + "," + str(self.loc[1])
print "You moved North"

elif dir == "E":
self.loc = (self.loc[0], self.loc[1] + 1)
self.loc_str = str(self.loc[0]) + "," + str(self.loc[1])
print "You moved East"

elif dir == "S":
self.loc = (self.loc[0] + 1, self.loc[1])
self.loc_str = str(self.loc[0]) + "," + str(self.loc[1])                
print "You moved South"

elif dir == "W":
self.loc = (self.loc[0], self.loc[1] - 1)
self.loc_str = str(self.loc[0]) + "," + str(self.loc[1])                
print "You moved West"
else:
print "You cannot move that direction."








#direction constants
N, E, S, W = "N", "E", "S", "W"

datafile = "data/mymap.dat"

gold  = Item("gold",
"This is a gold coin. It has a picture of a mountain\n" + \
"on one side and a dragon on the other.",
"gold",
"money",
"200",
"1",
["spend", "count"]
)

short_sword = Item("sword",
"This short sword has a diamond embeded in the hilt\n" +\
    "and looks very, very sharp",
"silver",
"weapon",
"5000",
"300",
["swing", "wield", "sheath", "throw"]
)


rooma = Room((0, 0),
"Room A",
"A dark room",
(N, S),
[gold],
["Charles"],
())

roomb = Room((1, 0),
"Room B",
"A blue room",
(N),
[gold, short_sword],
(),
["Beggar"])

roomc = Room((-1, 0),
"Room C",
"A dingy room",
(S),
[gold],
["Storeman Al", "Pete"],
())


rooma.save(datafile)
roomb.save(datafile)
roomc.save(datafile)


start_loc = (0,0)
gamemap = Map(datafile)
hero = Hero(gamemap, start_loc)

while input != "quit":

hero.look()
input = str(raw_input(": ")).upper()

hero.parse_action(input)


