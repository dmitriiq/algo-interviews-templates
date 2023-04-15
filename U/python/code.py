from typing import List

def log(*args):
    #print(args)
    pass

def check_symbol(c, stack):
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


def add_brace(n: int, s, r, stack):
    braces = ['(', '[', ')', ']']

    if n == 0:
        if len(stack) == 0:
            r.append(s)
        return

    for b in braces:
        sequnces = s + b
        copy_stack = stack.copy()
        if check_symbol(b, stack):
            add_brace(n - 1, sequnces, r, stack)
        stack = copy_stack


def generate_sequences(n: int) -> List[str]:
    result = []
    add_brace(n, '', result, [])
    return result

n = int(input())
sequnces = generate_sequences(n)
for seq in sequnces:
    print(seq)
