class Patterns:
    def pattern1(self,n: int):
        for _ in range(n):
            for _ in range(n):
                print("*",end=" ")
            print()

    def pattern2(self,n:int):
        for i in range(n):
            for j in range(n-i-1,n):
                print("*",end= " ")
            print()

    def pattern3(self,n:int):
        for i in range(n):
            k=1
            for _ in range(n-i-1,n):
                print(k,end= " ")
                k+=1
            print()

    def pattern4(self,n:int):
        for i in range(n):
            for _ in range(n-i-1,n):
                print(i+1,end= " ")
            print()

    def pattern5(self,n:int):
        for i in range(n):
            for _ in range(i,n):
                print("*",end= " ")
            print()

    def pattern6(self,n:int):
        for i in range(n):
            k=1
            for _ in range(i,n):
                print(k,end= " ")
                k+=1
            print()


    def pattern7(self,n:int):
        for i in range(n):
            for _ in range(i,n):
                print(" ",end= " ")

            for j in range((i*2)+1):
                print("*", end=" ")
            print()

    def pattern8(self,n:int):
        for i in range(n):
            for _ in range(n-i-1,n):
                print("",end="")

            for _ in range(1,(n-i)*2):
                print("*",end=" ")
            print()

   

    def pattern10(self,n:int):
        for i in range((2*n)):
            if i < n :
                stars=i
                print((stars+1)*"*",end=" ")
            else:
                print((2*n-i)*"*",end=" ")
            print()
            
            
                
                
            
        
        
            
    