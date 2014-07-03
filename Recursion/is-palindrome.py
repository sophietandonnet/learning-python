# Script to know if a string is a palindrome, using recursion
#
#
#

def is_palindrome(s):
    ''' exemples:
    is_palindrome('p') returns True
    is_palindrome('pop') returns True
    is_palindrome('piop') returns False
    is_palindrome('piip') returns True '''
    
    length = len(s)
    
    if length == 1:
        return True
        
    if length == 2 and s[0] == s[1]:
        return True
        
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
            
        else:
            return False
            
print(is_palindrome("p"))
print(is_palindrome("anna"))
print(is_palindrome("pop"))
print(is_palindrome("piop"))
print(is_palindrome("racecar"))
print(is_palindrome("socorram me subino onibus em marrocos"))


