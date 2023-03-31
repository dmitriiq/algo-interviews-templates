from typing import List
from sortedcontainers import SortedDict
from sortedcontainers import SortedList

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
            sortedDict[b.need_capital] = SortedList()
        for k in sortedDict:
            if k >= b.need_capital:
                sortedDict[k].add(b.added_capital)
            # else:
            #     break
            # print('k, v: ', k, sortedDict[k])

            # b.added_capital
            # print('need_capital', b.need_capital, 'added', b.added_capital)

    print(sortedDict)

    while max_buildings > 0:
        # print(max_buildings)
        i = 0
        for b in buildings:
            # print('list: ', b.need_capital, i)
            
            if capital >= b.need_capital:
                capital += b.added_capital
                # print('capital', capital)
                del buildings[i]
                found = True
                break
            i += 1

        max_buildings -= 1


    return capital

n, k = map(int, input().split())
buildings = []
for i in range(n):
    c, p = map(int, input().split())
    buildings.append(Building(c, p))
M = int(input())
print(get_max_final_capital(buildings, M, k))
