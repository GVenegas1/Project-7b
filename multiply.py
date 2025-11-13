
# project-7b

# Author: Gabriel Venegas
# GitHub username: GVenegas1
# Date: 11/12/2025
#Description: This program defines a recursive program called multiply.
# The function does not use multiplication, Instead it uses addition
#recursion to find the result.

def multiply(a, b):
    """Recursively multiplies a and b using addition"""

    #Base, if 'b' equals 1 we simply return 'a' because a*1 = a
    if b == 1:
        return a

    #Recursive: a * b = a + (a * ( b - 1))
    #Add 'a' once then multiply again with 'b' minus 1
    return a + multiply(a, b - 1)

# Example Test Run
if __name__ == '__main__':
    num1=10
    num2=10
    result = multiply(num1, num2)
    print(result)