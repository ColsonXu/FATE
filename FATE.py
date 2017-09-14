import copy
from random import randint
import time

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
"WIP"
'''
#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>

#<COMMON_CODE>

'''A list which stores integers representing a state that can change to other
states.'''
MUTABLE_STATES = [0, 1]


'''
    Makes a deep copy of a Game_State instance.

    :param Game_State s: The source that is being copied.

    :return Game_State: The copied Game_State instance.
'''
def copy_state(s):
    return s.__copy__()

def describe_state(stateObject):
    return str(stateObject)

def op_blocks(i, j, state):
    blocks = [[i, j]]
    if i > 0:
        blocks.append([i - 1, j])
    if i < 9:
        blocks.append([i + 1, j])
    if j > 0:
        blocks.append([i, j - 1])
    if j < 9:
        blocks.append([i, j + 1])
    for block in blocks:
        if state.board[block[0]][block[1]] != 0:
            del blocks[blocks.index(block)]
    return blocks

def slowly_change(stateObject):
    if stateObject.gg < 0:
        stateObject.gg = 0
    stateObject.food -= 0.2 * stateObject.p
    stateObject.p = int(1.079 * stateObject.p)
    stateObject.temp = 0.01 * stateObject.gg
    stateObject.gameYear += 1

    print('GameYear: %d' % stateObject.gameYear)

    if stateObject.temp >= 1 and randint(1, 3) == 1:
        forest = False
        while not forest:
            i = randint(0, 9)
            j = randint(0, 9)
            if stateObject.board[i][j] == 0:
                forest = True
                for block in op_blocks(i, j, stateObject):
                    stateObject.board[block[0]][block[1]] = 1
        print('Due to high temperture, forest fire happened at row %d, column %d, and burned down near blocks.' \
              % (i + 1, j + 1))

    if stateObject.temp >= 1.5:
        print('Sea level rising caused shore area being flooded.')
        for i in range(10):
            if (stateObject.board[i].count(7) == 9 and stateObject.board[i][9] == 6) or \
            (stateObject.board[i].count(7) == 10):
                nextRow = i - 1
                break
        change_list = []
        while True:
            index = randint(0, 9)
            if stateObject.board[nextRow][index] != 7 and len(change_list) < 4:
                change_list.append(index)
            if len(change_list) == 4 or len(change_list) == (10 - stateObject.board[nextRow].count(7)):
                break
        for i in range(4):
            try:
                stateObject.board[nextRow][change_list.pop()] = 7
            except:
                break

    for i in range(10):
        for j in range(10):
            if (i, j) not in stateObject.emptyDict and stateObject.board[i][j] == 1:
                stateObject.emptyDict[(i, j)] = 0
            elif (i, j) in stateObject.emptyDict and stateObject.emptyDict[(i, j)] < 3:
                stateObject.emptyDict[(i, j)] += 1
            elif (i, j) in stateObject.emptyDict and stateObject.emptyDict[(i, j)] == 3:
                stateObject.board[i][j] = 0
                del(stateObject.emptyDict[(i, j)])
            elif (i, j) in stateObject.emptyDict and stateObject.board[i][j] != 1:
                del(stateObject.emptyDict[(i, j)])


    for i in range(10):
        stateObject.gg += 15 * stateObject.board[i].count(4)
        stateObject.gg += 10 * stateObject.board[i].count(2)
        stateObject.gg -= 0.5 * stateObject.board[i].count(0)
        stateObject.gold += 10 * stateObject.board[i].count(3)
        stateObject.food += 20 * stateObject.board[i].count(2)

    electricity = 0
    house = 0
    for i in range(10):
        for j in range(10):
            if stateObject.board[i][j] == 4:
                electricity += 1
            if stateObject.board[i][j] == 5:
                house += 1
    if house > electricity * 3:
        stateObject.lq -= 10
    if stateObject.temp >= 1.5:
        stateObject.lq -= 3
    if stateObject.p >= 150 * house and stateObject.p >= 350:
        stateObject.lq -= 8
    if house <= electricity * 3 and stateObject.temp < 1.5 and stateObject.p < 150 * house:
        stateObject.lq += 2
        if stateObject.lq > 100:
            stateObject.lq = 100


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

INITIAL_STATE_DICT = {
                'p': 100,               # Population
                'gg': 0,                # Greenhouse Gas
                'gold': 50,             # Gold
                'wood': 0,              # Wood
                'food': 120,              # Food
                'lq': 100,              # Living Quality
                'temp': 0,              # Average Temperature
                'board': board,         # Game Board
                'nextInput': 'action',  # The next input that the user is making
                'selectedAction': '',   # Current action selected by the user
                'selectedRow': 0,       # Current row selected by the user
                'playerType': '',
                'gameYear': 1,
                'emptyDict': {}
                }

class Game_State:
    '''
        Game_State constructor.

        :param dict state: Initial state of the new Game_State instance.
    '''
    def __init__(self, state = INITIAL_STATE_DICT):
        self.p = state['p']
        self.gg = state['gg']
        self.gold = state['gold']
        self.wood = state['wood']
        self.food = state['food']
        self.lq = state['lq']
        self.temp = state['temp']
        self.board = state['board']
        self.nextInput = state['nextInput']
        self.selectedAction = state['selectedAction']
        self.selectedRow = state['selectedRow']
        self.playerType = state['playerType']
        self.gameYear = state['gameYear']
        self.emptyDict = state['emptyDict']

    '''
        Makes a deep copy of the current instance.

        :return Game_State: The copied Game_State instance.
    '''
    def __copy__(self):
        return copy.deepcopy(self)

    '''
        Returns a caption which represents some information about the current
        state.

        :return str: The caption representing the current state.
    '''
    def __str__(self):
        caption = "Polulation:", int(self.p), "Gold:", int(self.gold), \
                  "Wood:", int(self.wood), "Food:", int(self.food), \
                  "Living Quality:", int(self.lq), "ΔTemp.:", \
                  '%.2f' %self.temp
        return str(caption)  #return caption or the state???

    '''
        Compares two states and returns whether they are identical.

        :param Game_State other: The other state being compared.

        :return bool
    '''
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
        return (str(self)).__hash__()

    '''
        Evaluates whether an operator is legal under the current state.

        :param str action: The operator evaluated.

        :return bool
    '''
    def isActionAvailable(self, action):
        if self.nextInput == 'action':
            '''Filtrates all operators that are not a row/column selection operator
            or a dummy operator.'''
            if not 'Select' in action and action != 'Dummy operator':
                return True
            return False
        elif self.nextInput == 'row':
            '''Filtrates all operators that are a row selection operator.'''
            if 'Select row' in action:
                return True
            return False
        elif self.nextInput == 'col':
            '''Filtrates all operators that are a column selection operator.'''
            if 'Select column' in action:
                return True
            return False

    '''
        Executes an operator.

        :param str action: The operator executed.

        :return Game_State: A new game state produced by the action.
    '''
    def takeAction(self, action):
        newState = self.__copy__()

        '''After the player selects an operator, FATE will change the pointer
        storing type of the next input the player is going to make, `nextInput`, to
        the next value it ought to have.
        The order of entering those operators are action, row, and column.'''

        if self.nextInput == 'action':
            newState.nextInput = 'row'
            newState.selectedAction = action

        elif self.nextInput == 'row':
            newState.nextInput = 'col'
            '''Converts row selection to index of the list for the board.'''
            rowSelected = int(action[-1])
            if rowSelected == 0:
                newState.selectedRow = 9
            else:
                newState.selectedRow = rowSelected - 1

        elif self.nextInput == 'col':
            actionSelected = self.selectedAction
            i = self.selectedRow
            '''Converts column selection to index of the second-level list for
            the board.'''
            colSelected = int(action[-1])
            if colSelected == 0:
                j = 9
            else:
                j = colSelected - 1
            newState = self.changeGrid(i, j, actionSelected)
            newState.nextInput = 'action'

        return newState

    def changeGrid(self, i, j, actionSelected):
        newState = self.__copy__()
        apply = True

        '''Changes state of the block where the player chooses.'''
        if actionSelected == 'Build cattle farm':
            if newState.wood >= 5 and newState.gold >= 5 and newState.board[i][j] == 1:
                newState.board[i][j] = 2
                newState.wood -= 5
                newState.gold -= 5
                newState.food += 100
            else:
                print ("You don't have 5 wood and 5 gold or the selected square is not empty")
                apply = False

        elif actionSelected == 'Burn down forest':
            '''if you burn the glacial, all board turns to water. just for fun'''
            if newState.board[i][j] == 0:
                for block in op_blocks(i, j, self):
                    if not (self.board[block[0]][block[1]] == 6 or \
                            self.board[block[0]][block[1]] == 7):
                        newState.board[block[0]][block[1]] = 1
                for i in range(len(op_blocks(i, j, self))):
                    newState.gg += 20
            else:
                if i == 9 and j == 9:
                    for x in range(10):
                        for y in range(10):
                            newState.board[x][y] = 7
                    newState.lq = 0
                else:
                    print('You can only burn down forest')
                    apply = False


        elif actionSelected == 'Build house':
            power = 0
            house = 0
            for x in range(10):
                for y in range(10):
                    if newState.board[x][y] == 4:
                        power += 1
                    if newState.board[x][y] == 5:
                        house += 1
            electricity = True
            if power * 3 <= house:
                print('You need one power plant for every three house')
                apply = False
                electricity = False
            if newState.board[i][j] == 1 and newState.gold >= 5 and electricity == True:
                newState.board[i][j] = 5
                newState.gold -= 5 # capacity 1500, if full, LQ decrease 30 food and temp influence LQ
            elif electricity == True:
                print ("The space is not available or you don't have enough money")
                apply = False
        elif actionSelected == 'Cut down forest':
            if newState.board[i][j] == 0 and newState.gold >= 15:
                newState.board[i][j] = 1
                newState.wood += 5
                newState.gold -= 15
            else:
                print ("You can only cut down forest. At least 15 gold is needed")
                apply = False

        elif actionSelected == 'Mine coal':
            if newState.board[i][j] == 1 and newState.gold >= 10:
                newState.board[i][j] = 3
                newState.gold -= 10
                newState.gg += 20
            else:
                print ("You can only mine on empty spaces, or you don't have 10 gold.")
                apply = False

        elif actionSelected == 'Build power plant':
            mining = 0
            powerplant = 0
            for x in range(10):
                for y in range(10):
                    if newState.board[x][y] == 3:
                        mining += 1
                    if newState.board[x][y] == 4:
                        powerplant += 1
            mine = True
            if powerplant >= mining:
                print('One mine required for each powerplant')
                mine = False
            if newState.wood >= 5 and newState.gold >= 15 and newState.board[i][j] == 1 and mine == True:
                newState.board[i][j] = 4
                newState.wood -= 5
                newState.gold -= 15
            elif mine == True:
                print ("You need 15 gold and 5 wood to build a powerplant. And you can only build on empty space.")
                apply = False

        elif actionSelected == 'Fasting forward 5 states':
            for i in range(5):
                slowly_change(newState)

        if apply:#when temp rise to 1 and more, there's 1/3 chance of a forest fire that also burn down near blocks
            slowly_change(newState)

        time.sleep(2.5)
        return newState

'''
    Tests whether the player achieves the final goal:
    - Temperature risen should be less than 2 degrees Celsius
    - Living quality level should be greater than 60
    - Population should be more than 4500

    :param Game_State state: The game state evaluated.

    :return bool
