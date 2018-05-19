import random

#200 student
list_student = []
for i in range(200):
    list_student.append(random.randint(0,100))

print(sorted(list_student))
def convert(_list):
    list_1to100 = range(0,101)
    for i in list_1to100:
        count = 0
        for j in range(0,200):
            if _list[j] == i:
                count +=1
        for k in range(0,200):
            if _list[k] == i:
                _list[k] -= count
    return _list
print('----------------------------------------------------------------')
convert(list_student)
print(sorted(list_student))               
