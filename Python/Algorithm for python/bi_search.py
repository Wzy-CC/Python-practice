def binary_search(_list,_element):#list有序,返回值为索引
    low = 0
    high = len(_list)-1

    while low!=high:
        mid = int((low+high)/2)
        if _list[mid] == _element:
            return mid
        if _list[mid] < _element:
            low = mid+1
        else:
            high = mid-1
    return None    



print(binary_search([1,3,4,7,8,9,10,30,45,80],45))

