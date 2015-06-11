

def clearscreen(numlines=100):
  """Clear the console.

  numlines is an optional argument used only as a fall-back.
  """
  import os
  if os.name == "posix":
    # Unix/Linux/MacOS/BSD/etc
    os.system('clear')
  elif os.name in ("nt", "dos", "ce"):
    # DOS/Windows
    os.system('CLS')
  else:
    # Fallback for other operating systems.
    print '\n' * numlines
