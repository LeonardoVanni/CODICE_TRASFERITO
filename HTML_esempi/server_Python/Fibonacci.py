def Fibonacci(n):
    """restituisce l'ennesimo valore della serie"""
    if n<0:
        return
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
