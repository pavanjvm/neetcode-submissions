import math


class Maths:
    def count_digits(self,n:int):
        count = 0
        while n>0:
            n=n//10
            count+=1
        return count

    def reverse_digits(self,n:int) -> int:
        rd:int=0
        while n>0:
           rd = rd * 10 + n%10
           n=n//10
        return rd


    def gcd(self,n1:int,n2:int)->int:
        if n1>n2:
            n1=n1%n2
        else:
            n2 = n2%n1

        if n1 == 0:
            return n2
        else:
            return n1

    def armstrong_number(self,n:int)->bool:
        s = 0
        k=n
        while n>0:

            s+=(n%10)**3

            n=n//10
        return k == s

    def all_divisors(self,n:int)->list[int]:
        factors:list[int]=[]
        for i in range(1,int(math.sqrt(n))+1):
            
            if n%i==0:
                factors.append(i)
                if n//i != i:
                    factors.append(n//i)
        factors.sort()
        return factors


    def prime_num(self,n:int) -> bool:
        count =0
    
        for i in range(1,int(math.sqrt(n))+1):
            if n%i == 0:
                count+=1
                if n//i != i:
                    count+=1
        return count == 2
