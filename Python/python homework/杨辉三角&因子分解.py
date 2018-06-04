##    题目1：将一个正整数分解质因数。例如，输入90，打印出90=2*3*3*5。
##
##    题目2：请打印出如下的杨辉三角
##    1 
##    1     	1
##    1  	2     	1
##    1      	3      	3       1
##    1      	4      	6       4      	1
##    1      	5      	10     	10    	5      	1
##
##    给你一个正整数n，请你输出杨辉三角的前n层。
##    注意：层数从1开始计数,每层数字之间用空格或者Tab隔开，行尾不要有空格。如n=2,则输出： 
##    1 
##    1 	1

import math

def find_factor(_int):
    list_factor = []
    temp = _int
    sqrt_int = int(math.sqrt(_int))+1
    for fac in range(2,sqrt_int+1):
        while(temp % fac == 0):
            list_factor.append(fac)
            temp = temp / fac
    return list_factor

print(find_factor(90))

def print_triangle(_n):
    list_line = []
    for line in range(_n):
        list_line.append([])
        for col in range(line+1):
            if col == 0 or col == line:
                list_line[line].append(1)
            else:
                list_line[line].append(list_line[line-1][col]+list_line[line-1][col-1])
        print(list_line[line])
        
print_triangle(13)        

