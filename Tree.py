#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import queue
import sys
import math
import copy
from heapq import *
from puzzle import *
import time

class tree:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.head = node()
        #self.count = 1
        temp_p = puzzle(row, col)
        temp_p.random_created(row,col)
        #temp_p.scramble()
        self.head.p = temp_p
    def construct(self, level):
        count = [0]
        def tree_construct(n, level):
            if(level < 0):
                return
            #next puzzle
            row = math.floor(level / self.col)
            col = level % self.col
            #lchild not flip
            n.lchild = node(n.p, level, n.path, count[0])
            #rchild filp
            n.rchild = node(n.p, level, n.path, count[0] + 1)
            n.rchild.p.perform_move(row, col)
            n.rchild.path.append([row,col])
            count[0] += 1
            #print(n.rchild.count)
            #next level
            tree_construct(n.rchild, level - 1)
            tree_construct(n.lchild, level - 1)
            return
        return tree_construct(self.head, level)
    def bfs(self):
        q = queue.Queue(maxsize = 1000000000)
        #print(self.head.p.p)
        q.put(self.head)
        cost = 0
        step = 0
        path = []
        while(q.empty() != True):
            n = q.get()
            #print(n.p.p)
            if(n.p.is_solved() == True):
                cost = n.count
                step = len(n.path)
                path = copy.copy(n.path)
                #print(n.path)
                break
            if(n.lchild != -1):
                q.put(n.lchild)
            if(n.rchild != -1):
                q.put(n.rchild)
        return cost,step,path
    def dfs(self):
        find_flag = [0]
        cost = [0]
        step = [0]
        path = [0]
        def df_search(n):
            #global find_flag
            if(n == -1 or find_flag[0] == 1):
                return
            if(n.p.is_solved() == True):
                #print("%d cost:" % n.count)
                #print("%d steps:" % len(n.path))
                cost[0] = n.count
                step[0] = len(n.path)
                path[0] = copy.copy(n.path)
                #print(n.path)
                find_flag[0] = 1
                return
            df_search(n.lchild)
            df_search(n.rchild)
        return df_search(self.head),cost[0],step[0],path[0]
    def A_star(self):
        #f = h + g
        #h as the remained turn-on lights / 5
        #g as the length of path
        selected_node = []
        heappush(selected_node, self.head)
        selected_node.append(self.head)
        cost = 0
        step = 0
        path = []
        while(len(selected_node) != 0):
            n = heappop(selected_node)
            #print(len(selected_node))
            if(n.p.is_solved() == True):
                #print("%d cost:" % n.count)
                #print("%d steps:" % len(n.path))
                cost = n.count
                step = len(n.path)
                path = copy.copy(n.path)
                #print(n.path)
                break
            #put in r and l child
            if(n.rchild != -1):heappush(selected_node, n.rchild)
            if(n.lchild != -1):heappush(selected_node, n.lchild)
            #sort accoring to the h
            #selected_node.sort(key = lambda x:len(x.path) + n.p.p.sum()/5)

        return cost,step,path


class node:
    def __init__(self, p = puzzle(), level = - 1, path = [], count = 0):
        self.p = puzzle(p.row, p.col)
        self.p = copy.deepcopy(p)
        self.level = level
        self.path = copy.copy(path)
        self.count = count
        self.lchild = -1
        self.rchild = -1
    def __lt__(self , other):
        return len(self.path) + self.p.sum()/5 < len(other.path) + self.p.sum()/5







