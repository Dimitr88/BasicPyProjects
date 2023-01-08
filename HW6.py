#Task1
my_list_1 = ['There', 'is', 'a', 'house', 'in', 'New', 'Orleans']
my_list_2 = ['they', 'call', 'the', 'Rising', 'Sun', '333']

result = my_list_1[::2] + my_list_2[1::2]
print(result)

#Task2
my_str = 'Merry Christmas and Happy New Year to everybody'
result=[]
for i in my_str:
    if my_str.count(i)==1:
        result.append(i)
print(result)