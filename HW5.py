my_list = [23,43,66, 1, 3324 ,471,125,794,22,243]
my_result = []
#Task1
for i in my_list:
    if i >= 100:
        print(i, end=' ')
print()

#Task2
for n in my_list:
    if n > 100:
        my_result.append(n)
for n in my_result:
    print(n, end=' ')
print()
#Task3

if len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
else:
    my_list.append(0)

print(my_list)
print(sum(my_list[-2:]))