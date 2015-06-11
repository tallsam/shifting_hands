# Shifting Hands
# Entity Class
# Sam Hassell



class Entity():
  
  def __init__(self, gamemap, loc):
    self.loc = loc #current location as a tuple.
    self.loc_str = str(loc[0]) + "," + str(loc[1]) #current location as a string
    self.map = gamemap
    self.inv = Inventory() 
    self.room = self.map.mapdata[self.loc_str]; #the current room object
    self.hp = 100 #health points
    self.room.enter()
    self.desc = "Simple Entity"
    
  def __str__(self):
    rep = self.desc
    return rep
    
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

