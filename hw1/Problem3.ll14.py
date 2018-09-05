import pandas as pd
import numpy as np

data = {'Midterm':[95,86,78,99,84,90,88,75,96,96],'Final':[88,88,90,95,85,77,99,80,100,80]}
data_frame = pd.DataFrame(data = data)
midterm = data_frame.get('Midterm')
final = data_frame.get('Final')

def mean(score_list):
    sum = 0
    for i in score_list:
        sum += i
    return sum/len(score_list)

def covariance(l1,l2):
    e1 = mean(l1)
    e2 = mean(l2)
    e12 = 0
    for i in range(0,len(l1)):
        e12 += l1[i] * l2 [i]
    e12 /= len(l1)
    return e12-e1*e2

def solve_a():
    return covariance(midterm,final)

def 
if __name__ == '__main__':
    l1 = [2,3,5,4,6]
    l2 = [5,8,10,11,14]
    print(covariance(l1,l2))