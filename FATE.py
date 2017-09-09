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

'''A list which stores integers representing a state that can change to other
states.'''
MUTABLE_STATES = [0, 1, 3]

def copy_state(s):
    return s.__copy__()

class Game_state:
    def __init__(self, state):
        self.state = state

    def __call__(self):
        return self.state

    def __copy__(self):
        newState = copy.deepcopy(self)
        return newState

    def __str__(self):
        caption = "Polulation:", self()['p'], "Gold:", self()['gold'], \
                  "Wood:", self()['wood'], "Food:", self()['food'], \
                  "Living Quality:", self()['lq'], "ΔTemp.:", \
                  self()['temp']
        return str(caption)

    def __eq__(self, other):
        if self is other:
            return True
        elif self is None:
            return False
        elif other is None:
            return False
        else:
            return True

    def __hash__(self):
        return (str(self)).hash()

    def isActionAvailable(self, action):
        if self()['nextInput'] == 'action':
            '''Filtrates all operators that are not a row/column selection operator
            or a dummy operator.'''
            if not 'Select' in action and action != 'Dummy operator':
                return True
            return False
        elif self()['nextInput'] == 'row':
            '''Filtrates all operators that are a row selection operator.'''
            if 'Select row' in action:
                actionSelected = self()['selectedAction']
                '''Converts row selection to index of the list for the board.'''
                row = int(action[-1])
                if row == 0:
                    i = 9
                else:
                    i = row - 1
                '''Loops through all blocks in the row and sees if there is any
                block where the action selected is applicable.'''
                for j in range(10):
                    blockState = self()['board'][i][j]
                    if len(list(filter(lambda x: blockState == x, MUTABLE_STATES))):
                        blockState = self()['board'][i][j]
                        if len(list(filter(lambda x: blockState == x, MUTABLE_STATES))):
                            if blockState == 0 and actionSelected in \
                            ['Burn down forest', 'Cut down forest']:
                                return True
                            elif blockState == 1 and actionSelected in \
                            ['Build cattle farm', 'Mine coal', 'Build house']:
                                return True
                            elif blockState == 3 and actionSelected == 'Build power plant':
                                return True
            return False
        elif self()['nextInput'] == 'col':
            '''Filtrates all operators that are a column selection operator.'''
            if 'Select column' in action:
                actionSelected = self()['selectedAction']
                i = self()['selectedRow']
                '''Converts column selection to index of the second-level list for
                the board.'''
                col = int(action[-1])
                if col == 0:
                    j = 9
                else:
                    j = col - 1
                blockState = self()['board'][i][j]
                '''Evaluates all blocks in the row selected and sees if there is any
                block where the action selected is applicable.'''
                if len(list(filter(lambda x: blockState == x, MUTABLE_STATES))):
                    blockState = self()['board'][i][j]
                    if len(list(filter(lambda x: blockState == x, MUTABLE_STATES))):
                        if blockState == 0 and actionSelected in \
                        ['Burn down forest', 'Cut down forest']:
                            return True
                        elif blockState == 1 and actionSelected in \
                        ['Build cattle farm', 'Mine coal', 'Build house']:
                            return True
                        elif blockState == 3 and actionSelected == 'Build power plant':
                            return True
        return False

    def takeAction(self, action):
        newState = self.__copy__()

        '''After the player selects an operator, FATE will change the pointer
        storing type of the next input the player is going to make, `nextInput`, to
        the next value it ought to have.
        The order of entering those operators are action, row, and column.'''

        if self()['nextInput'] == 'action':
            newState()['nextInput'] = 'row'
            newState()['selectedAction'] = action

        elif self()['nextInput'] == 'row':
            newState()['nextInput'] = 'col'
            '''Converts row selection to index of the list for the board.'''
            rowSelected = int(action[-1])
            if rowSelected == 0:
                newState()['selectedRow'] = 9
            else:
                newState()['selectedRow'] = rowSelected - 1

        elif self()['nextInput'] == 'col':
            newState()['nextInput'] = 'action'
            actionSelected = self()['selectedAction']
            i = self()['selectedRow']
            '''Converts column selection to index of the second-level list for
            the board.'''
            colSelected = int(action[-1])
            if colSelected == 0:
                j = 9
            else:
                j = colSelected - 1

            '''Changes self() of the block where the player chooses.'''
            if actionSelected == 'Build cattle farm':
                newState()['board'][i][j] = 2
                newState()['wood'] -= 5
                newState()['gold'] -= 5
                newState()['food'] += 100

            elif actionSelected == 'Burn down forest':
                if i == 9 and j == 9:
                    for x in range(10):
                        for y in range(10):
                            newState()['board'][x][y] = 7

                if newState()['board'][i][j] == 7:
                    print('You cannot burn down ocean.')
                else:
                    op_blocks = [[i, j]]
                    if i > 0:
                        op_blocks.append([i - 1, j])
                    if i < 9:
                        op_blocks.append([i + 1, j])
                    if j > 0:
                        op_blocks.append([i, j - 1])
                    if j < 9:
                        op_blocks.append([i, j + 1])

                    for block in op_blocks:
                        if not (self()['board'][block[0]][block[1]] == 6 or \
                                self()['board'][block[0]][block[1]] == 7):
                            newState()['board'][block[0]][block[1]] = 1
                    for i in range(len(op_blocks)):
                        newState()['gg'] += 25


            elif actionSelected == 'Build house':
                newState()['board'][i][j] = 5
                newState()['gold'] -= 5 # capacity 1500, LQ decrease by 10 if no power, by 30 if full WIP

            elif actionSelected == 'Cut down forest':
                newState()['board'][i][j] = 1
                newState()['wood'] += 5
                newState()['gold'] -= 15

            elif actionSelected == 'Mine coal':
                newState()['board'][i][j] = 3
                newState()['gold'] -= 10
                newState()['gg'] += 20

            elif actionSelected == 'Build power plant':
                newState()['board'][i][j] = 4
                #pre-req mining one, can supply 3 house

            for i in range(10):
                newState()['gg'] += 15 * self()['board'][i].count(4)
                newState()['gg'] += 10 * self()['board'][i].count(2)
                newState()['gg'] -= 0.5 * self()['board'][i].count(0)
                newState()['gold'] += 10 * self()['board'][i].count(3)
                #decrease of food in progress, 1 food for 5 people
        return newState

def goal_test(state):
    s = state()
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

initialState = {
                'p': 100,               # Population
                'gg': 0,                # Greenhouse Gas
                'gold': 50,             # Gold
                'wood': 0,              # Wood
                'food': 0,              # Food
                'lq': 100,              # Living Quality
                'temp': 0,              # Average Temperature
                'board': board,         # Game Board
                'nextInput': 'action',  # The next input that the user is making
                'selectedAction': '',   # Current action selected by the user
                'selectedRow': 0,       # Current row selected by the user
                }

INITIAL_STATE = Game_state(initialState)

#</INITIAL_STATE>

#<OPERATORS>
actions = [ 'Burn down forest',
            'Cut down forest',
            'Build cattle farm',
            'Mine coal',
            'Build power plant',
            'Build house'] + \
            ['Dummy operator' for i in range(5)] + \
            ['Select %s %d' %(string, i) for string in ['row', 'column'] for i \
            in range(1, 11)]
'''Dummy operator allows the player to enter 11 rather than 6 for row
1, enters 12 rather than 7 for row 2, etc., so the row and column
selection process can be more user-friendly.'''

OPERATORS = [Operator(
    action,
    lambda state, action1 = action: state.isActionAvailable(action1),
    lambda state, action1 = action: state.takeAction(action1))
    for action in actions]
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
