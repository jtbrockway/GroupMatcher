from input import *
from itertools import combinations

student_arr = []
pos_groups = []
groupnums = []
final_groups = []
leftovers = []
groupsize = 3
stunum = 9
priorities = ['T', 'I', 'K']
student_arr = read_csv('response.csv')

def tracker(groups):
    global final_groups
    global leftovers
    flagger = True
    while(flagger):
    	retarray = []
    	for i in range(stunum):
        	retarray.append(0)
        for group in groups:
        	for person in group:
        		retarray[person] += 1
        flagger2 = False
        for i in range (stunum):
            if retarray[i] == 0:
            	print('appending to leftovers: ', i)
            	if i in leftovers:
            		continue
            	else:
            		leftovers.append(i)
            if retarray[i] == 1:
                for group in groups:
                    if i in group:
                        final_groups.append(group)
                        for other in group:
                            for others in groups:
                                if other in others:
                                    flagger2 = True
                                    groups.remove(others)
                        #groups.remove(group)
        flagger = flagger2
    return groups

def time(posgroup):
    counter = 0
    newposgroups = []
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
        '''else:
            for person in group:
                deletedgroups[person].append(group)'''
    print ('time', counter)
    newpostgroups = tracker(newposgroups)
    global pos_groups
    pos_groups = newposgroups
    
def intention(groups):
    newposgroups = []
    counter = 0
    for group in groups:
        if (abs(student_arr[group[0]][2] - student_arr[group[1]][2]) < 2 and abs(student_arr[group[0]][2] - student_arr[group[2]][2]) < 2 and abs(student_arr[group[1]][2] - student_arr[group[2]][2]) < 2):
            counter = counter + 1
            newposgroups.append(group)
        '''else:
            for person in group:
                deletedgroups[person].append(group)'''
    newposgroups = tracker(newposgroups)
    global pos_groups
    pos_groups = newposgroups
    print('intention counter ', counter)
        
def language(groups):
    counter = 0
    global pos_groups
    newposgroups = []
    for group in groups:
        flagger = True
        for lang in student_arr[group[0]][3]:
            if lang in student_arr[group[1]][3]:
                if lang in student_arr[group[2]][3]:
                    flagger = False
                    newposgroups.append(group)
                    counter += 1
                    break
        '''if(flagger):
            for person in group:
                deletedgroups[person].append(group)'''
    newposgroups = tracker(newposgroups)
    print('language', counter)
    pos_groups = newposgroups

def driver():
    templist = []
    for i in range(stunum):
        templist.append(i)
    els = [list(x) for x in combinations(templist, groupsize)]
    global pos_groups
    pos_groups.append(els)
    pos_groups = pos_groups[0]
    while(len(priorities) > 0):
        charnew = priorities.pop(0)
        if charnew == 'T':
            time(pos_groups)
        if charnew == 'I':
            intention(pos_groups)
        if charnew == 'K':
            language(pos_groups)
        global leftovers
        print(leftovers)
        #print(pos_groups)
        #print("--------")
        #print(final_groups)
        print("----------")

    #base cases multiple group possiblities after all paramters filtered


    
driver()

