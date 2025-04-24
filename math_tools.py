def add(a, b):
    
   # Returns the sum of a and b.
  
    return a + b

def subtract(a, b):

    #Returns the difference between a and b (a - b).
    
    return a - b

def multiply(a, b):
    
    #Returns the product of a and b.
    
    return a * b

def divide(a, b):

    #Returns the quotient of a divided by b.

    #If b is zero, returns 'Undefined' to avoid division by zero.
    
    if b == 0:
        return "Undefined"
    return a / b
