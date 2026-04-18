l=[12,3,46,74,82,47,79,74,211,433,53,64,7,69,8,9,67,5,636]

# print(l[0])

# for index in range(len(l)):
#     if l[index] > 10:
#         print(l[index])

# for element in l:
#     if element>10:
#         print (element)

for i, element in enumerate(l):
    if element > 10:
        print(i, element)