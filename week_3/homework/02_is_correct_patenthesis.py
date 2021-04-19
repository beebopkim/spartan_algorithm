s = "(()))()"


def is_correct_parenthesis(string):
    paren_stack = []
    param_stack = []
    for i in range(len(string)):
        param_stack.append(string[i])

    for i in range(len(string)):
        c = param_stack.pop(0)
        if c == "(":
            paren_stack.append("(")
        elif c == ")":
            if len(paren_stack) == 0:
                return False
            paren_stack.pop()

    if len(param_stack) == 0 and len(paren_stack) == 0:
        return True
    else:
        return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!