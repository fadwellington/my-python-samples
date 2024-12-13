#working with pdb to debug a program
import pdb

def buggy_function():
    x=10
    y=0
    pdb.set_trace()
    result=x / y
    print(result)

buggy_function()
