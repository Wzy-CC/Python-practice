##    题目1：假设有一个敏感词文本文件 filtered_words.txt，当发现用户输入敏感词时，
##           则用星号 * 来替换这些敏感词。例如当用户输入“I love Beijing.”, 则变成
##           “I love *******.”。
##
##    要求：1）定义一个类SensitiveWordFilter来实现上面的功能。
##          2）对敏感词的查找或替换时无需区分字母的大小写形式，即如果敏感词中有“beijing”，
##             那么当用户输入“BEIJING”或者“Beijing”时，都应该用星号将其替换。

##    import re
##    print('06-04')
##    f = open('长者简介.txt')
##
##    def censor(file):
##        text = file.read()
##        text = str(text)
##        print('----------------------------原文----------------------------')
##        print(text)
##        pat1 = re.compile(r'长(.*?)者|Zhang(.*?)zhe|zhang(.*?)者|长(.*?)zhe',flags = re.IGNORECASE)
##        text_new = re.sub(pat1,'**',text)
##        print('\n')
##        print('----------------------------和谐后----------------------------')
##        print(text_new)
##    censor(f)

import re

input_words = input("please input some words:")
f = open('filtered_words.txt','w')
f.write(input_words)

f = open('filtered_words.txt')

class SensitiveWordFilter:
    def __init__(self,file_obj):
        self.text = file_obj.read()
    def censor(self):
        pat = re.compile(r'beijing',flags = re.IGNORECASE)
        text_new = re.sub(pat,"*******",self.text)
        return text_new
          
wordfilter_obj = SensitiveWordFilter(f)
print(wordfilter_obj.censor())
