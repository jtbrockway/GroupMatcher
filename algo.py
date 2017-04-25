from inputFile import *
from itertools import combinations
import outputToFile

student_arr = []
pos_groups = []
groupnums = []
final_groups = []
leftovers = []
theygone = []
groupsize = 3
stunum = 9
priorities = []
filename = ""
student_arr = []

def setPrio(prioList):
    global priorities
    priorities = prioList

def setStuNum(num):
    global stunum
    stunum = num

def setGroupSize(num):
    global groupsize
    groupsize = num

def setReadFile(file):
    global filename
    filename = file

def createStudents():
    global student_arr
    global filename
    student_arr = read_csv("response.csv")

def output():
    global final_groups
    global student_arr
    outputToFile.write_csv(final_groups, student_arr)

def tracker(groups):
    global final_groups
    global leftovers
    global theygone
    flagger = True
    while(flagger):
        flagger2 = False
        retarray = []
        for i in range(stunum):
            retarray.append(0)
        for group in groups:
            for person in group:
                retarray[person] += 1
                flagger2 = False
        for i in range (stunum):
            if retarray[i] == 0:
                if (i in leftovers) or (i in theygone):
                    continue
                else:
                    print('appending to leftovers: ', i)
                    leftovers.append(i)
            if retarray[i] == 1:
                deletegroups = []
                for group in groups:
                    if i in group:
                        final_groups.append(group)
                        for person in group:
                        	theygone.append(person)
                        print('added to final groups', group)
                        for other in group:
                            for others in groups:
                                if other in others:
                                    flagger2 = True
                                    print('found one', others)
                                    if others not in deletegroups:
                                        deletegroups.append(others)
                for thing in deletegroups:
                    groups.remove(thing)
        flagger = flagger2
    return groups

def time(posgroup):
    counter = 0
    newposgroups = []
    print(posgroup)
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
    print(groups)
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
    global pos_groups
    templist = []
    for i in range(stunum):
        templist.append(i)
    els = [list(x) for x in combinations(templist, groupsize)]
    pos_groups.append(els)
    print(pos_groups)
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
        print('leftovers', leftovers)
        #print(pos_groups)
        #print("--------")
        #print(final_groups)
        print("----------")
    
    print(leftovers)
    print(final_groups)
    print("||||||||||||||||||")
    print(pos_groups)
    while(len(leftovers) > groupsize - 1):
        nextgroup = []
        for i in range (groupsize):
            nextgroup.append(leftovers.pop())
        final_groups.append(nextgroup)
    while (len(pos_groups) > 0):
        checkar = []
        for i in range(stunum):
            checkar.append(0)
        for grp in pos_groups:
            for aperson in grp:
                checkar[aperson] =+ 1
        minnum = 100
        minperson = -1
        careabout = []
        for i in range(stunum):
            if checkar[i] > 0:
                careabout.append(i)
                if checkar[i] < minnum:
                    minnum = checkar[i]
                    minperson = i
        print('minperson', minperson)
        theygone = []
        for group in pos_groups:
            if minperson in group:
                print('removing their group: ', group)
                pos_groups.remove(group)
                final_groups.append(group)
                for other in group:
                    theygone.append(other)
                for person in group:
                    for othergroup in pos_groups:
                        if person in othergroup:
                            print('clearingout the other group', othergroup)
                            pos_groups.remove(othergroup)
                break
        checkar = []
        print('theygone', theygone)
        for i in range(stunum):
            checkar.append(0)
        for grp in pos_groups:
            for aperson in grp:
                checkar[aperson] += 1
        print('careabout', careabout)
        print(checkar[8])
        for num in careabout:
            if checkar[num] == 0:
                if num not in theygone:
                    leftovers.append(num)
                    print('adding ', num, 'to leftovers')
    while(len(leftovers) > groupsize - 1):
        nextgroup = []
        for i in range (groupsize):
            nextgroup.append(leftovers.pop())
        final_groups.append(nextgroup)
            
    print(final_groups)

    #base cases multiple group possiblities after all paramters filtered
def displayFinal():
    displayList
