'''
This module is part of the DoublePendulum computational physics project, as implemented by
Christian Bunker and Leo Bunker, June-July 2020. Credit to Allen B Downey's works "Think
Python" and "Think Complexity" and Stickler and Schachinger's book "Basic Concepts in
Computational Physics" for their help.

Written in Python 3.7.3

solvers.py implements various ways of solving the initial-value ODE, y'(t) = F(y, t)
'''

import errors

import numpy as np

#######################################################################
# define ODE solvers
#######################################################################


#######################################################################
# simple integration rules
# see Stickler pg 65-66
#######################################################################

def ForwardRectangular(yn, tn, f, dt):
    '''
    Forward rectangular rule or explicit Euler method for integration stepping,
    used to solve problem of form y(t) = \int f(t) dt
    
    Args:
    yn, double, the nth y value of function y which is the result of the integration
    tn, double, nth value of the variable being integrated over
    f, function pointer, the function which is the integrand
    dt, double, the step of the integration variable
    
    Returns:
    double, the y_{n+1}th value of y
    '''
    
    return yn + f(yn, tn)*dt; #### end ForwardRectangular
    
    
def BackwardRectangular(yn, tn, f, dt):

    #TODO: define backward rectangular rule
    
    return; #### end backward rectangular
    
    
def CentralRectangular(yn, tn, f, dt):

    #TODO: define central rectangular rule

    return; #### end central rectangular
    
    
def Trapezoidal(yn, tn, f, dt):

    #TODO: define trapezoidal rule

    return; #### end trapezoidal


#######################################################################
# test code
#######################################################################


#######################################################################
# execute code
#######################################################################
if(__name__ == "__main__"):

    pass;
