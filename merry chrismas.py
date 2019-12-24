"""
this text is just writed to exercise.
"""
import random

x = "Merry"
y = "Chrismas"
fruit1 = ["apple","banana"]     #list
fruit2 = ("cherry","orange")    #tuple
a = range(5)                    #range
b = {"name":"Jerry","age":22}   #dictionary
c = {"apple","banana","cherry","orange"}    #set

def blessing():
    x = "merry"
    global z
    z = "It's Thursday."
    print(x+" "+y)




if __name__=="__main__":
    blessing()
    print(x+" "+y)
    print(z)
    print(type(fruit1),type(fruit2))
    print(a)
    print(b)
    print(random.randrange(10))