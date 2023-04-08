from typing import List, Tuple


def is_on_one_line(points: List[Tuple[int]]) -> bool:
    if len(points) < 3:
        return True

    if points[1][0] - points[0][0] != 0:
        a = (points[1][1] - points[0][1])/(points[1][0] - points[0][0])
        b = points[0][1] - a * points[0][0]

        # print(a, b)

        for (x,y) in points:
            if y != round(a * x + b):
                return False
        return True
    elif points[1][1] - points[0][1] != 0:
        for (x,y) in points:
            if x != points[0][0]:
                return False
        return True
    else:
        return is_on_one_line(points[1::])

n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

if is_on_one_line(points):
    print('YES')
else:
    print('NO')