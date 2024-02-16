from math import log2, ceil
NEUTRAL_ELEMENT = 0
def build(arr):
    N = 2** ceil(log2(len(arr)))
    for _ in range(N - len(arr)):
        arr.append(NEUTRAL_ELEMENT)

    tree = [NEUTRAL_ELEMENT for i in range(2 * N)]



    for i in range(N):
        modify(tree, i, arr[i])
    return  tree
def modify(tree, i, d):
    while i < len(tree) // 2:
        tree[i] += d
        i = i  | (i+1)

def set_elem(tree, arr, i, d):
#    x = d - arr[i]
    arr[i] = d
    modify(tree, i, arr[i])
def query(tree, qlo, qhi):
    return _sum(tree, qhi) - _sum(tree, qlo - 1)
def _sum(tree, q):
    res = NEUTRAL_ELEMENT
    while q >= 0:
        res += tree[q]
        q = (q & (q +1)) - 1
    return  res



arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
print(f"Init arr: {arr}")
tree = build(arr)
print(f"Init tree: {tree}")
print(query(tree, 1, 2))
