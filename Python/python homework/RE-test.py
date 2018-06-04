##    题目3：写一个函数, 用正则表达式清除一个英文字符串s中[]和其中的内容。如:
##    s = '''Regular expressions are [essentially] a tiny, highly specialized [ programming ]
##    language []embedded inside Python and made available through the re module. '''
##
##    清除后
##    s= '''Regular expressions are  a tiny, highly specialized 
##    language embedded inside Python and made available through the re module. '''

s = '''Regular expressions are [essentially] a tiny, highly specialized [ programming ] language []embedded inside Python and made available through the re module. '''

import re
def clear_bracket(_char):
    list_recorder = []
    pat = re.compile(r'[[][^\]]*[\]]')

    _char = re.sub(pat,"",_char)
##    find = re.search(pat,str(_char))
##    while(find):
##        start,end = find.span()
##        for ele in range(start,end+1):
##            list_record.append(ele)
##            find = re.search(pat,_char)
    return _char

print(clear_bracket(s))
