'''FATE_Array_VIS_FOR_TK.py
Version of Aug. 5, 2017.

'''

from show_state_array import initialize_tk, state_array, state_display, STATE_WINDOW, test
import Missionaries
from tkinter import font

myFont=None

WIDTH = 500
HEIGHT = 500
TITLE = 'FATE'

def initialize_vis():
  initialize_tk(WIDTH, HEIGHT, TITLE)
  
def render_state(s):
    # Note that font creation is only allowed after the Tk root has been
    # defined.  So we check here if the font creation is still needed,
    # and we do it (the first time this method is called).
    global myFont
    if not myFont:
        myFont = font.Font(family="Helvetica", size=18, weight="bold")
    print("In render_state, state is "+str(s))
    # Create the default array of colors
    plants = (67,160,71)
    ice = (245,245,245)
    beef = (194,24,91)
    ocean = (2,136,209)
    empty = (161,136,127)
    house = (253,216,53)
    power = (96,125,139)
    mine = (0,0,0)


    row = [plants] * 10
    the_color_array = [row, row[:], row[:], row[:], row[:], row[:], row[:], row[:], row[:], [ocean] * 9 + [ice]]
    the_string_array = []
    
    caption="Current state of the puzzle. Textual version: "+Missionaries.describe_state(s)
    the_state_array = state_array(color_array=the_color_array,
                                  string_array=the_string_array,
                                  text_font=myFont,
                                  caption=caption)
    print("the_state_array is: "+str(the_state_array))
    the_state_array.show()
