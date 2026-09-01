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
            
    

           
           
           