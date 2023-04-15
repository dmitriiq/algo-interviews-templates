from typing import List

def log(*args):
    #print(args)
    pass

def update_stack(c, stack):
    # log('c', c, stack)
    if c == '(':
        if '[' in stack:
            return False
        stack.append(c)
    elif c == '[':
        stack.append(c)
        # log(stack)
    elif c == ')':
        if len(stack) == 0:
            return False
        # log('stack[-1]', stack[-1])
        if stack[-1] != '(':
            return False
        del stack[-1]
        # log('stack', stack)
    elif c == ']':
        if len(stack) == 0:
            return False
        if stack[-1] != '[':
            return False
        del stack[-1]
        # log(stack)

    # log('update_stack True', stack)
    return True

def is_correct(s):

    # log('str', s)
    stack = []
    for c in s:
        if not update_stack(c, stack):
            return False

    # log('stack 1', stack)
    if len(stack) != 0:
        return False

    # log('True', s)
    return True


def add_brace(n: int, s, r, stack):
    braces = ['(', '[', ')', ']']

    if n == 0:
        # if is_correct(s):
        if len(stack) == 0:
            r.append(s)
        return

    for b in braces:
        sequnces = s + b
        copy_stack = stack.copy()
        if update_stack(b, stack):
            add_brace(n - 1, sequnces, r, stack)
        stack = copy_stack


def generate_sequences(n: int) -> List[str]:
    result = []

    # stack = []
    add_brace(n, '', result, [])
    # log(result)

    return result

n = int(input())
sequnces = generate_sequences(n)
for seq in sequnces:
    print(seq)
