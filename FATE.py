import copy
from random import randint
import time

'''
FATE.py

"FATE is an environmental game. You are the governer of this area.
Let your people live a high quality life so they don't rebel. Also, please
remember to protect the environment from depletion.

The cost and consequence of each operator is shown below:
Burning trees \t no cost \t emit very large amount of CO2
Cutting down trees \t costs 15 gold \t get 5 wood that can be used to build other buildings
Mining \t cost 10 gold \t produce CO2 and earn 10 gold back each year
Build cattle farm \t costs 5 gold and 5 wood \t get 100 food immediately, and get 20 food per year.
Building power plant \t costs 10 gold \t emit CO2, requires one mining for each power plant
Building house \t costs 5 gold \t can contain 150 people, three houses require one power plant

Other tips for you:
1. When temperature gets too high, random forest fire happens. When temperature
gets even higher, shore area gets flooded.
2. Empty space grow back to forest after 3 years.
3. Temperature, whether house has electricity and if houses are enough are factors that
influence the living quality.
4. Mining gives you money! So try mine first!
5. Burning down too much trees causes temperature rises very fast! Don't do that!

Your goal is to hang in there for 45 years! Go ahead!
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
'''"FATE is an environmental game. You are the governer of this area.
Let your people live a high quality life so they don't rebel. Also, please
remember to protect the environment from depletion.
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

'''
    Returns blocks burnt when a tree burning event is initiated.

    :param int        i:     Index of row of the fire event's center.
    :param int        j:     Index of column of the fire event's center.
    :param Game_State state: Current game state.

    :return list: A list containing the given block plus all adjacent blocks.
'''
def getBurntArea(i, j, state):
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

'''
    The following function is called everytime after one change of state.
    It calculates and refreshes state variables and triggers natural events,
    such as natural wildfire activity, flood, and tree recovery.

    :param Game_State state: The game state processed.
'''
def slowly_change(state):
    if state.gg < 0:
        state.gg = 0
    state.food -= 0.2 * state.p
    state.p = int(1.079 * state.p)
    state.temp = 0.008 * state.gg
    state.gameYear += 1

    # Random Wild Fire when Delta T > 1 (1/3 properbility)
    if state.temp >= 1 and randint(1, 3) == 1:
        forest = False
        while not forest:
            i = randint(0, 9)
            j = randint(0, 9)
            if state.board[i][j] == 0:
                forest = True
                for block in getBurntArea(i, j, state):
                    state.board[block[0]][block[1]] = 1
        print('Due to high temperture, forest fire happened at row %d, column %d, and burned down near blocks.' \
              % (i + 1, j + 1))

    # Flood
    if state.temp >= 1.5:
        print('Sea level rising caused shore area being flooded.')
        for i in range(10):
            if (state.board[i].count(7) == 9 and state.board[i][9] == 6) or \
            (state.board[i].count(7) == 10):
                nextRow = i - 1
                break
        change_list = []
        while True:
            index = randint(0, 9)
            if state.board[nextRow][index] != 7 and len(change_list) < 4:
                change_list.append(index)
            if len(change_list) == 4 or len(change_list) == (10 - state.board[nextRow].count(7)):
                break
        for i in range(4):
            try:
                state.board[nextRow][change_list.pop()] = 7
            except:
                break

    # Empty space grow back to forest
    for i in range(10):
        for j in range(10):
            if state.board[i][j] == 1:
                if (i, j) not in state.emptyDict and state.board[i][j] == 1:
                    state.emptyDict[(i, j)] = 0
                elif (i, j) in state.emptyDict and state.emptyDict[(i, j)] < 5:
                    state.emptyDict[(i, j)] += 1
                elif (i, j) in state.emptyDict and state.emptyDict[(i, j)] == 5:
                    state.board[i][j] = 0
                    del state.emptyDict[(i, j)]
                elif (i, j) in state.emptyDict and state.board[i][j] != 1:
                    del state.emptyDict[(i, j)]

    # Count every facilities on the game board for variable change
    for i in range(10):
        state.gg += 15 * state.board[i].count(4)
        state.gg += 10 * state.board[i].count(2)
        state.gg -= 0.5 * state.board[i].count(0)
        state.gold += 10 * state.board[i].count(3)
        state.food += 20 * state.board[i].count(2)

    # LQ
    electricity = 0
    house = 0
    for i in range(10):
        for j in range(10):
            if state.board[i][j] == 4:
                electricity += 1
            if state.board[i][j] == 5:
                house += 1
    if house > electricity * 3:
        state.lq -= 10
    if state.temp >= 1.5:
        state.lq -= 3
    if state.p >= 150 * house and state.p >= 350:
        state.lq -= 8
    if house <= electricity * 3 and state.temp < 1.5 and state.p < 150 * house:
        state.lq += 2
        if state.lq > 100:
            state.lq = 100

    print('GameYear: %d' % state.gameYear)


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
                'gameYear': 0,
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
        if self.nextInput == 'player':
            if 'I am' in action:
                return True
            return False
        elif self.nextInput == 'action':
            # Filtrates all operators that are not a row/column selection operator
            # or a dummy operator.
            if not 'Select' in action and action != 'Dummy operator' and not \
            'I am' in action:
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

        '''
        After the player selects an operator, FATE will change the pointer
        storing type of the next input the player is going to make, `nextInput`, to
        the next value it ought to have.
        The order of entering those operators are action, row, and column.
        '''

        if self.nextInput == 'action':
            newState.nextInput = 'row'
            newState.selectedAction = action

        elif self.nextInput == 'row':
            newState.nextInput = 'col'

            # Converts row selection to index of the list for the board.
            rowSelected = int(action[-1])
            if rowSelected == 0:
                newState.selectedRow = 9
            else:
                newState.selectedRow = rowSelected - 1

        elif self.nextInput == 'col':
            actionSelected = self.selectedAction
            i = self.selectedRow

            # Converts column selection to index of the second-level list for the board.
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

        # Changes state of the block where the player chooses.
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
            # if you burn the glacial, all board turns to water. just for fun
            if newState.board[i][j] == 0:
                for block in getBurntArea(i, j, self):
                    if not (self.board[block[0]][block[1]] == 6 or \
                            self.board[block[0]][block[1]] == 7):
                        newState.board[block[0]][block[1]] = 1
                for i in range(len(getBurntArea(i, j, self))):
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
                newState.gold -= 5
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
                newState.gg += 15
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

# change later
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
            'Fasting forward 5 states'] + \
            ['Dummy operator' for i in range(4)] + \
            ['Select %s %d' %(string, i) for string in ['row', 'column'] for i \
            in range(1, 11)]
'''
Dummy operator allows the player to enter 11 rather than 6 for row
1, enters 12 rather than 7 for row 2, etc., so the row and column
selection process can be more user-friendly.
'''

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
    # from Missionaries_SVG_VIS_FOR_BRIFL import render_state as rs
    # render_state = rs
    from Missionaries_SVG_VIS_FOR_BRIFL import render_state
#</STATE_VIS>
