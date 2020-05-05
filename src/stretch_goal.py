# Using Sieve of Eratosthenes algorithm
# logic for grabbing prime numbers starting at 2:

# problem break down:
'''
Find all prime numbers up to any given limit
Iterate over the list of numbers and mark the composite number (not prime number) by multiplying the number by itself.
Store the product and not the initial prime number
Store the initial prime number
While you are iterating over the list the composite number and prime number are placed in their respective list
Finally return the list with all the prime numbers up to the given limit
'''
def sieve():
    num = []
    num3 = []
    for x in range(2, 100):
        for i in range(2, 100):
            num2 = x * i
            if num2 not in num:
                num.append(num2)
    for x in range(2,100):
        if x not in num:
            num3.append(x)
    return num3

print(sieve())
#