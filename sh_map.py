# Shifting Hands
# Map and Room Classes
# Sam Hassell


import shelve  # for loading the map data.
import sh_map  # The class controlling maps and rooms.
import sh_item # The class controlling items.

class Room():
  def __init__(self, loc, title, description, exits, items, npcs, mobs):

    self.loc         = loc
    self.title       = title
    self.description = description
    self.exits       = exits
    self.items       = items
    self.npcs        = npcs
    self.mobs        = mobs
    
    self.visited     = 0

  def __str__(self):
  
    # Room title.
    rep  = " ** " + self.title + " **\n"
    rep += self.description
    
    # Exits
    rep += "\n Exits: "
    for x in self.exits:
      rep += x
    
    # Items
    rep += "\n Items: "
    item_list = ""
    if self.items:
      for x in self.items:
        item_list += x.name.capitalize() + ", "
      rep += item_list[:-2]
    else:
      rep += "None" 
    
    # NPCs
    rep += "\n NPCs:  "
    npc_list = ""
    if self.npcs:            
      for x in self.npcs:
        npc_list += x.title() + ", "
      rep += npc_list[:-2]
    else:
      rep += "None"
      
    # Mobs
    
    rep += "\n Mobs:  "
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


  def enter(self):
    self.visited = 1;

  def add_item(self, item):
    'add an item to the room'
    self.items.append(item)    


  def remove_item(self, item):
    'removes an item from the room if it exists'
    if item in self.items:
      self.items.remove(item)    


  def get_items(self):
    'returns a list of the rooms item objects.'
    return self.items

  
  def get_item(self, item_name):
    'checks if the item is in the room'
    for room_item in self.items:
      if room_item.name == item_name:
        return room_item
    return False



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
      self.mapdata[key] = sh_map.Room(loc, title, description,
                                      exits, items, npcs, mobs)
    data.close

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
    
    
  def display(self, cur_loc):
    'Displays ASCII map of places that have been seen.'
    
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    x = 0
    y = 0
    
    loc = str(cur_loc[0]) + ',' + str(cur_loc[1])
    for key in self.mapdata.keys():
      room = self.mapdata[key]
      if room.visited == 1:
        if room.loc[0] < min_x:
          min_x = room.loc[0]
        if room.loc[0] > max_x:
          max_x = room.loc[0]
        if room.loc[1] > max_y:
          max_y = room.loc[1]
        if room.loc[1] < min_y:
          min_y = room.loc[1]
    
    mapstr = ""
    for y in range(max_y, min_y-1, -1):   
      buff_a = " "
      buff_b = " "
      buff_c = " "
      for x in range(min_x, max_x+1, +1):        
        key = str(x) + "," + str(y) 
        
        if not self.mapdata.has_key(key):
          buff_a += "     "
          buff_b += "     "
          buff_c += "     "
        else:
          # calc exits
          if "N" in self.mapdata[key].exits:
            north = "  |  "
          else:
            north = "     "
          if "S" in self.mapdata[key].exits:
            south = "  |  "
          else:
            south = "     "
          if "E" in self.mapdata[key].exits:
            east = "-"
          else:
            east = " "
          if "W" in self.mapdata[key].exits:
            west = "-"
          else:
            west = " "
          # draw ascii    
          if loc == key: 
            buff_a += north
            buff_b += west+"[*]"+east
            buff_c += south             
          else:                    
            buff_a += north
            buff_b += west+"[ ]"+east
            buff_c += south               
 
      mapstr += buff_a + "\n" +buff_b+ "\n" +buff_c+ "\n"
      
    return mapstr 

'''
    mapstr = ""
    for y in range(max_y, min_y-1, -1):   
      for x in range(min_x, max_x+1, +1):        
        key = str(x) + "," + str(y) 
        if not self.mapdata.has_key(key):
          mapstr += "   "
        elif loc == key:      
          mapstr += "[*]"          
        else:                    
          mapstr += "[ ]"
      mapstr += "\n"    
  '''  
    



    
if __name__ == "__main__":
  print "You ran this module directly (and did not 'import' it)."
  raw_input("\n\nPress the enter key to exit.")

 
    
  


    



