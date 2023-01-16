spisok = [{"name": "Yana", "age": 34}, {"name": "Dmytro", "age": 36},{"name": "Greg", "age": 23},
          {"name": "Irina", "age": 56}, {"name": "Alex", "age": 16}, {"name": "Yura", "age": 16}]
age_min = spisok[0]["age"]
name = [spisok[0]["name"]]
for i in spisok:
    if i["age"] < age_min:
        age_min = i["age"]
        name = [i["name"]]
    elif i["age"] == age_min:
        name.append(i["name"])
        print(age_min, name)
#Task2
my_dict_1 = {1:1, 2:2, 3:3}
my_dict_2 = {11:11, 2:22}
res1 = dict((key, my_dict_1[key])
for key in my_dict_1 if key not in my_dict_2)
print(res1)

res2 = dict((item[0], item[1]
if item[0] not in my_dict_2
else [item[1], my_dict_2[item[0]]])
for item in my_dict_1.items())
print(res2)