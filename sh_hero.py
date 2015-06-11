# Shifting Hands
# Hero Class
# Sam Hassell

import sh_entity # A base character class for mobs, npcs & the hero.

class Hero(sh_entity.Entity):

  def __init__(self, gamemap, loc):
    self.loc = loc #current location as a tuple.
    self.loc_str = str(loc[0]) + "," + str(loc[1]) #current location as a string
    self.map = gamemap
    self.inv = Inventory() 
    self.room = self.map.mapdata[self.loc_str]; #the current room object
    self.hp = 100 #health points
    self.room.enter()



  def __str__(self):
    rep = "You are located at " + \
    str(self.loc[0]) + \
    "," + \
    str(self.loc[1]) + \
    "\n" + \
     "You have " + str(self.hp) + " health"
    return rep



  def parse(self, input):
    'parses the user input and triggers the appropriate function.'
    print
    
    # Sanitise input.
    # Delete small words.
    # Remove multiple spaces.
    
    # Move.
    if input in ("N", "E", "S", "W"):
      return self.move(input)
      
    # Location.
    elif input in ("LOC"):
      return str(self)
    
    # Inventory.
    elif input in ("I", "INV"):
      return str(self.inv)
    
    # Kill
    elif input.split( )[0] in ("K", "KILL", "ATTACK", "A") :
      if len(input.split( )) > 1: 
        return self.attack(input.split( )[1])
      else:
        return "What do you want to attack?"
    
    # Help.
    elif input.split( )[0] in ("HELP"):
      return "n, e, s, w, loc, i, pu"
    
    # Pickup an Item. 
    elif input.split( )[0] in ("PU", "PICKUP"):
      return self.pickup(input.lower().split( )[1])
      
    # Display Map
    elif input.split( )[0] in ("MAP"):
      return self.map.display(self.loc)
      
    # Drop an Item
    elif input.split( )[0] in ("DROP", "D"):
      if len(input.split( )) > 1:
        return self.drop(input.lower().split( )[1])
      else:
        return 'What do you want to drop?';
    
    # Look at an item or just look. 
    elif input.split( )[0] in ("EXAMINE", "LOOK", "L" ):
      if input.split( )[1] in (""):
        return self;
      else:
        #need to pass an object here, not the string.
        return self.examine(input.lower().split( )[1])
        
    # Quit.
    elif input in ('QUIT','Q'):
      return 'Goodbye!'
      
    # PEBKAC      
    else:
      return "I dont understand."



  def look(self):
    return str(self.map.get_room(self.loc_str))
    
  def move(self, dir):
    if not self.map.move_ok(self.loc_str, dir):
      return "You cannot move that direction."
    if dir == "N":
      self.loc = (self.loc[0] , self.loc[1] + 1) # inc y by 1
      self.loc_str = str(self.loc[0]) + "," + str(self.loc[1])
      output = "You moved North"
    elif dir == "E":
      self.loc = (self.loc[0] + 1, self.loc[1]) # inc x by 1
      self.loc_str = str(self.loc[0]) + "," + str(self.loc[1])
      output = "You moved East"
    elif dir == "S":
      self.loc = (self.loc[0], self.loc[1] -1) # decr y by 1
      self.loc_str = str(self.loc[0]) + "," + str(self.loc[1])                
      output = "You moved South"
    elif dir == "W":
      self.loc = (self.loc[0] - 1, self.loc[1]) #decr x by 1
      self.loc_str = str(self.loc[0]) + "," + str(self.loc[1])                
      output = "You moved West"      
    self.room = self.map.mapdata[self.loc_str];
    self.room.enter()
    return output    

  def pickup(self, item):
    'checks if the item is in the room then makes the hero pick it up.'
    room_item = self.room.get_item(item)    
    if room_item:
      self.room.remove_item(room_item)
      self.inv.add_item(room_item)
      return "You picked up the " + item + "." 
    else:
      return "That item is not here." 

  def drop(self, item):
    'If the hero has the current item, drop it in the room'
    inv_item = self.inv.get_item(item)
    if inv_item:
      self.inv.drop_item(inv_item)
      self.room.add_item(inv_item)
      return "You dropped the " + item + "." 
    else:
      return "You do not have that item." 


  def examine(self, item):
    'checks if the item is in the room then displays its information.'
    room_item = self.room.get_item(item)    
    if room_item:
      return room_item
    else:
      return "That item is not here."
   

  def attack(self, mob):
    return "You attack."  
    
      
    


class Inventory():

  def __init__(self):
    self.size   = 20; #items
    self.weight = 20000; #grams
    self.inv = []
      
  def __str__(self):
    rep = "** Inventory **\n"
    if self.inv:
      for item in self.inv:
        rep += "  " + str(item.name.capitalize()) + "\n"
    else:
      rep += "  Your inventory is empty!"
    return rep
    
  def add_item(self, item):
      self.inv.append(item)
      
  def drop_item(self, item):
      self.inv.remove(item)
    
  def get_item(self, item_name):
    'checks if the item is in the inventory'
    for inv_item in self.inv:
      if inv_item.name == item_name:
        return inv_item
    return False
 
 
      
if __name__ == "__main__":
  print "You ran this module directly (and did not 'import' it)."
  raw_input("\n\nPress the enter key to exit.")

