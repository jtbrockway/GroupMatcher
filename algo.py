from input import *
from itertools import combinations

student_arr = []
pos_groups = []
groupnums = []
groupsize = 3
stunum = 9
priorities = ['t', 'i', 'l']
student_arr = read_csv('response.csv')

def time(posgroup):
    counter = 0 
    newposgroups = []
    posgroup = posgroup[0]
    for group in posgroup:
        greedy = group[0]
        daymatch = []
        for i in range(5):
            for time in student_arr[greedy][4+i]:
                if time in student_arr[group[1]][4+i]:
                    if time in student_arr[group[2]][4+i]:
                        daymatch.append(i)
        flagger = False
        if len(daymatch) > 1:
            for day in daymatch:
                for otherday in daymatch:
                    if abs(otherday-day) > 1:
                        flagger = True
        if (flagger):
            counter += 1
            newposgroups.append(group)
    print ('time', counter)
    pos_groups = newposgroups
    
def intention(groups):
    newposgroups = []
    counter = 0
    for group in groups[0]:
        if (abs(student_arr[group[0]][2] - student_arr[group[1]][2]) < 2 and abs(student_arr[group[0]][2] - student_arr[group[2]][2]) < 2 and abs(student_arr[group[1]][2] - student_arr[group[2]][2]) < 2):
            counter = counter + 1
            newposgroups.append(group)
    pos_groups = newposgroups
    print('intention counter ', counter)
        
def language(groups):
    counter = 0 
    newposgroups = []
    for group in groups[0]:
        for lang in student_arr[group[0]][3]:
            if lang in student_arr[group[1]][3]:
                if lang in student_arr[group[2]][3]:
                    newposgroups.append(group)
                    counter += 1
                    continue
    pos_groups = newposgroups

def driver():
    templist = []
    for i in range(stunum):
        templist.append(i)
    els = [list(x) for x in combinations(templist, groupsize)]
    pos_groups.append(els)
    while(len(priorities) > 0):
        charnew = priorities.pop(0)
        if charnew == 't':
            time(pos_groups)
        if charnew == 'i':
            intention(pos_groups)
        if charnew == 'l':
            language(pos_groups)
        print(pos_groups)
        print(len(pos_groups[0]))

    #base cases multiple group possiblities after all paramters filtered


    
driver()