'''
def goal_test(state):
    if state.gameYear == 45:
        print('You achieved the impossible! You managed to survive 60 years with \
        your people, but the environment is still getting worse and worse.')
        return True
    if state.gameYear < 45:
        if state.lq <= 60:
            print('Your people are living in hell! They rebelled!')
            return True
        if state.food <= 0:
            print('Your people starved to death!')
            return True
        if state.temp >= 2.5:
            print('The temperature is too high! Your land become unlivable.')
            return True
        return False



'''
    :param mixed s

    :return str
'''

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

INITIAL_STATE = Game_State(INITIAL_STATE_DICT)

#</INITIAL_STATE>

#<OPERATORS>
actions = [ 'Burn down forest',
            'Cut down forest',
            'Build cattle farm',
            'Mine coal',
            'Build power plant',
            'Build house',
            'Fasting forward 5 states',
            'I am a human',
            'I am not a human'] + \
            ['Dummy operator' for i in range(2)] + \
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
#</GOAL_MESSAGE_FUNCTION>

#<STATE_VIS>
render_state = None

def use_BRIFL_SVG():
    global render_state
    #from    Missionaries_SVG_VIS_FOR_BRIFL import render_state as rs
    #render_state = rs
    from Missionaries_SVG_VIS_FOR_BRIFL import render_state
#</STATE_VIS>
