"""
print("hello world")
print(10)
print([1,2,3])
name="jai"
age=18
cgpa=8.0
is_student=True
print(type(is_student))
name=input("enter ur name")
print(name)
age=int(input("enter ur age"))
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)#power
print(a//b) #takes lowest whole number
age=20
if True:
    print("jai loves shalini")
if age>18:
    print("ur adult")
else:
    print("ur young")
for i in range(4):#used when number of iterations known
    print(i)
i=4
while i<=10: #runs until the condition becomes false
    print(i)
    i+=1
list=["jaideep",18,8.0] #collection of multiple values
print(list)
print(list[0])
list[0]="shalini" #lists can be modified
print(list)
list.insert(1,"pawan")
print(list)
name='Jaideep'
print(len(name))
print(name[0:9:2])
print(name[-1:-4:-1])
print(name.lower())
print(name.upper())
print(name.replace("deep","shaluu"))
def greet():
    return "hello jai"
def add(a,b):
    return a+b
print(add(10,2))
tuple=(10,"jai",8.0,18)
print(tuple)#tuples are same like lists only but immuattble
print(tuple[0])
print(tuple[0:3])
student={"name":"jaideep","age":18,"cgpa":8.0}
print(student["age"])
student["country"]="india"
print(student)
del student["cgpa"]
print(student)
student["age"]=19
print(student)
#sets
set={10,20,30,10}
print(set)
set.add(40)
print(set)
#typecasting
x=10
y=float(x)
print(y)
z=24.335
j=int(z)
print(j)
#list compherensio:shortest approach to create list
#syntax list=[what u want for item in iterable if condition]
squares=[]
for i in range(10):
    squares.append(i*i)
print(squares)
squares=[i*i for i in range(10) if i%2==0]
print(squares)
evensquares=[i*i for i in range(1,100) if i%2==0]
print(evensquares)
squares=[]
for i in range(1,100):
    squares.append(i*2)
print(squares)
num=[-1,-2,-3,-4,1]
positive=[i for i in num if i>0]
print(positive)
capletters=[i.upper() for i in "jaideep"]
print(capletters)
num=[1,2,3,4,5,6,7,8,9,10]
evennum=[i for i in num if i%2==0]
print(evennum)
#combining two strings
a="hello"
b="jai"
print(a +" "+ b)
print(f"{a}  {b}")
c="".join[a,b]
print(c)
#nested list compherension
boys=["jai","shalini"]
girls=["shaluuu","deep"]
#using nested loops
combo=[]
for b in boys:
    for g in girls:
       combo.append(b + " " + g)
#combo=[b+ " " + g for b in boys for g in girls]
print(combo) 
#2d flat
matrix=[[1,2,3],[4,5,6],[7,8,9]]
num=[i for row in matrix for i in row ]
print(num)
#list comphrehension using functions
def cube(x):
    return x*x*x
cubenum=[cube(i) for i in range(1,10) ]
print(cubenum)
#if else list compherension
list=[1,2,3,4,5,6,7,8,9,10]
evennum=["even" if x%2==0 else "odd" for x in list ]
print(evennum)
#lambda function
#syntax :lambda argu:exp
x=lambda a:a*a
print(x(2))
pow=lambda a,b:a**b
print(pow(10,2))
evennum=lambda a:"even" if a%2==0 else "odd"
print(evennum(8))
nums=[1,2,3,4,5]
doublenum=list(map(lambda a:a*2,nums))
print(doublenum)
nums=[1,2,3,4,5]
evennum=list(filter(lambda a:a%2==0,nums))
print(evennum)
list=[["jai",10],["jassu",20],["pawan,30"]]
#map detail
#syntax:map(func,iterable)
def square(x):
    return x*x
num1=[1,2,3,4]
num2=[5,6,7,8]
#print(list(map(square,nums)))
#print(list(map(lambda x:x*x,nums)))
words=['jai','shalu','pawan']
print(list(map(str.upper,words)))
print(list(map(lambda x,y:x+y,num1,num2)
nums=["10","20","30"]
print(list(map(int,nums)))
from operator import mul
a=[1,2,3]
b=[10,20,30]
print(list(map(mul,a,b)))
it=map(lambda x:x*2,range(10))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#filter
def is_pos(n):
    return n>0
nums=[-1,-2,-3,4,5,6]
word=["jai","pawan","shalini"]
print(list(filter(is_pos,nums)))
print(list(filter(lambda x:x%2==0 and x>2,nums)))
print(list(filter(lambda x:len(x)>3,word)))
print(list(filter(lambda x:x%2==0,nums)))
#using none as a function
words=[None,30,0,{},[],"","jai"]
print(list(filter(None,words)))
#filters with advanced way
students=[
    {"name" : "jai","marks":20},{"name":"shalini","marks":100},{"name":"pawan","marks":90}
]
print(list(filter(lambda x:x["marks"]>50,students)))
#reduce:it takes a function and applies it to all items and transform into single element
from functools import reduce
#syntax reduce(func,iterable,intialzer)
nums=[1,2,3,4,5]
print(reduce(lambda a,b:a+b,nums))
print(reduce(lambda a,b:a*b,nums))
print(reduce(lambda a,b:a if a>b else b,nums))
print(reduce(lambda a,b:a+b,nums,10))
words=["jai","loves","shaluu"]
print(reduce(lambda x,y: x+ " " + y,words))
#enumerate:used for both index and value
#syntax:enumerate(iterable,list)
items=["jai","python","ml"
for index,value in enumerate(items):
    print(index,value)
for i,j in enumerate("jaideep"):
    print(i,j)
for i,j in enumerate("jaideep",start=2):
    print(i,j)
items=["jai","python","ml"] 
print(list(enumerate(items)))
print(f"{i}{j}" for i,j in enumerate(items))
matrix=[[1,2,3],[4,5,6]]
for row_index,row in enumerate(matrix):
    for col_index, val in enumerate(row):
         print(row_index,col_index,val)
         """
a=[1,2,3]
b=["jai","shalu","pawan"]
print(list(zip(a,b)))
for x,y in zip([10,20,30],[40,50,60]):
    print(x,y)
    a=[1,2,3]
b=["jai","shalu","pawan"]
city=["vizag","nellore","kadapa"]
print(list(zip(a,b,city)))
#creating dict using zips
keys=["name","age","sex"]
value=["jai",18,"male"]
print(dict(zip(keys,value)))