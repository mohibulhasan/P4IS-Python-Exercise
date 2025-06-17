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

Exe3.sum()