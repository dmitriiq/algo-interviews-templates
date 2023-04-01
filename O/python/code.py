from typing import List

class Building:
    def __init__(self, need_capital, added_capital) -> None:
        self.need_capital = need_capital
        self.added_capital = added_capital

def get_max_final_capital(buildings: List[Building], start_capital: int, max_buildings: int) -> int:
    # your code goes here
    capital = start_capital
    buildings.sort(reverse=True, key=lambda b: b.need_capital)
    # print(buildings)

    sortedDict = dict()
    for b in buildings:
        if not sortedDict.__contains__(b.need_capital):
            sortedDict[b.need_capital] = []
        sortedDict[b.need_capital].append(b.added_capital)

    need_capitals = []
    for c in sortedDict:
        need_capitals.append(c)
        sortedDict[c].sort()

    it = 0
    while it < len(need_capitals):
        if need_capitals[it] > capital:
            it += 1
        else:
            break

    if it == len(need_capitals):
        return capital

    while max_buildings > 0:
        it2 = it
        max_it = it
        max_added = sortedDict[need_capitals[it2]][-1]
        # print('max_added', max_added)
        while it2 < len(need_capitals):
            # print('need_capitals[it2]', need_capitals[it2], sortedDict[need_capitals[it2]])
            if sortedDict[need_capitals[it2]][-1] > max_added:
                max_added = sortedDict[need_capitals[it2]][-1]
                max_it = it2
            it2 += 1
            # print('len', len(need_capitals), 'it2', it2)
        added_cap = max_added
        del sortedDict[need_capitals[max_it]][-1]
        if len(sortedDict[need_capitals[max_it]]) == 0:
            del sortedDict[need_capitals[max_it]]
            del need_capitals[max_it]
        capital += added_cap
        while it >= 0:
            if need_capitals[it] <= capital:
                it -= 1
            else:
                it += 1
                break
        if it < 0:
            it = 0
        max_buildings -= 1
    return capital

n, k = map(int, input().split())
buildings = []
for i in range(n):
    c, p = map(int, input().split())
    buildings.append(Building(c, p))
M = int(input())
print(get_max_final_capital(buildings, M, k))
