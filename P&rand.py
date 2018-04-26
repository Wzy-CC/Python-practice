list_num = [0,1,2,3]
sum = 0
list_sum =[]
count_0 = 0
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
for num_01 in list_num:
    for num_02 in list_num:
        for num_03 in list_num:
            for num_04 in list_num:
                for num_05 in list_num:
                    sum = num_01 + num_02 + num_03 + num_04 + num_05
                    sum = sum%5
                    list_sum.append(sum)
for num in list_sum:
    if num == 0:
        count_0+=1
    if num == 1:
        count_1+=1
    if num == 2:
        count_2+=1
    if num == 3:
        count_3+=1
    if num == 4:
        count_4+=1
print("result0:",count_0)
print("result1:",count_1)
print("result2:",count_2)
print("result3:",count_3)
print("result4:",count_4)
