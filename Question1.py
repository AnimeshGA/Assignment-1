# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 16:31:44 2021

@author: Royal
"""

#LIST METHODS

#append
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

#clear
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

#copy
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

#count
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)

#extend
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

#index
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

#insert
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

#pop
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

#remove
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

#reverse
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

#sort
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

#LIST EXERCISE
#Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print()

#Answer
fruits = ["apple", "banana", "cherry"]
print(fruits[1])


#TUPLE METHODS

#count
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

#index
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

#TUPLE EXERCISE
#Print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print()

#Answer
fruits = ("apple", "banana", "cherry")
print(fruits[0])


#SET METHODS

#add
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

#clear
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

#copy
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

#difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

#difference update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

#discard
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

#intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#intersection update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#isdisjoint
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

#issubset
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

#issuperset
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

#pop
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

#remove
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

#symmetric difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#symmetric difference update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#union
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

#update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

#SET EXERCISE
#Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if"apple" in fruits:   
  print("Yes, apple is a fruit!")

#Answer
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
 print("Yes, apple is a fruit!")
 

#DICTIONARY METHODS

#clear
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)

#copy
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()
print(x)

#fromkeys
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#get
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)

#items
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)

#keys
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)

#pop
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)

#popitem
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car)

#setdefault
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)

#update
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car)

#values
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)

#DICTIONARY EXERCISES
#Use the get method to print the value of the "model" key of the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print()

#Answer
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#IF CONDITIONS

#if
a = 33
b = 200
if b > a:
 print("b is greater than a")

#elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
#else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Short hand if
if a > b: print("a is greater than b")

#Short hand if else
a = 2
b = 330
print("A") if a > b else print("B")

#and
a = 200
b = 33
c = 500
if a > b and c > a:
 print("Both conditions are True")

#or
a = 200
b = 33
c = 500
if a > b or a > c:
 print("At least one of the conditions is True")

#nested if
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#pass statement
a = 33
b = 200
if b > a:
  pass


#LOOPS

@whileloops

#while loop
i = 1
while i < 6:
  print(i)
  i += 1
  
#break statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
#continue statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#else statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
@forloops

#for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
#Looping Through a String
for x in "banana":
  print(x)
  
#The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
#The range Function
for x in range(6):
  print(x)


#Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")


#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
#pass Statement
for x in [0, 1, 2]:
  pass