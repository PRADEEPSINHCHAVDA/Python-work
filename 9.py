# -*- coding: utf-8 -*-
"""


@author: PRADEEPSINH
"""

print("enter marks of 5 subject:")
marks=[]
 
for i in range(0,5):
    mark=int(input())
    marks.append(mark)
    
total=0
for i in range(0,len(marks)):
    total=total+marks[i]

percentage=total/len(marks)
print("mean:",percentage)
print("percentage:",percentage,"%")

if percentage<35:
    print("fail")
else:
    print("pass")