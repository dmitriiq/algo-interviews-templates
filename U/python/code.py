from typing import List



def is_correct(s: str, complete: bool):
    stack = []

    # print('str', str)
    for c in s:
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

    if complete and len(stack) != 0:
        return False
    
    # print('True', str)
    return True


def add_brace(n: int, s, r):
    braces = ['(', '[', ')', ']']

    if n == 0:
        if is_correct(s, True):
            r.append(s)
        return

    for b in braces:
        sequnces = s + b
        if is_correct(sequnces, False):
            add_brace(n - 1, sequnces, r)


def generate_sequences(n: int) -> List[str]:
    result = []

    add_brace(n, '', result)
    # print(result)

    return result

n = int(input())
sequnces = generate_sequences(n)
for seq in sequnces:
    print(seq)
