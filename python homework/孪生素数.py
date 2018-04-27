#题目2：孪生素数（素数也叫质数）是一对相差2的素数，例如3和5，5和7，11和13都是孪生素数。请写一段代码找到所有1000以内的孪生素数，
#结果显示如下：
#（3，5）
#（5，7）
#……
#要求：
#（1）定义一个函数isPrime(num)，该函数判断给定数num是否是素数（或质数）；
#（2）要有文档字符串说明函数的功能。
import math
def isPrime(num):
    '函数判断是否为素数'
    sqrn = int(math.sqrt(num))+1
    for n in range(sqrn):
        if num!=3 and num%(n+2) == 0:
            return False
    return True

for i in range(1000):
    if isPrime(i+3) and isPrime(i+5):
        print(i+3,i+5)
    
         
    
    
        
        
