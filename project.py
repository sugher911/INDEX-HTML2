# info=input("enter employees name:")
# info = str(info)
# emp = ["payal", "piriya","prachi","ritik","aryan","vansh"]
# for emps in emp:
#     if emps==info:
#         print("verification successfully:")
#         break
#     else:
#         print("verification unsuccessfully:")
#         break

'''info = input("Enter employee's name: ")
info = str(info)
emp = ["payal", "piriya", "prachi", "ritik", "aryan", "vansh"]
found = False

for emps in emp:
    if emps == info:
        print("Verification successful.")
        found = True
        break

if not found:
    print("Verification unsuccessful.")


list = [1,32.4,"mohit",3+9j]
truple = "a","h","j","k"
set ={1,2,3,4,5,6,3,5,3,5,3,5,4,6,7,7,8,9,9,5,43,}
print(list)
print(type(list))
print(truple)
print(type(truple))
print(set)
print(type(set))'''

# a=4
# b=3
# a = a+b
# b = a-b
# a = a-b
# print("a",a)
# print("b",b)
# print("a",a)

# import turtle
# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("pink")
# t.pencolor("orange")
# t.speed(0)
# for i in range(150):
#     t.circle(190-i,90)
#     t.lt(90)
#     t.circle(190-i,90)
#     t.lt(18)

# import keyword
# print((keyword.kwlist))
# a = "331"
# print(type(a))
# print(a)
# b=int(a)
# c=float(a)
# print(type(b))
# print(b)
# print(type(c))
# print(c)
# import math
# a=math.factorial(5)
# print(a)

#dedine the menu of restaurant
'''menu ={
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
}
#Greet
print("Welcome to Python restaurant:")
print("Pizza: 40\nPasta: 50\nBurger:60\nSalad: 70\nCoffee: 80")

order_total = 0
#80+70=150

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total +=menu[item_1]#0 +50 = 50
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not avaialable yet")

another_order = input("Do you want to add another item? (Yes/NO)")
if another_order =="Yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not avaialable!")
print(f"The total amount of items to pay is {order_total}")'''

'''from turtle import *
import colorsys
bgcolor("black")
tracer(500)

def draw():
    h = 0
    for i in range(100):
        c = colorsys.hsv_to_rgb(h,1,1)
        h += 0.5
        up()
        goto(0,0)
        down()
        color("black")
        fillcolor (c)
        begin_fill()
        rt (98)
        circle(i,12)
        fd (290)
        fd(i)
        lt (29)
        for j in range(129):
            fd(i)
            circle(j, 299, steps=2)
        end_fill()
draw()
done()'''
# s = "programming"
# s=s [0:4]
# print(s)

# x = [1,2,3,4]
# print(sum(x))

# s = ["hello",2,4,6]
# print(len(s))

'''num = 1
while num < 5:
    print(num, end=" ")
    num +=1
    if num == 3:
        break'''
'''r = float(input("enter the area of circle:"))
pi = 3.14
result = pi*r*r
print(result)'''

'''if 1 == 0o1:
    print("true")
else:
    print("false")'''

'''result = (10+3*2**2)
print(result)

print(id(result))
a =5
print(id(a))
b = 5
print(id(b))
a = {11,22,33,44,5,4,6,3,5,3,4,4,5,33,99,55,443,55,4,3}
print(max(a))
print(len(a))'''

'''i = 0
while i < 5:
    i+=1
    if i % 2 == 0:
      continue
    print(i)'''

'''a = 4
for i in range(5):
    a*= i
print(a)'''


num =range(1,50)

def is_prime(num):
    for i in range(2,num):
        if(num%i)==0:
            return False
        return True
    
primes=list(filter(is_prime, num))
        
print(primes)