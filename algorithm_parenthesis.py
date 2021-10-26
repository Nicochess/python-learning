def balanced(expression):
    unBalanced = False
    count = 0

    for char in expression:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1

    if count > 0:
        return unBalanced
    elif count == 0:
        for char in expression[::-1]:
            if char == "(":
                return False
            elif char == ")":
                return True
    else:
        return unBalanced