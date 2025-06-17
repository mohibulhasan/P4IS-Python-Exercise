class Exe3:
    def sum():
        sum=0
        a=int(input("insert a: "))
        b=int(input("insert b: "))
        n=int(input("insert n: "))
        for i in range(n):
            if (i%a==0 or i%b==0):
                sum+=i
        return print("The answer is:", sum)

class Exe4:
    def sum():
        sum = 0
        a=int(input("insert number a: "))
        b=int(input("insert number b: "))
        arr=input("insert Array (e.g. 1,3,4,5,6,7,8,9,10): ")
        n = list(map(lambda num: int(num.strip()), arr.split(",")))

        for i in range(len(n)):
            if (n[i]%a==0 or n[i]%b==0):
                sum+=n[i]
        return print("The answer is:", sum)
    
Exe4.sum()