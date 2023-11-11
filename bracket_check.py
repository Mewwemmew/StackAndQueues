from Stack import Stack

#input: str
#output: is_error : boolean
#output: location: int

def bracket_check(str):
    is_error = False
    location = []
    stack = Stack()

    for i in range(len(str)):
        s = str[i]
        if s == "(" or s == "[" or s == "{":
            stack.push(s)
        elif s == ")" or s == "]" or s == "}":
            if not stack.isEmpty():
                p = stack.pop()
            else:
                p = ""
            location.append(i)
            if(not ((p == "(" and s == ")") or (p == "[" and s == "]") or (p == "{" and s == "}"))) :
                is_error = True
            else:
                location.pop()


    if not stack.isEmpty():
        is_error = True
        location.append(len(str)-1)

    return is_error, location

