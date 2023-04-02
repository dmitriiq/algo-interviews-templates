from typing import List

class Building:
    def __init__(self, need_capital, added_capital) -> None:
        self.need_capital = need_capital
        self.added_capital = added_capital

def get_max_final_capital(buildings: List[Building], start_capital: int, max_buildings: int) -> int:
    # your code goes here
    capital = start_capital
    # sorted_need = [e for e in range(len(buildings))]
    buildings.sort(reverse=False, key=lambda b: b.need_capital)

    # sortedDict = dict()
    added_capital = []
    i = 0
    unsorted = False
    while max_buildings > 0:
        if i < len(buildings) and buildings[i].need_capital <= capital:
            # print('added_capital', added_capital, 'b.added_capital', b.added_capital)
            added_capital.append(buildings[i].added_capital)
            i += 1
            unsorted = True
        else:
            if unsorted:
                added_capital.sort()
                unsorted = False
            # print('added_capital sorted', added_capital)
            if len(added_capital) > 0:
                capital += added_capital.pop()
                max_buildings -= 1
            else:
                break

    return capital

n, k = map(int, input().split())
buildings = []
for i in range(n):
    c, p = map(int, input().split())
    buildings.append(Building(c, p))
M = int(input())
print(get_max_final_capital(buildings, M, k))
