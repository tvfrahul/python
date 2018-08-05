a=3
b=7
c=4
loop = [a,b,c]
def compare(x,y):
    if(x>y):
        return x
    else:
        return y

max1 = compare(a,b)
max2 = compare(max1,c)
if(max2 == a):
    print("largest number is a")
if(max2 == b):
    print("largest number is b")
if(max2 == c):
    print("largest number is c")



