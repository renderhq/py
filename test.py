"""
num=[11,20,30,40]
evennum1=[i for i in num if i%2==0]
print(evennum1)
evennum=lambda a: "even" if a%2==0 else "odd"
print(evennum(10))
squares=[i*i for i in range(1,21)]
print(squares)
matrix=[[1,2],[3,4],[5,6]]
nums=[i for row in matrix for i in row]
print(nums)
upperletter=[ch.upper() for ch in "pythonrocks"]
print(upperletter)
nums=[1,2,3,4,5]
print(list(map(lambda a:a*2,nums)))
boys=["a","b"]
girls=[1,2]
combo=[b + " " + str(g) for b in boys for g in girls]
print(combo)
nums=[12,3,5,6,7,8,10]
evennums=list(filter(lambda a:a%2==0,nums))
print(evennums)
"""
#swapping  
a=10
b=20

a,b=b,a
print(a,b)
