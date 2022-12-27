#Task1
my_string = '0123456789'
result = []

for symbol_1 in my_string:
    for symbol_2 in my_string:
        result.append(int(symbol_1 + symbol_2))

print(result)

#Task2

height = int(input('Enter height: '))

for i in range (height):
    print(' '*(height - i), '*', i*'**', sep='')

for i in range (height):
    print(' ' * (height - i), '*', i*' *', sep='')