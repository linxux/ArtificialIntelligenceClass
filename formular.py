#   formula.py
#-*- encoding: utf-8 -*-

import sys
from decimal import *

def debug(msg):
    print "[DEBUG]:"+msg
def get_cur_info():
    """
    Return the frame object for the caller's stack frame
    """
    print "[DEBUG]call <"+sys._getframe().f_back.f_code.co_name+">", "Line:"+str(sys._getframe().f_back.f_lineno)
def split_method():
    print "=" * 40

def gaussian_formula(xValues):
    get_cur_info()
    if xValues is None:
        return
    M = len(xValues)
    totalX = 0
    for x in xValues:
        totalX += x
    u = Decimal(totalX) / Decimal(M)

    totalY = 0
    for x in xValues:
        totalY += Decimal((Decimal(x) - Decimal(u)) ** 2)
    y = Decimal(totalY) / Decimal(M)

    print 'M is %(num)d, u is %(uNum)f, y is %(yNum)f' % {'num': M, 'uNum': float(u), 'yNum': float(y)}

def linear_regression_formula(xValues, yValues):
    get_cur_info()

    sumX1 = 0
    sumSquareX1 = 0
    for x in xValues:
        sumX1 += x
        sumSquareX1 += x ** 2

    sumY1 = 0
    for y in yValues:
        sumY1 += y
    
    sumX1Y1 = 0
    m = len(xValues)
    for index in range(m):
        sumX1Y1 += xValues[index] * yValues[index]

    W1 = Decimal(m * sumX1Y1 - sumX1 * sumY1) / Decimal(m * sumSquareX1 - sumX1 ** 2)
    W0 = Decimal(sumY1 - W1 * sumX1) / Decimal(m)
    print ("the W1 = [ %(w1)f ], and W0 = [ %(w0)f ]" % {"w1": float(W1), "w0": float(W0)})

def markovChain_A_State(A0, A1A0, A1B0, step):
    get_cur_info()
    
    f_r1r0 = bayes_furmula_r1r0(A1A0, A1B0)

    for i in range(step):
        A0 = f_r1r0(A0)
        print ("P(A%(cur)d|A%(pre)d) = %(value)f" % 
                {"cur": i+1, "pre": i, "value": A0})

def bayes_furmula_r1r0(r1r0, r1s0):
    return lambda r0: r1r0 * r0 + r1s0 * (1-r0)

def markovChian_A_InfiniteState(A1A0, A1B0):
    """
    P(A1) = P(A0)
    ==> P(A1 | A0)P(A0) + P(A1 | B0)P(B0)
    (P(B0) = 1 - P(A0))
    """
    get_cur_info()
    AInifite = A1B0 / (A1B0 - A1A0 + 1)
    print ("P(A1|A0) = %(v1)f\nP(A1|B0) = %(v2)f"
            % {"v1": A1A0, "v2": A1B0})
    print ("The Stationary Distribution value is: %(inifite)f"
            % {"inifite": AInifite})

if __name__ == '__main__':
    gaussian_formula([3,4,5,6,7])
    #split_method()
    #gaussian_formula([8,7,5,3,2])
    #split_method()
    #gaussian_formula([-2,-1,0,1,2])
    #split_method()
    #gaussian_formula([3,2,0,-2,-3])
    #split_method()
    #linear_regression_formula([3, 6, 4, 5],[0, -3, -1, -2])
    split_method()
    #linear_regression_formula([0, 1, 2, 3, 4],[3, 6, 7, 8, 11])
    markovChain_A_State(1, 0.5, 1, 3)
    split_method()
    markovChian_A_InfiniteState(0.6, 0.2)
