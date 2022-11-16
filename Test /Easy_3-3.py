def tree(n):
    for i in range(n):
        print(" "*(n-i-1)+"*",end="")
        if i>=1:
            print(" "*(2*i-1)+"* ",end="")
        print()

n = int(input("ใส่ตัวเลขที่ต้องการ : "))
tree(n)
 