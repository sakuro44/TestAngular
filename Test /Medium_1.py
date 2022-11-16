def main():
    n = int(input("ใส่ตัวเลขที่ต้องการ : "))
    print("ตัวเลขเฉพาะของ",n,"คือ : ")
    for i in range(n+1):
        if isPrime(i):
            print(i, end = ' ')
 
def isPrime(num):
    if num < 2:
        return False
    for k in range(2, num):
        if num % k == 0:
            return False
    return True
 
main()
