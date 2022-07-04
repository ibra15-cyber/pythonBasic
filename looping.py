a = ['a', 'b', 'c']
b = [1, 2, 3]

# for index in a:
#     for index2 in b:
#         print(index ,'is' ,index2)

for index in a and b:
    print(a[index-1], 'is', b[index-1])

print("......................................")
for i, j in zip(a, b): #zip is the list a and b
    print("%s is %s" %(i, j))
 
