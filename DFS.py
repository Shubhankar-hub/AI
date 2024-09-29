def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()
    visited.add(start)
    print(start,end=' ')
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited) 

graph={
    'A':['B','C'],
    'B':['C','D'],
    'C':['F','G'],
    'D':['A','B'],
    'E':['H'],
    'F':['E','A'],
    'G':['A','H'],
    'H':[]
}

print("DFS TRAVERSAL")
dfs(graph,'A')