#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Tree import *

if __name__ == "__main__":
    m = 4
    n = 4
    print("For Problem 4.4")
    T = tree(m, n)
    T.construct(m * n - 1)
    print("Construct completed")
    print("----bfs begin------")
    print(T.bfs())
    #print("----bfs end--------")
    print("----dfs begin------")
    print(T.dfs())
    #print("-----dfs end-------")
    print("----A_star begin---")
    print(T.A_star())
    #print("----A_star end-----")
