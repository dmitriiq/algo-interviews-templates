from typing import List



def is_correct(str):
    stack = []

    # print('str', str)
    for c in str:
        # print('c', c, stack)
        if c == '(':
            if '[' in stack:
                return False
            stack.append(c)
        elif c == '[':
            stack.append(c)
            # print(stack)
        elif c == ')':
            if len(stack) == 0:
                return False
            # print('stack[-1]', stack[-1])
            if stack[-1] != '(':
                return False
            stack = stack[:-1]
            # print('stack', stack)
        elif c == ']':
            if len(stack) == 0:
                return False
            if stack[-1] != '[':
                return False
            stack = stack[:-1]
            # print(stack)

    if len(stack) != 0:
        return False
    
    # print('True', str)
    return True


def add_brace(n: int, s, r):
    braces = ['(', '[', ')', ']']

    if n == 0:
        if is_correct(s):
            r.append(s)
        return

    for b in braces:
        add_brace(n - 1, s + b, r)


def generate_sequences(n: int) -> List[str]:
    result = []

    add_brace(n, '', result)
    # print(result)

    return result

n = int(input())
sequnces = generate_sequences(n)
for seq in sequnces:
    print(seq)
