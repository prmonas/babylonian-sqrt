# Finds the square root through the babylonian method

# Steps:
#   1) Make initial guess: a
#   2) Set aux variable b=1 and the accuracy e=0.001
#   3) Improve the guess and iterate until convergence:
#      find the approximation using average of a and b
#      and set b=n/a

def bln_sqrt(n):  
        a = n 
        b = 1
        e = 0.001
        
        while(a - b > e):   
            a = (a + b)/2
            b = n / a 
      
return a 
