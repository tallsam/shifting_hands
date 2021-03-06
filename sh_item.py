# Shifting Hands
# Item Classes
# Sam Hassell

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
  
  
if __name__ == "__main__":
    print "You ran this module directly (and did not 'import' it)."
    raw_input("\n\nPress the enter key to exit.")
