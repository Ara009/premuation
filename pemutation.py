def solution (array,k):
    permuation = []
    index = 0
    while array:
        index = (index + k - 1) % len(array)
        item = array.pop(index)
        permuation.append(item)
    return permuation

soldier = 7
arr = [s+1 for s in range(soldier)]
k = 3
perm = solution(arr, k)
print(perm)

#deque double ended que

from collections import deque
def solution (array,k):
    permuation = []
    d = deque(array)

    while d:
        d.rotate(1-k)
        item = d.popleft()
        permuation.append(item)
    return permuation

soldier = 7
k = 3
arr = [s+1 for s in range(soldier)]

perm = solution(arr,k)

print(perm)




