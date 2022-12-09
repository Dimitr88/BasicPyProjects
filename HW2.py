#Task 1
apples = int(input('Enter number of apples: '))
pupils = int(input('Enter number of pupils: '))
print(f'Number of apples for each pupil: {apples} / {pupils} = {apples // pupils}')
print(f'Number of apples in the backet: {apples} % {pupils} = {apples % pupils}')

#Task 2
first_class = int(input('Enter number of pupils for the first class: '))
second_class = int(input('Enter number of pupils for the second class: '))
third_class = int(input('Enter number of pupils for the third: '))
print(f'required number of school desks: ({first_class //2} + {first_class %2} = {first_class // 2 + first_class % 2})'
      f' + ({second_class //2} + {second_class %2} = {second_class // 2 + second_class % 2})'
      f' + ({third_class //2} + {third_class %2} = {third_class // 2 + third_class % 2})'
      f' = {first_class // 2 + first_class % 2 + second_class // 2 + second_class % 2 + third_class // 2 + third_class % 2}')

#Task 3
N = int(input('Enter integer: '))
print(type(int(f'{N%10}'
      f'{N//10%10}'
      f'{N//100}')),
      (int(f'{N % 10}'
            f'{N // 10 % 10}'
            f'{N // 100}'))
      )

#Task 4
N = int(input('Enter integer: '))
Hours = N//3600
S = N%3600
Minutes = S//60
Seconds = N%60
print(Hours,str(':'),Minutes,str(':'),Seconds)