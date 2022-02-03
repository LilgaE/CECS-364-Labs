# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    ret_value = myf(25)
    print(ret_value)
    print(my_lam(27))
    return 0

def myf(gets):
    return gets+2


my_lam = lambda my_int : my_int * 2 if my_int <= 27 else 0

#LIST COMPREHENTION

my_list = [1,2,3,4,5]
new_list = my_list



main()