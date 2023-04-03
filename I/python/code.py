from node import Node

# Comment it before submitting
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

def Reverse(head: Node, left: int, right: int) -> Node:
    cnt = 0
    arr = []
    fakeHead = Node(0, head)
    it = fakeHead

    while it != None and cnt <= right:
        # print(head.value)
        if cnt >= left-1:
            arr.append(it)
            # print('arr: ', it.value)
        it = it.next
        cnt += 1

    # print('it: ', it.value)
    # print('arr[-1]: ', arr[-1].value)
    arr[0].next = arr[-1]
    for x in range(1, len(arr) - 1):
        arr[x+1].next = arr[x]
    arr[1].next = it

    return fakeHead.next
