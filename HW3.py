#Task 1
first_operand = int(input('Enter first integer: '))
operator = input('Enter operator: ')
second_operand = int(input('Enter second integer: '))

if operator == '/':
    print(f'result: {first_operand}/{second_operand} = {first_operand/second_operand}')
elif operator == '*':
    print(f'result: {first_operand}*{second_operand} = {first_operand*second_operand}')
elif operator == '+':
    print(f'result: {first_operand}+{second_operand} = {first_operand+second_operand}')
elif operator == '-':
    print(f'result: {first_operand}-{second_operand} = {first_operand-second_operand}')

#Task2
N = int(input('Enter integer: '))
for i in range (1,N+1):
    if i**2<= N:
        print(i**2,end = ' ')
print()
#Task3

Number = int(input('Enter: '))
for i in range(2, Number-1):
   if Number%i==0:
       print(Number, 'is not a prime')
       break
else:
    print(Number, 'is a prime')

#Task4 in progress, have no time


for i in range (heigh):
    print(' '*(heigh - i), '*', i*'**', sep='')
for i in reversed(range(heigh-2)):
    print((heigh - i - 1)*' ',  '*', int((i*2+1)/2)*' ','*',int((i*2+1)/2)*' ', '*', sep='')
print (heigh*' ', '*',sep='')