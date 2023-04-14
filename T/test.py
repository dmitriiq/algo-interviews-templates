from typing import List

def get_max_xor(numbers: List[int]) -> int:
    r = 0

    i = 0
    while i < len(numbers):
        j = i + 1
        while j < len(numbers):
            # print(numbers[i] ^ numbers[j])
            r = max(r, numbers[i] ^ numbers[j])
            j += 1
        i += 1
    return r


n = int(input())
numbers = list(map(int, input().split()))
print(get_max_xor(numbers))
