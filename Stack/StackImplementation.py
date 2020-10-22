
#  A stack is an abstract data structure. It is just like a pile of plates.
# You can add a new plate or remove a plate
# If you want to get to the last last plate you have to remove all the plates on top 
# of it first

# Adding a new item on the stack is called a push. To push you first have to check if the stack is not
# full

# Removing an item from the stack is called a pop. To pop you have to check if the stack is empty

# Looking at the top item without removing it is called peeking



def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)

def peek(stack):
    return stack[len(stack) - 1]

def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"
    
    return stack.pop()


stack = create_stack()

push(stack, str(5))
push(stack, str(59))
push(stack, str(12))
push(stack, str(88))

print("Popped item: " + pop(stack))
print("Stack after popping: " + str(stack))
print("Peeking top item: " + peek(stack))
print("Stack after peeking: " + str(stack))

print(stack)

