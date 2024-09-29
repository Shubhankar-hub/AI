from collections import deque

def bfs(graph,start):
   visited=set()
   queue=deque([start])
   visited.add(start)
   while queue:
      vertex=queue.popleft()
      print(vertex,end=" ") 
      for neighbours in graph[vertex]:
         if neighbours not in visited:
            queue.append(neighbours)
            visited.add(neighbours)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['B', 'C'],
    'E': ['F'],
    'F': []
}

print("BFS traversal:")
bfs(graph, 'B')