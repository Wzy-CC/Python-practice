## 一个机器人在平面中移动，起始点位于（0，0）的位置。此机器人可以向上、下、左、
## 右以一定的步长移动，其移动的信息通常用以下形式表述：
##  UP 5               #  即方向+步长
##  DOWN 3
##  LEFT 3
##  RIGHT 2
##
## 请编写一个程序，计算出经过一系列移动步骤后，机器人目前距离起始点的距离
##（用整数表示）。例如经过上述4个步骤后，程序应该返回2。

import math
def move(_up,_down,_left,_right):
    distance = math.sqrt(pow(abs(up-down),2)+pow(abs(left-right),2))
    return int(distance)

(up,down,left,right) = eval(input('please input 4 vector:'))
print(move(up,down,left,right))
