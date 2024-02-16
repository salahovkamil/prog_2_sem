from math import log2, ceil
NEUTRAL_ELEMENT = 0
def build(arr):
    N = 2** ceil(log2(len(arr)))
    for _ in range(N - len(arr)):
        arr.append(NEUTRAL_ELEMENT)

    tree = [NEUTRAL_ELEMENT for i in range(2 * N)]
    for i in range(0, N):
        tree[N - 1 + i] = arr[i]
    for i in range(N - 2, -1, -1):
        tree[i] = tree[2 * i + 1] + tree[2 * i +2]
    return tree
def _query(tree, qlo, qhi, lo, hi, pos):
    if no_overlap(qlo, qhi, lo, hi):
        return NEUTRAL_ELEMENT

    if total_overlap(qlo, qhi, lo, hi):
        return  tree[pos]
    mid = (lo + hi) // 2
    return _query(tree, qlo, qhi, lo, mid, 2 * pos + 1) + _query(tree, qlo, qhi,  mid, hi, 2 * pos + 2)
def query(tree, qlo, qhi):
    return _query(tree, qlo, qhi,0,len(tree) // 2,0)
def no_overlap(qlo,qhi,lo,hi):
    return  qlo >= hi or qhi <= lo
def total_overlap(qlo, qhi, lo, hi):
    return qlo <= lo and hi <= qhi

arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
print(f"Init arr: {arr}")
tree = build(arr)
print(f"Init tree: {tree}")
print(query(tree, 3, 6))
