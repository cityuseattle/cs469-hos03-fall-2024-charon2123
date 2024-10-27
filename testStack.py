from simpleStack import SimpleStack

# Create a stack
stack = SimpleStack()
stack.push_back(25)
stack.push_back(13)
stack.push_back(97)
stack.print_stack()

# Pop the last element
stack.pop()
print("After the pop operations")
stack.print_stack()

# Get the last element
print(f"The last element is {stack.peek()}")
stack.print_stack()