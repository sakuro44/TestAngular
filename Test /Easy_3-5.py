n = int(input("ใส่ตัวเลขที่ต้องการ : "))

if n % 2==0:
    k = int((n/2)+1)
    
    for i in range(1,n):
        if i % 2!=0:
            for x in range(1,k-1):
                print(' ',end='')
            for y in range(1,i+1):
                print('*',end='')    
            k = k-1
            print()

    for i in range(1,n):
        if i % 2!=0:
            for x in range(1,k):
                print(' ',end='')
            for y in range(1,n-i+1):
                print('*',end='')    
            k = k+1
            print()  
elif n % 2!=0:
    k = int((n/2)+1)
    for i in range(1,n):
        if i % 2==0:
            for x in range(1,k):
                print(' ',end='')
            for y in range(1,i):
                print('*',end='')    
            k = k-1
            print()

    
    for i in range(1,n+2):
        if i % 2==0:
            for x in range(1,k):
                print(' ',end='')
            for y in range(1,n-i+3):
                print('*',end='')    
            k = k+1
            print()