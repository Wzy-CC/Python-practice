num_set = ["S","I","O","D"]

def perm(list_p,begin,end):           # begin/end is a son_set head/end
    if begin == end:
        print(list_p)
    else:
        for i in range(begin,end+1):
            list_p[begin],list_p[i] = list_p[i],list_p[begin]
            perm(list_p,begin+1,end)
            list_p[begin],list_p[i] = list_p[i],list_p[begin]

perm(num_set,0,3)
