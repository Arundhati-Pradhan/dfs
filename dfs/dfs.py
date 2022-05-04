from turtle import color


adjacent_list = {
    'A' :['B','C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

color = {}
parent = {}
trav_t = {}
dfs_traversal = []

for node in adjacent_list.keys():
    color [node] = "W"
    parent[node] = None
    trav_t[node] = [-1,-1]

time = 0
def dfs(u):
    global time
    color[u]="G"
    trav_t[u][0] = time
    dfs_traversal.append(u)

    for v in adjacent_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs(v)
    color[u] = "B"
    trav_t[u][1] = time
    time += 1

dfs("A")
print(dfs_traversal)

