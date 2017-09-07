'''FATE_Array_VIS_FOR_TK.py
Version of Aug. 5, 2017.

'''

from show_state_array import initialize_tk, state_array, state_display, STATE_WINDOW, test
import FATE
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
        myFont = font.Font(family="Helvetica", size=10, weight="bold")
    print("In render_state, state is "+str(s))
    # Create the default array of colors
    plants = (67,160,71)    # 0
    ice = (245,245,245)     # 6
    beef = (194,24,91)      # 2
    ocean = (2,136,209)     # 7
    empty = (161,136,127)   # 1
    house = (253,216,53)    # 5
    power = (96,125,139)    # 4
    mine = (0,0,0)          # 3

    translate = {plants: 'Tree', ice: 'Ice', beef: 'Cattles', ocean: 'Ocean',\
                 empty: 'Empty', house: 'House', power: 'Industry', mine: 'Mining'}

    color_dic = {0: plants, 1: empty, 2: beef, 3: mine, 4: power, 5: house, 6: ice, 7: ocean}
    row = [plants] * 10
    the_color_array = [row, row[:], row[:], row[:], row[:], row[:], row[:], row[:], row[:], [ocean] * 9 + [ice]]
    the_string_array = [['']*10]*10
      
    
    for i in range(10):
      for j in range(10):
        the_color_array[i][j] = color_dic[s['board'][i][j]]
        the_string_array[i][j] = translate[the_color_array[i][j]]

    
    
    
    caption="Current state of the puzzle. Textual version: " + FATE.describe_state(s)
    the_state_array = state_array(color_array=the_color_array,
                                  string_array=the_string_array,
                                  text_font=myFont,
                                  caption=caption)
    print("the_state_array is: "+str(the_state_array))
    the_state_array.show()
