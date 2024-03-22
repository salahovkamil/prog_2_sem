# матрица граф
edge_list = [[0, 1], [0, 3],
             [1, 3],
             [2, 3],
             [4, 0], [4, 3],
             [5, 0]
             ]
vert_num = 6



'''edge_list = [[0, 1], [0, 2], [0, 3],
             [1, 2],  [1, 4], 
             [2, 4],  
             [3, 4],
             [4, 5], 
             [5, 3]
]
vert_num = 6'''



adj_list = [[] for _ in range(vert_num)]
for u, v in edge_list:
    adj_list[u].append(v)
adj_list


adj_matrix = [[0 for _ in range(vert_num)] for _ in range(vert_num)]

for edge in edge_list:
    u = edge[0]
    v = edge[1]
    adj_matrix[u][v] = 1

adj_matrix




# поиск в глубину

g = adj_list

parents = [None for _ in range(vert_num)]
colors = ["w" for _ in range(vert_num)]
timer = 0
tin = [None for _ in range(vert_num)]
tout = [None for _ in range(vert_num)]


def dfs(v, p=-1):
    global timer
    parents[v] = p
    colors[v] = "g"
    timer += 1
    tin[v] = timer
    for u in g[v]:
        if colors[u] == "g":
            print(f"found cycle {v} -> {u}")
            continue
        elif colors[u] == "b":
            continue
        elif colors[u] == "w":
            dfs(u, v)
    colors[v] = "b"
    timer += 1
    tout[v] = timer


dfs(4)
# print(tin)
# print(colors)
print("Exit_timer:", tout)



# Топологическая сортировка (перестановка вершин графа, такая что ребра ведут слева направо)
g = adj_list
parents = [None for _ in range(vert_num)]
colors = ["w" for _ in range(vert_num)]
timer = 0
tin = [None for _ in range(vert_num)]
tout = [None for _ in range(vert_num)]


def top_sort():
    for v in range(vert_num):
        if colors[v] == "w":
            dfs(v)
    vert_list = [i for i in range(vert_num)]
    ans = [
        x for y, x in sorted(zip(tout, vert_list), key=lambda pair: pair[0], reverse=True)
    ]
    return ans


top_sort()


# Количество путей из вершины=
ts = top_sort()
path = []
path_finish = []

for i in range(len(ts)):
    path.append(1)

for i in range(len(ts) - 2, -1, -1):
    f = ts[i]
    arr = adj_list[f]
    for y in range(0, len(arr)):
        u = arr[y]
        ind = ts.index(u)
        znach = path[i] + path[ind]
        path[i] = znach

for i in range(0, len(ts)):
    inde = ts.index(i)
    path_finish.append(path[inde])

print(path_finish)

