#题目1：请编写一段代码，其中至少包含以下两个函数，
# 将摄氏度转换成华氏度
#def celsiusToFahrenhei(celsius):
# 将华氏度转换成摄氏度
#def fahrenheitToCelsius(fahrenheit):
#其中涉及到的转换公式如下：
#celsius = (5/9) * (fahrenheit-32)
#fahrenheit = (9/5) * celsius + 32
#然后写一段代码调用以上两个函数并显示如下信息：
#Celsius       Fahrenheit   |    Fahrenheit          Celsius
#40.0            104.0           |    120.0                   48.89 
#39.0             102.2          |     110.0                  43.33
#……             ………        |  . ………..               …………
#31.0              87.8           |     30.0                    -1.11 
list_Celsius_1 = range(40,32,-1)
list_Fahrenheit_2 = range(120,20,-10)
def celsiusToFahrenhei(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit
def fahrenheitToCelsius(fahrenheit):
    celsius = (5/9) * (fahrenheit-32)
    return celsius
print('Celsius       Fahrenheit   |    Fahrenheit          Celsius')
for C in list_Celsius_1:
    print(C,celsiusToFahrenhei(C))
for F in list_Fahrenheit_2:
    print(F,fahrenheitToCelsius(F))
