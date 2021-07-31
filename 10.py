# -*- coding: utf-8 -*-
"""
@author: PRADEEPSINH
"""

def simple_interest(amount,time,rate):
    si=(amount*time*rate)/100
    print("simple interest:",si)
print("enter amount:")
amount=int(input())
print("enter time:")
time=int(input())
print("enter rate")
rate=float(input())

simple_interest(amount,time,rate)