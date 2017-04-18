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
            newposgroups.append(group)
    print(newposgroups)
    #done making newposgroups
    
def intention(group):
    print('intention')

def language(group):
    print('language')

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

    #base cases multiple group possiblities after all paramters filtered


    
driver()
