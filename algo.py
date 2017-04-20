from input import *
from itertools import combinations

student_arr = []
pos_groups = []
groupnums = []
groupsize = 3
stunum = 9
priorities = ['t', 'i', 'l']
student_arr = read_csv('response.csv')

def tracker(groups):
	retarray = []
	for i in range(stunum):
		retarray.append(0)
	for group in groups:
		for person in group:
			retarray[person] += 1
	return retarray

def time(posgroup):
	deletedgroups = []
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
        else:
        	deletedgroups.append(group)
    print ('time', counter)
    global pos_groups
    pos_groups = newposgroups
    
def intention(groups):
	deletedgroups = []
    newposgroups = []
    counter = 0
    for group in groups:
        if (abs(student_arr[group[0]][2] - student_arr[group[1]][2]) < 2 and abs(student_arr[group[0]][2] - student_arr[group[2]][2]) < 2 and abs(student_arr[group[1]][2] - student_arr[group[2]][2]) < 2):
            counter = counter + 1
            newposgroups.append(group)
        else:
        	deletedgroups.append(group)
    global pos_groups
    pos_groups = newposgroups
    print('intention counter ', counter)
        
def language(groups):
    counter = 0
    deletedgroups = []
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
        if(flagger):
        	deletedgroups.append(group)
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
        if charnew == 't':
            time(pos_groups)
        if charnew == 'i':
            intention(pos_groups)
        if charnew == 'l':
            language(pos_groups)
        print(tracker(pos_groups))
        print(pos_groups)

    #base cases multiple group possiblities after all paramters filtered


    
driver()
