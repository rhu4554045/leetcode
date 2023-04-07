import collections


def bfs(graph, node):
    visited = set()
    next_check = collections.deque(node)

    while next_check:
        vertex = next_check.popleft()
        if vertex not in visited:
            print(vertex, " ")
            visited.add(vertex)
            next_check.extend(set(graph[vertex]) - set(visited))


def dfs(graph, node):
    visited = set()
    next_check = collections.deque(node)

    while next_check:
        vertex = next_check.pop()
        if vertex not in visited:
            print(vertex, " ")
            visited.add(vertex)
            next_check.extend(set(graph[vertex]) - set(visited))


graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

node = 'A'

bfs(graph, node)
dfs(graph, node)
