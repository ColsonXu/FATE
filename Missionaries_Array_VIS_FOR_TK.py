'''FATE_Array_VIS_FOR_TK.py
Version of Aug. 5, 2017.

'''

from show_state_array import initialize_tk, state_array, state_display, STATE_WINDOW, test

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
    green = (67,160,71)
    white = (245,245,245)
    burgendy = (194,24,91)
    blue = (2,136,209)

    row = [green] * 10
    the_color_array = [row, row[:], row[:], row[:], row[:], row[:], row[:], row[:], row[:], [blue] * 9 + [white]]
    the_string_array = []
    
    caption="Current state of the puzzle. Textual version: "+str(s)        
    the_state_array = state_array(color_array=the_color_array,
                                  string_array=the_string_array,
                                  text_font=myFont,
                                  caption=caption)
    print("the_state_array is: "+str(the_state_array))
    the_state_array.show()
