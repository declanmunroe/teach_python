def addTwoNumbers(x, y):
    return x + y
    
print (addTwoNumbers(5,3))

print (addTwoNumbers("5","3"))

def bigSmall(num):
    if num > 10:
        return "Big"
    else:
        return "Small"

print (bigSmall(11))

def are_same(x,y):
    return x == y
    
print (are_same(5,5))

def size(x,y):
    if x == y:
        return "Same"
    elif x > y:
        return "Bigger"
    else:
        return "Smaller"
        
print (size(5,5))
        
    