def is_balanced(expr):
    list=[]

    for char in expr:
        if char in ["(","{","["]:
            list.append(char)
        else:
            if not list:
                return False

            current_char=list.pop()
            if current_char=='(':
                if char!=')':
                    return False
            if current_char=='{':
                if char!='}':
                    return False
            if current_char=='[':
                if char!=']':
                    return False

    if list:
        return False
    else:
        return True


print(is_balanced('[]'))


