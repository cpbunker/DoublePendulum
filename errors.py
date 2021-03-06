'''
This module is part of the DoublePendulum computational physics project, as implemented by
Christian Bunker and Leo Bunker, June-July 2020. Credit to Allen B Downey's works "Think
Python" and "Think Complexity" and Stickler and Schachinger's book "Basic Concepts in
Computational Physics" for their help.

Written in Python 3.7.3

errors.py implements specific child classes of Exception for use throughout this project
'''

#######################################################################
# define exception classes
#######################################################################

class SolverError(Exception):
    '''
    Error class for using when something goes wrong in the operation of an ODE solver
    function in the solvers.py module
    '''
    
    pass; #### end solver error

