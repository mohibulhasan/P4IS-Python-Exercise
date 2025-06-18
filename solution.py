class Exe:
    def e3(a,b,n):
        sum=0
        for i in range(n):
            if (i%a==0 or i%b==0):
                sum+=i
        return print("The answer is:", sum)

    def e4(a,b,n):
        sum = 0
        for i in range(len(n)):
            if (n[i]%a==0 or n[i]%b==0):
                sum+=n[i]
        return print("The answer is:", sum)
    def e5(a,l):
        sum = 0
        for i in range(len(l)):
            for j in range(len(a)):
                if l[i]%a[j]==0:
                    sum+=l[i]
        return print("The answer is:", sum)

prompt = int(input("Which Exercise you want to try? 3,4 or 5:"))  

if prompt == 3:
    a=int(input("insert a: "))
    b=int(input("insert b: "))
    n=int(input("insert n: "))
    Exe.e3(a,b,n)
elif prompt == 4:
    a=int(input("insert number a: "))
    b=int(input("insert number b: "))
    arr=input("insert Array (e.g. 1,3,4,5,6,7,8,9,10): ")
    n = list(map(lambda num: int(num.strip()), arr.split(",")))
    Exe.e4(a,b,n)
elif prompt == 5:
    while True:
        arr1=input("insert an 2 digit Array (e.g. 1,3): ")
        a=list(map(lambda num: int(num.strip()), arr1.split(","))) #help of AI.
        #print (len(a))
        if len(a)!=2:
            print("only provide valid 2 digit array")
        else:
            break
    arr2=input("insert Array (e.g. 1,3,4,5,6,7,8,9,10...): ")
    l = list(map(lambda num: int(num.strip()), arr2.split(",")))
    Exe.e5(a,l)
else:
    print('You did not chose between 3 exercise!')