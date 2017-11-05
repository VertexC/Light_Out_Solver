#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import queue
import sys
import math
import copy
from heapq import *
import time

class puzzle:
    # create a puzzle with 0 value
    def __init__(self, row = 0, col = 0):
        self.row = row
        self.col = col
        self.p = np.zeros((row, col))
    # same as init
    def create_p(self, row, col):
        self.row = row
        self.col = col
        self.p = np.zeros((row, col))
    # perform turn-on on specific position
    def perform_move(self, row, col):
        m,n = self.p.shape
        self.p[row, col] = (self.p[row, col] + 1)%2
        if (row + 1 < m):
            self.p[row + 1, col] = (self.p[row + 1, col] + 1) % 2
        if (row - 1 >= 0):
            self.p[row - 1, col] = (self.p[row - 1, col] + 1) % 2
        if (col + 1 < n):
            self.p[row, col + 1] = (self.p[row, col + 1] + 1) % 2
        if (col - 1 >= 0):
            self.p[row, col - 1] = (self.p[row, col - 1] + 1) % 2
    # scramble all the light(use random_created() for random)
    def scramble(self):
        m, n = self.p.shape
        for i in range(0, m):
            for j in range(0,n):
                self.perform_move(i, j)
    # return Ture if every entry in matrix is zero
    def is_solved(self):
        return (self.p == 0).all()
    # randomly generated a matrix with 0 or 1
    def random_created(self, row, col):
        r = np.random.random((row,col))
        for i in range(0, row):
            for j in range(0, col):
                if(r[i][j] >= 0.5):
                    self.perform_move(i, j)
    # return the sum of every entry in the matrix
    def sum(self):
        return self.p.sum()

