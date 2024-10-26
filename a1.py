def factorial(n):
    product=1
    for i in range(1,n+1):
        product=product*i
    print("The factorial of number" , n ,"is : ", product)
factorial(5)
