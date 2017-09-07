import copy

'''Missionaries.py
("Missionaries and Cannibals" problem)
A SOLUZION problem formulation.
The XML-like tags used here may not be necessary, in the end.
But for now, they serve to identify key sections of this 
problem formulation.    It is important that COMMON_CODE come
before all the other sections (except METADATA), including COMMON_DATA.

This version includes a check for the use of the Tk graphics client.
If this client is being used, then it loads the visualization module:
Missionaries_Array_VIS_FOR_TK.py.

'''
#<METADATA>
SOLUZION_VERSION = "1.0"
PROBLEM_NAME = "FATE"
PROBLEM_VERSION = "1.1"
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


def can_move(s,m,c):
    pass

def move(olds,m,c):
    pass

def describe_state(s):
    pass

def goal_test(s):
    pass

def goal_message(s):
    return ""


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
INITIAL_STATE = {
                'Population': 100,
                'Greenhouse Gas Level': 0,
                'Gold': 200,
                'Wood': 0,
                'Food': 0,
                'Living Quality': 100,
                'Temp.': 0,
                'Board': [ [0]*10 ]*10
                }
#</INITIAL_STATE>

#<OPERATORS>
MC_combinations = [(1,0),(2,0),(3,0),(1,1),(2,1)]

OPERATORS = [Operator(
    "Cross the river with "+str(m)+" missionaries and "+str(c)+" cannibals",
    lambda s, m1=m, c1=c: can_move(s,m1,c1),
    lambda s, m1=m, c1=c: move(s,m1,c1) ) 
    for (m,c) in MC_combinations]
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

