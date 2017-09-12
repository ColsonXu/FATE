'''StateTester.py
This tests to make sure that a class has been implemented
called Game_State and that it satisfies certain requirements.

'''


problem_name = 'FATE'

import sys, importlib.util

# Get the PROBLEM name from the command-line arguments

if len(sys.argv)<2:
  """ The following few lines go with the LINUX version of the text client.
  print('''
       Usage:
./IDLE_Text_SOLUZION_Client <PROBLEM NAME>
       For example:
./IDLE_Text_SOLUZION_Client Missionaries
  ''')
  exit(1)
  """
  sys.argv = ['Tk_SOLUZION_Client.py', problem_name] # IDLE and Tk version only.
  # Sets up sys.argv as if it were coming in on a Linux command line.

problem_name = sys.argv[1]
print("problem_name = "+problem_name)

try:
  spec = importlib.util.spec_from_file_location(problem_name, "../"+problem_name+".py")
  PROBLEM = spec.loader.load_module()
  spec.loader.exec_module(PROBLEM)
except Exception as e:
  print(e)
  exit(1)


def print_metadata():
  print("\nMetatdata follows:\n")
  print("PROBLEM_NAME: "+PROBLEM.PROBLEM_NAME)
  print("PROBLEM_VERSION: "+PROBLEM.PROBLEM_VERSION)
  print("PROBLEM_AUTHORS: ", end=' ')
  for i in range(len(PROBLEM.PROBLEM_AUTHORS)):
      if i==len(PROBLEM.PROBLEM_AUTHORS)-1:
        c = '\n'
      else:
        c = ', '
      print(PROBLEM.PROBLEM_AUTHORS[i], end=c)

  print("PROBLEM_CREATION_DATE: "+PROBLEM.PROBLEM_CREATION_DATE)
  print("PROBLEM_DESC: "+PROBLEM.PROBLEM_DESC)

try:
  print_metadata()
except Exception as e:
  print("There was a problem getting one or more of the metadata items from the formulation.")
  print(e)

def test_state():
  try:
    gs = PROBLEM.Game_state
  except Exception as e:
    print("class Game_state could not be found in the problem formulation.")
    print(e)
    exit(1)

  try:
    s = gs()
  except Exception as e:
    print('''Your Game_State __init__ method needs to provide default values
      of arguments to support automatic unit testing, but apparently it does not.''')
    print(e)

  try:
    s2 = s.__copy__()

    if id(s2)==id(s):
       print("Your __copy__ method does not seem to be returning a new object. That is an error.")
       exit(1)
    else: print("Found a Game_State  __copy__ method.")

  except Exception as e:
    print("Did you implement the __copy__ method for your Game_State class?  It seems to either be missing or to throw an exception.")
    print(e)
    exit(1)
  try:
    if s2 != s:
       print("Perhaps you did not implement the __eq__ method or it is not working correctly. Your copy and the original state should be equal according to __eq__.")
       exit(1)
  except Exception as e:
    print(e)
    print("Exiting since your equality test threw an exception.")

  try:
    n = s.__hash__()
  except Exception as e:
    print("Perhaps you did not implement __hash__ for your Game_State class.  It doesn't work.")
  if type(n)==type(0):
    print("Hash function exists and returns an int.")
  else:
    print("Invalid type returned by __hash__: "+str(type(n)))
    exit(1)
  print("Basic tests of Game_State passed.")


test_state()
