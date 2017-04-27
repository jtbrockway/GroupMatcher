from inputFile import *
from itertools import combinations
import outputToFile

student_arr = []
pos_groups = []
groupnums = []
final_groups = []
leftovers = []
theygone = []
groupsize = 0
stunum = 0
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
    #CHANGE THIS BEFORE SUBMISSION!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    student_arr = read_csv("response.csv")

def output():
    global final_groups
    global student_arr
    outputToFile.write_csv(final_groups, student_arr)

def tracker(groups, numStus):
    global final_groups
    global leftovers
    global theygone
    flagger = True
    while(flagger):
        flagger2 = False
        retarray = []
        for i in range(numStus):
            retarray.append(0)
        for group in groups:
            for person in group:
                retarray[person] += 1
                flagger2 = False
        for i in range (numStus):
            if retarray[i] == 0:
                if (i in leftovers) or (i in theygone):
                    continue
                else:
                    leftovers.append(i)
            if retarray[i] == 1:
                deletegroups = []
                for group in groups:
                    if i in group:
                        final_groups.append(group)
                        for person in group:
                        	theygone.append(person)
                        for other in group:
                            for others in groups:
                                if other in others:
                                    flagger2 = True
                                    if others not in deletegroups:
                                        deletegroups.append(others)
                for thing in deletegroups:
                    groups.remove(thing)
        flagger = flagger2
    return groups

def time(posgroup, students, numStus):
    counter = 0
    newposgroups = []
    for group in posgroup:
        greedy = group[0]
        daymatch = []
        for i in range(5):
            for time in students[greedy][4+i]:
                flaggertime = True
                for j in range(groupsize):
                    if time in students[group[j]][4+i]:
                        continue
                    else:
                        flaggertime = False
                if flaggertime == True:
                    if i not in daymatch:
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
    newposgroups = tracker(newposgroups, numStus)
    return newposgroups
    
def intention(groups, students, numStus):
    newposgroups = []
    counter = 0
    for group in groups:
        flagger1 = True #true if everyone is just wanting to pass or get an A
        flagger2 = True #true if everyone is wanting an A or a major resume item
        for student in group:

            if students[student][2] > 1:
                flagger1 = False
            if students[student][2] < 1:
                flagger2 = False
        if(flagger1 or flagger2):
            counter = counter + 1
            newposgroups.append(group)
    newposgroups = tracker(newposgroups, numStus)

    return newposgroups
        
def language(groups, students, numStus):
    counter = 0
    newposgroups = []
    counter = 0
    for group in groups:
        flagger = True
        for lang in students[group[0]][3]:
            for student in group:
                if lang in students[student][3]:
                    continue
                else:
                    flagger = False
            if(flagger):
                newposgroups.append(group)
                counter += 1
                break
    newposgroups = tracker(newposgroups, numStus)
    return newposgroups
    
def create(numStu):
    global student_arr
    driver(numStu, student_arr)

def regen(keepgrouplist):
    global theygone
    theygone = []
    global final_groups
    tempfin = []
    global student_arr
    newarr = []
    counter = 0
    for group in final_groups:
        if group in keepgrouplist:
            tempfin.append(group)
        else:
            for person in group:
                counter += 1
                tempbin = student_arr[person]
                newarr.append(tempbin)
    final_groups = []
    driver(counter, newarr)
    for group in final_groups:
        newgroup = []
        for person in group:
            for i in range(len(student_arr)):
                if student_arr[i][0] == newarr[person][0]:
                    if student_arr[i][1] == newarr[person][1]:
                        newgroup.append(i)
        tempfin.append(newgroup)
    final_groups = tempfin
    print(final_groups)
    return counter


                
    

def driver(numStudents, stuarray):
    global pos_groups
    templist = []
    for i in range(numStudents):
        templist.append(i)
    els = [list(x) for x in combinations(templist, groupsize)]
    pos_groups.append(els)
    pos_groups = pos_groups[0]
    while(len(priorities) > 0):
        charnew = priorities.pop(0)
        if charnew == 'T':
            pos_groups = time(pos_groups, student_arr, numStudents)
        if charnew == 'I':
            pos_groups = intention(pos_groups, student_arr, numStudents)
        if charnew == 'K':
            pos_groups = language(pos_groups, student_arr, numStudents)
    global leftovers
    while(len(leftovers) > groupsize - 1):
        nextgroup = []
        for i in range (groupsize):
            nextgroup.append(leftovers.pop())
        final_groups.append(nextgroup)
    while (len(pos_groups) > 0):
        checkar = []
        for i in range(numStudents):
            checkar.append(0)
        for grp in pos_groups:
            for aperson in grp:
                checkar[aperson] += 1
        minnum = 100
        minperson = -1
        careabout = []
        for i in range(numStudents):
            if checkar[i] > 0:
                careabout.append(i)
                if checkar[i] < minnum:
                    minnum = checkar[i]
                    minperson = i
        theygone = []
        for group in pos_groups:
            if minperson in group:
                pos_groups.remove(group)
                final_groups.append(group)
                for other in group:
                    theygone.append(other)
                for person in group:
                    for othergroup in pos_groups:
                        if person in othergroup:
                            pos_groups.remove(othergroup)
                break
        checkar = []
        for i in range(numStudents):
            checkar.append(0)
        for grp in pos_groups:
            for aperson in grp:
                checkar[aperson] += 1
        for num in careabout:
            if checkar[num] == 0:
                if num not in theygone:
                    leftovers.append(num)
    while(len(leftovers) > groupsize - 1):
        nextgroup = []
        for i in range (groupsize):
            nextgroup.append(leftovers.pop())
        final_groups.append(nextgroup)

    #base cases multiple group possiblities after all paramters filtered
