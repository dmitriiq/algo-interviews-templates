from typing import List, Tuple


def is_on_one_line(points: List[Tuple[int]]) -> bool:
    if len(points) < 3:
        return True

    if points[1][0] - points[0][0] != 0:
        leftmost = 0
        rightmost = 0
        for i in range(len(points)):
            if points[i][0] < points[leftmost][0]:
                leftmost = i
            if points[i][0] > points[rightmost][0]:
                rightmost = i

        # print('leftmost', leftmost, 'rightmost', rightmost)

        if points[rightmost][0] == points[leftmost][0]:
            return False
        a = (points[rightmost][1] - points[leftmost][1])/(points[rightmost][0] - points[leftmost][0])
        b = points[rightmost][1] - a * points[rightmost][0]

        # print(a, b)

        eps = 10e-16
        for (x,y) in points:
            if y - eps > a * x + b or y + eps < a * x + b:
                # print('y =', y - eps, 'ax + b =', a * x + b)
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