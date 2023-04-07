import pandas as pd
from pytrends.request import TrendReq
import time
import numpy as np
import datetime


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

if __name__ == "__main__":
    graph = {'A': (['B', 'C']),
             'B': (['A', 'D', 'E']),
             'C': (['A', 'F']),
             'D': (['B']),
             'E': (['B', 'F']),
             'F': (['C', 'E'])}

    dfs(graph, 'A')  # {'E', 'D', 'F', 'A', 'C', 'B'}

    list(dfs_paths(graph, 'C', 'F'))  # [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]
