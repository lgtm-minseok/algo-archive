n = int(input())

# Please write your code here.

def a(n):
    print("HelloWorld")
    if n <=1:
        return
    
    n-=1
    return a(n)

a(n)