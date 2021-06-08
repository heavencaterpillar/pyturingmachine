my_str = "/home/anton/Projects/pyturingmachine/temp/rr.pkl"
my_str = my_str.split('/')
my_str[-1] = my_str[-1].split('.')
print(my_str)
print(my_str[-1][0])