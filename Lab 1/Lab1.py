#EvanLilga
#CSCE 364; Spring 2022
# Lab 1, Lilga_lab1.py
#Lab file showing install and basic format
def lab1_averages():
    myint = int(input("\tPlease enter an int:"))
    myfloat = float(input("\tPlease enter a float:"))
    return (myint + myfloat) / 2
def lab1_concat():
    first = input("\tPlease enter a first name: ")
    last = input("\tPlease enter a last name: ")
    return last + ", " + first
def main():
    print("Hello User, Welcome to lab 1\n\n")
    print("\n\nThanks you "+lab1_concat()+"!  You're average is "+ str(lab1_averages()))
    return
main()