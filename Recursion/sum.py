# sum of numbers going from 0 to N

def sum(N):
    ''' exemple : sum(4) = 1+2+3+4 = 10
        sum(4) returns 10 '''
        
    if N == 0: # base case, could be 1
        return 0
        
    else:
        return sum(N-1) + N
        
        
print(sum(1))
print(sum(2))
print(sum(3))
print(sum(4))
print(sum(50))
