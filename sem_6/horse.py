import queue

n = 8
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

q = queue.Queue()
dist = [[-1] * n for i in range(n)]
dist[x1][y1] = 0
q.put((x1, y1))

while not q.empty():
    vx, vy = q.get()
    for dx, dy in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
        try:
            tx, ty = vx + dx, vy + dy
            if dist[tx][ty] == -1:
                q.put((tx, ty))
                dist[tx][ty] = dist[vx][vy] + 1
        except:
            pass
print(dist[x2][y2])
