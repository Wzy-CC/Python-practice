def useLogging (old_function):
    def new_funtion(a,b):
        print('this is a log')
        print(old_function(a,b))
    return new_funtion

@useLogging
def add(a,b):
    return a+b

add(1,4)
