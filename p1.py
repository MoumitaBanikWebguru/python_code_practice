# print("hello world")
# print("hello")

list1 = [1, 2, 2, 3, 4, 3, 5, 1]
# new_list = list(set(list1))
new_list = []
for l in list1:
    if l not in new_list:
        new_list.append(l)
print(new_list)