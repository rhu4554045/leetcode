import numpy as np
import collections
import itertools


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    visited_lst = []
    island = 0
    lst_len = len(visited_lst)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            visited_lst = dfs(grid, visited_lst, [(row, col)])
            if len(visited_lst) > lst_len:
                island += 1
                lst_len = len(visited_lst)

    return island


def is_valid(grid, node_p):
    return True if (0 <= node_p[0] <= len(grid)-1) and (0 <= node_p[1] <= len(grid[0]) -1) and (
            grid[node_p[0]][node_p[1]] == "1") else False


def dfs(grid, visit_lst, node):
    num_q = collections.deque(node)
    position_comb = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    while num_q:
        vertex = num_q.pop()
        if vertex not in visit_lst and is_valid(grid, vertex):
            visit_lst.append(vertex)
            for pos in position_comb:
                near_node = (vertex[0] + pos[0], vertex[1] + pos[1])
                if is_valid(grid, near_node):
                    num_q.append(near_node)

    return visit_lst

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

node= [(3,3)]
visit_lst = []

print(numIslands(grid))
