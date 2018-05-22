#选择排序
def p(lst):
    smallest = lst[0]
    index = 0
    for i in range(len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
            index = i
    return index

def permutation(lst):
    lst_new = []
    for i in range(len(lst)):
        small = p(lst)
        lst_new.append(lst.pop(small))
        #pop(index)可选参数为列表索引！
    return lst_new

print(permutation([3,29,87,1,7]))

