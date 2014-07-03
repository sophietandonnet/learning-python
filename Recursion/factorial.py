#
# Calculate factorial using recursion 
#

def factorial(N):
    ''' factorial(4) returns 24'''
    
    if N == 1:
        return 1
        
    else:
        return factorial(N-1) * N
        
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(50))
