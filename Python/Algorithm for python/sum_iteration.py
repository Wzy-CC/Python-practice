def sum_iteration(_list):
    if _list == []:
        return 0
    else:
        num = _list.pop(0)
        return num + sum_iteration(_list)
    
print(sum_iteration([11,4,3,1,40]))
