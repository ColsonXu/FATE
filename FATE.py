import copy

'''
Missionaries.py
("Missionaries and Cannibals" problem)
A SOLUZION problem formulation.
The XML-like tags used here may not be necessary, in the end.
But for now, they serve to identify key sections of this
problem formulation. It is important that COMMON_CODE come
before all the other sections (except METADATA), including COMMON_DATA.

This version includes a check for the use of the Tk graphics client.
If this client is being used, then it loads the visualization module:
Missionaries_Array_VIS_FOR_TK.py.
'''
#<METADATA>
SOLUZION_VERSION = "1.0"
PROBLEM_NAME = "FATE"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['Colson Xu', 'Leo Liao', 'Yujia Lin', 'Yuxuan Lu']
PROBLEM_CREATION_DATE = "5-SEP-2017"

# The following field is mainly for the human solver, via either the Text_SOLUZION_Client.
# or the SVG graphics client.
PROBLEM_DESC=\
'''

'''
#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>

#<COMMON_CODE>


def copy_state(s):
    return copy.deepcopy(s)


def isActionAvailable(state, action, loc):
    # WIP, temporarily returns True
    return True

def takeAction(state, action, loc):
    newState = copy_state(state)
    if action == 'Grow beef':
        newState['board'][loc[0]][loc[1]] = 2
    return newState

def describe_state(s):
    caption = "Polulation:", s['p'], "Gold:", s['gold'], "Wood:", s['wood'], "Food:", s['food'], "Living Quality:", s['lq'], "Temp.:", s['temp']
    return str(caption)


def goal_test(s):
    if s['temp'] < 2 and s['lq'] > 60 and s['p'] > 4500:
        return True
    return False


def goal_message(s):
    return "Wow, you achieved the impossible!"


class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)

#</COMMON_CODE>

#<INITIAL_STATE>

    '''
    Block Code Index:

    0: Plants
    1: Empty Space
    2: Cattle Farm
    3: Coal Mine
    4: Power Plant
    5: House
    6: Ice
    7: Ocean
    '''

row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board = [row]
for i in range(8):
    board.append(row[:])
board.append([7, 7, 7, 7, 7, 7, 7, 7, 7, 6])
INITIAL_STATE = {
                'p': 100,
                'gg_level': 0,
                'gold': 200,
                'wood': 0,
                'food': 0,
                'lq': 100,
                'temp': 0,
                'board': board
                }
#</INITIAL_STATE>

#<OPERATORS>
actions = [('Grow beef', (0, 0))]

OPERATORS = [Operator(
    action + " on row " + str(loc[0] + 1) + ", column " + str(loc[1] + 1),
    lambda state, action1 = action, loc1 = loc: isActionAvailable(state, action1, loc1),
    lambda state, action1 = action, loc1 = loc: takeAction(state, action1, loc1))
    for (action, loc) in actions]
#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

#<STATE_VIS>
render_state = None

def use_BRIFL_SVG():
    global render_state
    #from    Missionaries_SVG_VIS_FOR_BRIFL import render_state as rs
    #render_state = rs
    from Missionaries_SVG_VIS_FOR_BRIFL import render_state
#</STATE_VIS>
