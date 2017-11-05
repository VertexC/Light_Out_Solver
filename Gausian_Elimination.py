#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import math
import time
from puzzle import *

def GE(f_m, pv, m, n):
    cost = 0
    # put f_m and pv into matrix and make pv the last column
    # thus, f_m is not changed
    fm = np.zeros((m * n, m * n + 1))
    for i in range(0, m * n):
        for j in range(0, m * n + 1):
            if (j < m * n):
                fm[i][j] = f_m[i][j]
            else:
                fm[i][j] = pv[i]
    '''
    # prepare row_exchange
    row_exchange = []
    for i in range(0, m * n):
        row_exchange.append(i)
    '''
    # perform GE with % 2
    for i in range(0, m * n):
        # need to exchange row
        if (fm[i][i] == 0):
            for j in range(i + 1, m * n):
                if (fm[j][i] == 1):
                    # find the row to exchange
                    temp = []
                    temp = copy.copy(fm[j])
                    fm[j] = copy.copy(fm[i])
                    fm[i] = copy.copy(temp)
                    '''
                  # record row exchange in row_exchange
                  temp = row_exchange[j]
                  row_exchange[j] = row_exchange[i]
                  row_exchange[i] = temp
                  '''
                    break
            if (fm[i][i] == 0):
                # there is no row to exchange
                continue
        # here, the ith element of row is 1
        for j in range(i + 1, m * n):
            if (fm[j][i] == 1):
                # do the elimination
                fm[j][:] = (fm[j][:] - fm[i][:]) % 2
                cost += m*n + 1
    #print(fm)
    #tart back substitution
    temp_result = np.zeros((m * n,1))
    for row in reversed(range(0, m * n)):
        #first one
        pivot = -1
        for col in range(0, m * n):
            if(fm[row][col] == 1):
                pivot = col
                break
        if(pivot == -1):
            #no one in this row
            continue
        sum = fm[row][m * n]#b
        for col in range(pivot + 1, m * n):
            sum = (sum - fm[row][col] * temp_result[col]) % 2
            cost += 3
        temp_result[pivot] = sum
    # take result factor into list of single steps
    step = []
    for i in range(0, m * n):
        if (temp_result[i] == 1):
            row = math.floor(i / n)
            col = i % n
            step.append([row, col])
    return step, cost

if __name__ == "__main__":
    m = 8
    n = 8
    # random generated 100 puzzle matrix and convert them into vector
    pv_l = []
    for i in range(0, 100):
        p = puzzle(m, n)
        p.random_created(m, n)
        # conver p.p matrix into vector pv
        pv = np.zeros((m * n, 1))
        for row in range(0, m):
            for col in range(0, n):
                pv[row * n + col, 0] = p.p[row, col]
        pv_l.append(pv)

    # form matrix fm with column as vector fv(i,j)
    f_m = np.zeros((m * n, m * n))
    for i in range(0, m * n):
        # i as col of fm which indicate which positon of puzzle if flipped
        row = math.floor(i / n)
        col = i % n
        temp_p = puzzle(m, n)
        temp_p.perform_move(row, col)
        # put flipped matrix into vector
        for x in range(0, m):
            for y in range(0, n):
                f_m[x * n + y, i] = temp_p.p[x, y]
    step_s = 0
    time_s = 0.0
    for p in pv_l:
        start = time.clock()
        result, cost = GE(f_m, p, m, n)
        time_s += (time.clock() - start) * 1.0
        step_s += len(result)
    print("For GE: steps:%d cost:%d clock:%f" % (step_s, cost, time_s))












