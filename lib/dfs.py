
def dfs(G):
    global time
    for u in G.V:
        u.color == "white"
        u.pi = None
    time = 0
    for u in G.V:
        if u.color == "white":
            dfs_visit(G, u)
    
def dfs_visit(G, u):
    global time
    time += 1
    u.d = time
    u.color = "gray"
    for v in G.Adj[u]:
        if v.color == "white":
            v.pi = u
            dfs_visit(G, v)
    u.color = "black"
    time += 1
    u.f = time

