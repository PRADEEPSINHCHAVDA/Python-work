# -*- coding: utf-8 -*-
"""


@author: PRADEEPSINH
"""

print("enter days:")
day=int(input())
 
year=day/360
months=(day%360)/30
days=(day%360)%30

print("years=",int(year),"months=",int(months),"days=",int(days))