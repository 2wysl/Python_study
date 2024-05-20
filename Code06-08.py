#스택이 꽉 찼는지 확인하는 함수#

def isStackFull() :
    global SIZE, stack, top
    if (top>= SIZE-1) :
        return True
    else :
        return False
    
def isStackEmpty() :
    global SIZE, stack, top
    if (top == -1) :
        return True
    else :
        return False

def push(data) :
    global SIZE, stack, top
    if (isStackFull()) :
        print("스택이 꽉 찼습니다.")
        return 
    top += 1 
    stack[top] = data

def pop() :
    global SIZE, stack, top
    if (isStackEmpty()) : 
        print("스택이 비었습니다.")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1 
    return data

def peek() :
    global SIZE, stack, top
    if (isStackEmpty()) : 
        print("스택이 비었습니다.")
        return None
    return stack[top]


