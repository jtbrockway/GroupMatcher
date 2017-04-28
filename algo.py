from inputFile import *
from itertools import combinations
import outputToFile

final_groups = []  #List of the final groups 
student_arr = []   #Students obtained from input file
pos_groups = []    #All possible groups of size n
leftovers = []     #People who were removed from all of their possible groups
theygone = []      #Holds people who were removed from groups
groupsize = 0      #Size of Groups
stunum = 0         #Class size
priorities = []    #List of filter priorty - Obtained from GUI
filename = ""      #File to read input from

'''
Setter functions
    These functions set global variables.
    Used so that input from GUI can be used in running the algorithm
'''
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
    student_arr = read_csv(filename)

def output():
    global final_groups
    global student_arr
    outputToFile.write_csv(final_groups, student_arr)
'''
End of Setter functions
'''

'''
Tracker Function
If a person has only one group remaining, makes sure that group will be saved
Considers the others in that group and stops considering their other remaining groups 
Tracks which people are not in any of the remaining groups
'''
def tracker(groups, numStus):
    global final_groups
    global leftovers
    global theygone
    flagger = True
    while(flagger):
        flagger2 = False
        retarray = []
        deletegroups = []
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
                    print("Adding student", i, "to leftovers in tracker")
                    leftovers.append(i)
            if retarray[i] == 1:
                for group in groups:
                    if i in group:
                        if group not in final_groups:
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
    
'''
Filter Functions
Filters through a set of possible groups and eliminates groups that do not meet its 
pass fail criteria of group validity
'''

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
    '''
    Filters out groups if there is a person who wants this to be a major resume item with someone 
    who just wants to pass
    '''
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
    '''
    Filters out groups if there is not one strong language in common
    '''
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

'''
Button Functions
'''

def create(numStu):
    '''
    Run when the create button is pressed
    '''
    global student_arr
    driver(numStu, student_arr)

def regen(keepgrouplist):
    '''
    Run when the regenerate button is pressed
    Re-runs the algorithm with new priority list, but saves the groups selected by the user
    '''
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
    return counter
                
'''
Group Division 
'''    

def driver(numStudents, stuarray):
    '''
    Creates all possible groups. Runs groups through filters in the order of user's priority
    '''
    global pos_groups
    templist = []
    for i in range(numStudents):
        templist.append(i)
    pos_groups = [list(x) for x in combinations(templist, groupsize)]
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
        flagger3 = True
        for group in pos_groups:
            if minperson in group:
                toremove = []
                if flagger3 == True: 
                    flagger3 = False
                    if group not in toremove:
                        toremove.append(group)
                    final_groups.append(group)
                    for person in group:    
                        theygone.append(person)
                        for othergroup in pos_groups:
                            if person in othergroup:
                                if othergroup not in toremove:
                                    toremove.append(othergroup)
                for removeit in toremove:
                    pos_groups.remove(removeit)
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
