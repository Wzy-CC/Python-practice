#编写一个函数converter()，给出一个整型值, 返回代表该值的英文, 比如输入 89 返回 “eighty-nine”。
#注意：（1）本练习中的输入整型值限定在[0，2000]。
#      （2）对可能出现异常的地方，根据需要使用try/except/else/finally来捕捉与处理异常。
zero_dict = {0:'zero'}
ones_dict = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:''}
ten_plus_dict = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
tens_dict = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety',0:''}
hundreds_dict = {1:'onehundreds',2:'twohundreds',3:'threehundreds',4:'fourhundreds',5:'fivehundreds',6:'sixhundreds',7:'sevenhundreds',8:'eighthundreds',9:'ninehundreds',0:''}
thousands_dict = {1:'onethousands',2:'twothousands'}
def converter(_int):
    
    list_int = []
    i = len(_int)
    _int = int(_int)
    chr_int = ''

    #拆解为'个''十''百''千'位:
    for j in range(i):
        list_int.append(_int%10) 
        _int = (_int-list_int[j])/10

    if i==1:
        if list_int[0] == 0:
            ones_chr = zero_dict[list_int[0]]
        else:
            ones_chr = ones_dict[list_int[0]]
        tens_chr = huns_chr = thos_chr = ''
        
    if i==2:
        if list_int[1] == 1:
            ten_plus = list_int[0] + list_int[1] * 10
            ones_chr = ten_plus_dict[ten_plus]
            tens_chr =''
        else:
            ones_chr = ones_dict[list_int[0]]
            tens_chr = tens_dict[list_int[1]]
        huns_chr = thos_chr = ''
        
    if i==3:
        if list_int[1] == 1:
            ten_plus = list_int[0] + list_int[1] * 10
            ones_chr = ten_plus_dict[ten_plus]
            tens_chr =''
        else:
            ones_chr = ones_dict[list_int[0]]
            tens_chr = tens_dict[list_int[1]]
        huns_chr = hundreds_dict[list_int[2]]
        thos_chr = ''
        
    if i==4:
        if list_int[1] == 1:
            ten_plus = list_int[0] + list_int[1] * 10
            ones_chr = ten_plus_dict[ten_plus]
            tens_chr =''
        else:
            ones_chr = ones_dict[list_int[0]]
            tens_chr = tens_dict[list_int[1]]

        huns_chr = hundreds_dict[list_int[2]]
        thos_chr = thousands_dict[list_int[3]]+'-'
    if (thos_chr or huns_chr )and (tens_chr or ones_chr):
        chr_int = thos_chr + huns_chr +'-and-'+ tens_chr + ones_chr
    else:
        chr_int = thos_chr + huns_chr +tens_chr + ones_chr
    return chr_int

while True:
##    try:
        in_num = input('input something:')
        print(converter(in_num))
##    except:
##        print('something error.try again:')
##    else:
##        break

