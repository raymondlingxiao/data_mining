import pandas as pd
import numpy as np

data = {'Midterm':[95,86,78,99,84,90,88,75,96,96],'Final':[88,88,90,95,85,77,99,80,100,80]}
data_frame = pd.DataFrame(data = data)
midterm = data_frame.get('Midterm')
final = data_frame.get('Final')

def max_and_min(score_list):
    return max(score_list),min(score_list)

def mean(score_list):
    sum = 0
    for i in score_list:
        sum += i
    return sum/len(score_list)

def min_max(v,new_min, new_max, score_list):
    old_min, old_max = max_and_min(score_list)
    new_v = ((v-old_min)/(old_max-old_min)) * (new_max-new_min)+new_min
    return new_v

def population_var(score_list):
    mean_value = mean(score_list)
    temp = 0
    for score in score_list:
        temp += np.square(score - mean_value)

    return temp/len(score_list)

def z_score(v, score_list):
    mean_value = mean(score_list)
    standard_dev = np.sqrt(population_var(score_list))
    new_v = (v-mean_value)/standard_dev
    return new_v


def solve_a():
    student1 = min_max(midterm[0])
    student2 = min_max(midterm[1])
    student3 = min_max(midterm[2])

    return student1,student2,student3

def solve_b():
    min_max_mid = []
    for score in midterm:
        min_max_mid.append(min_max(score))
    return population_var(min_max_mid)

def solve_c():
    student4 = z_score(final[3],final)
    student5 = z_score(final[4],final)
    student6 = z_score(final[5],final)

    return student4, student5, student6

def solve_d():
    z_score_final =[]
    for score in final:
        z_score_final.append(z_score(score,final))
    return population_var(z_score_final)



if __name__ == '__main__':
    solve_a()
    solve_b()
    solve_c()
    solve_d()
