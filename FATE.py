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

    if action == 'Build cattle farm':
        newState['board'][loc[0]][loc[1]] = 2

    elif action == 'Burn down forest':
        newState['board'][loc[0]][loc[1]] = 1

        left_edge = loc[0] == 0 and (not loc[1] == 0) and (not loc[1] == 9)
        right_edge = loc[0] == 9 and (not loc[1] == 0) and (not loc[1] == 9)
        up_edge = loc[1] == 0 and (not loc[0] == 0) and (not loc[0] == 9)
        low_edge = loc[1] == 9 and (not loc[0] == 0) and (not loc[0] == 9)
        ul_corner = loc[0] == 0 and loc[1] == 0
        ur_corner = loc[0] == 9 and loc[1] == 0
        dl_corner = loc[0] == 0 and loc[1] == 9
        dr_corner = loc[0] == 9 and loc[1] == 9

        if left_edge:
            op_blocks = [
            [loc[0] + 1, loc[1]],
            [loc[0], loc[1] - 1],
            [loc[0], loc[1] + 1]
            ]
        elif right_edge:
            op_blocks = [
            [loc[0] - 1, loc[1]],
            [loc[0], loc[1] - 1],
            [loc[0], loc[1] + 1]
            ]
        elif up_edge:
            op_blocks = [
            [loc[0] - 1, loc[1]],
            [loc[0] + 1, loc[1]],
            [loc[0], loc[1] + 1]
            ]
        elif low_edge:
            op_blocks = [
            [loc[0] - 1, loc[1]],
            [loc[0] + 1, loc[1]],
            [loc[0], loc[1] - 1]
            ]
        elif ul_corner:
            op_blocks = [
            [loc[0] + 1, loc[1]],
            [loc[0], loc[1] + 1]
            ]
        elif ur_corner:
            op_blocks = [
            [loc[0] - 1][loc[1]],
            [loc[0]][loc[1] + 1]
            ]
        elif dl_corner:
            op_blocks = [
            [loc[0] + 1, loc[1]],
            [loc[0], loc[1] - 1]
            ]
        elif dr_corner:
            op_blocks = [
            [loc[0] - 1, loc[1]],
            [loc[0], loc[1] - 1]
            ]
        elif not (left_edge or right_edge or up_edge or low_edge):
            op_blocks = [
            [loc[0] - 1, loc[1]],
            [loc[0] + 1, loc[1]],
            [loc[0], loc[1] - 1],
            [loc[0], loc[1] + 1]
            ]
        
        for block in op_blocks:
            if not (state['board'][block[0]][block[1]] == 6 or state['board'][block[0]][block[1]] == 7):
                newState['board'][block[0]][block[1]] = 1

        print(newState['board'])

    elif action == 'Build house':
        newState['board'][loc[0]][loc[1]] = 5

    elif action == 'Cut down forest':
        newState['board'][loc[0]][loc[1]] = 1

    elif action == 'Mine coal':
        newState['board'][loc[0]][loc[1]] = 3

    elif action == 'Build power plant':
        newState['board'][loc[0]][loc[1]] = 4

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

row = [0] * 10
board = [row[:] for i in range(9)]
board.append([7, 7, 7, 7, 7, 7, 7, 7, 7, 6])

INITIAL_STATE = {
                'p': 100,               # Population
                'gg': 0,                # Greenhouse Gas
                'gold': 200,            # Gold
                'wood': 0,              # Wood
                'food': 0,              # Food
                'lq': 100,              # Living Quality
                'temp': 0,              # Average Temperature
                'board': board          # Game Board
                }

#</INITIAL_STATE>

#<OPERATORS>
actions = [
            ('Burn down forest', (9,8)), 
            ('Build cattle farm', (0,1)), 
            ('Build house', (0,2)), 
            ('Cut down forest', (0,3)), 
            ('Mine coal', (0,4)), 
            ('Build power plant', (0,5))
          ]

OPERATORS = [Operator(
    action + " on row " + str(loc[0]) + ", column " + str(loc[1]),
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
