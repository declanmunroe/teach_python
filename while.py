x = 0
total = 0

while x <= 6:
    x = x + 1
    total = total + x
    
print(total)

x = 0
total = 0

while x <= 10:
    x = x + 1
    total = total + x

print(total)

    
def sumnums(n):
    x = 0
    total = 0
    while x <= n:
        x = x + 1
        total = total + x
    return total

print(sumnums(10))

def contains(x,y,n):
    result = False
    while x <= y:
        if x == n:
            result = True
        x = x + 1
    return result
            
print(contains(1,10,0))
        
        
        