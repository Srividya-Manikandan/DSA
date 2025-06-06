# Function to return precedence of operators
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

# Function to perform infix to postfix conversion
def infix_to_postfix(expression):
    stack = []  # Initialize an empty stack
    output = []  # Initialize an empty output list

    for char in expression:
        # If the character is an operand, add it to output
        if char.isalnum():  # Check if character is operand
            output.append(char)

        # If the character is '(', push it to stack
        elif char == '(':
            stack.append(char)

        # If the character is ')', pop and output from the stack
        # until an '(' is encountered
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Discard the '(' from the stack

        # An operator is encountered
        else:
            while (stack and precedence(stack[-1]) >= precedence(char)):
                output.append(stack.pop())
            stack.append(char)

    # Pop all the operators from the stack
    while stack:
        output.append(stack.pop())

    return ''.join(output)

# Example usage
infix_expr = "a+b*(c^d-e)^(f+g*h)-i"
postfix_expr = infix_to_postfix(infix_expr)
print("Infix Expression:", infix_expr)
print("Postfix Expression:", postfix_expr)
