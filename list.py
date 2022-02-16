machines = ['tractors', 'bulldozer', 'refridgerator', 'bicycles']
print(machines)

print(machines[1])
print(machines[2].title())
print("The first machine in the list is", machines[0])

# modifying lists
machines[0] = "caterpillar"
print(machines)

machines.append("helicopter")
print(machines)

# removing elements from a list

del machines[1]
print(machines)

machines.sort()
print(machines)

machines.sort(reverse=True)
print(machines)

machines.reverse()
print(machines)

for mach in machines:
    print(mach)
    
for value in range(1, 5):
    print(value)

numbers = list(range(1, 5))
print(numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    print(squares)

print(squares)

digits = [1, 3, 5, 7, 9, 13, 15, 17, 19, 25]
print(max(digits))
print(min(digits))
print(sum(digits))

# list comprehension

val = [val**2 for val in range(1, 5)]
print(val)


