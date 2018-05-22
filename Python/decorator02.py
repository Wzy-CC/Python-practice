def log(func):
    def inner(*args,**kw):
        print('w')
        func(*args,**kw)
    return inner

def log2(func):
    def inner(*args,**kw):
        print('w2')
        func(*args,**kw)
    return inner

@log2
@log
def add(a,b):
    print(a+b)

