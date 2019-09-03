# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:28:32 2019

@author: SunA
"""

def solution(clothes):
    dic = {}
    for i in clothes:
        dic[i[1]] = []
    for i in clothes:
        dic[i[1]].append(i[0])
    answer = 1
    for i in dic.keys():
        answer = answer*(len(dic[i])+1)

    return answer-1