# def  some_function ():
#     return  sum(range(1000))
# result = some_function ()# return a value  and  print  execution  time

import timeit
 
strlist = ["test str" for n in range(10000)]
 
def join_test():
    return "".join(strlist)
 
def plus_test():
    result = ""
    for i in strlist:
        result = result + i
    return result
 
if __name__ == "__main__":
    jointimer = timeit.timeit()
    # print(jointimer)
    # exit()
    jointimer = timeit.Timer("join_test()", "from __main__ import join_test")
 
    print("jointime:", jointimer.timeit(number=1000))
    plustimer = timeit.Timer("plus_test()", "from __main__ import plus_test")
    print("plustime:", plustimer.timeit(number=1000))