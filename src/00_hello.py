# Print "Hello, world!" to your terminal
print("Hello, world!")
print("Hello, " + "world!")

greeter = "Hello, world!"
print(greeter)

print(f'{greeter}')


p = [10, 60, 20, 5]
print(p)
p.append(77)
print(p)

for num in p:
     print(num)

squares = [num*num for num in p]
print(squares)

evens = [num for num in p if num % 2 == 0]
print(evens)