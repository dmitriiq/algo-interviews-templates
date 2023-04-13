from typing import List


def get_max_xor(numbers: List[int]) -> int:
    r = 0

    i = 0x80000000
    while i > 0:
        arr1 = []
        arr2 = []
        for n in numbers:
            if n & i > 0:
                arr1.append(n)
            else:
                arr2.append(n)
        # print(i, arr1, arr2)
        if len(arr1) > 0 and len(arr2) > 0:
            for a in arr1:
                for b in arr2:
                    r = max(r, a^b)
            i = 0
        i = i >> 1
    return r

n = int(input())
numbers = list(map(int, input().split()))
print(get_max_xor(numbers))