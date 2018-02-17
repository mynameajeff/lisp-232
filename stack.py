
stack = []


def empty():
    global stack

    stack = []


def stringify(gpt_return):
    global stack

    for item in gpt_return:

        if isinstance(item, float):

            if item.is_integer():
                stack.append(str(int(item)))

            else:
                stack.append(str(item))

        elif isinstance(item, str):
            stack.append(item)

        elif isinstance(item, tuple):

            stack.append("(")
            stringify(item)
            stack.append(")")
    
    return ' '.join(stack)  \
        .replace("( ", "(") \
        .replace(" )", ")")


def gpt(match):

    tree = []

    for x in range(2):

        tval = match[x + 1]

        if isinstance(tval, float):
            tree.append(tval)

        else:
            tree.append(gpt(tval))

    tree.insert(1, match[0])

    # print(tree)

    return tuple(tree)
