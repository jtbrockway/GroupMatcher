from input import *
from itertools import combinations

student_arr = []
pos_groups = []
groupnums = []
groupsize = 3
stunum = 6
priorities = ['t', 'i', 'l']

def time(posgroup):
	newposgroups = []
    for group in posgroup:
    	greedy = group[0]
    	daymatch = []
    	for i in range(5):
    		for time in student_arr[greedy][5+i]:
    			if student_arr[posgroup[1]][5+i].contains(time):
    				if student_arr[posgroup[2]][5+i].contains(time):
    					daymatch.append(i)
    	flagger = False
    	if len(daymatch) > 1
    		for day in daymatch:
    			for otherday in daymatch:
    				if abs(otherday-day) > 1:
    					flagger = True
    	if (flagger):
    		newposgroups.append(group)
    #done making newposgroups
    
def intention(group):
    print('intention')

def language(group):
    print('language')

def driver():
    student_arr = read_csv('response.csv')
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
