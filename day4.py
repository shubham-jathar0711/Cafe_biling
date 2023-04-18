# class Add():
#     a=10
#     def f1(self):                           #class
#         print('welcome to class')
# add= Add()
# print(Add.a)


    #write a program to calculate area of polygon using class and object

# class Polygon():
#     side = 4
#     radius=10
#     length=3
#
#     k= side/2 *length*radius
#
#     print(k)
# area=Polygon()
# print(area.k)
           #write a program to print sq of givrn numbers
# class Sqaure():
#     n=int(input('enter the number'))
#     print(pow(n,2))
# sq= Sqaure()
# print(sq.n)

#write aprogram to display happy number
#write a program to show radius of pentagon
#
# class Pentagon():
#
#     def rad(self,area,perimeter):
#         k=(2*area)/perimeter
#         print(k)
# peri=Pentagon()
# area = int(input('enter the area'))
# perimeter = int(input('enter the perimeter'))
# print(peri.rad(area,perimeter))

       #write a program to sum of all elements in list using only class
# class Num():
#     list=[3,4,5,6,7]
#     sum = 0
#     for i in list:
#         sum=sum+i
# add = Num()

# print(add.sum)




#write a program to print cube of list elements
# class Num():
#     list = [1,2,3,4,5]
#     for i in list:
#        k=print(pow(i,3))
# cube= Num()
# print(cube.k)


# #write a program to print fact of fraction
# import math
# class Frac():
#     def fact(self,f):
#
#       k=print(math.factorial(f))
# f= float(input('enter the number:'))
# fc= Frac()
# print(fc.fact(f))



#writee a program to calculate current speed
# class Speed():
#     def sp(self,Dis,Tim):
#         k= print(Dis/Tim)
# Dis=int(input('enter the distance'))
# Tim=int(input('enter the time'))
# obj=Speed()
# print(obj.sp(Dis,Tim))

#Inheritance
# class Person:
#     def _init_(self, first, last):
#         self.firstname = first
#         self.lastname = last
#     def Name(self):
#         return self.firstname + "" + self.lastname
# class Employee(Person):
#     def _init_(self, first,last,staffnum):
#         Person._init_(self,first,last)
#         self.staffnumber = staffnum
#     def GetEmployee(self):
#         return self.Name() + "" + self.staffnumber
#     x = Person("Aditya", "Adi")
#     y = Employee("Jony", "Adi", "1002")
#     print(x.Name())
#     print(y.GetEmployee())

#write a program for operator overloading
#function overloading
#function overloading in class
#program for overwriting


# Python program to draw square
# using Turtle Programming
# import turtle
#
# skk = turtle.Turtle()
#
# for i in range(4):
#     skk.forward(50)
#     skk.right(90)
#
# turtle.done()


# Python program to draw
# Spiral  Helix Pattern
# using Turtle Programming

import turtle

loadWindow = turtle.Screen()
turtle.speed(2)

for i in range(100):
    turtle.circle(5 * i)
    turtle.circle(-5 * i)
    turtle.left(i)

turtle.exitonclick()

