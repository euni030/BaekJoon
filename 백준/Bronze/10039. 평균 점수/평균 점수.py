total=0

for i in range(5):
    x=int(input())
    
    if x<40:
        total+=40
    else:
        total+=x

print(total//5)