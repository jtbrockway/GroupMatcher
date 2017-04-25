import csv

file = ""
def set_file(filename):
    file = filename

def get_intent(arr,lst):
    #Function that grabs the intent of the student for the class from CSV
    #Takes in an array read in from CSV and appends to the final list that the student info will be placed in
    if((arr[2][-1])=='s'):
        lst.append(0)
    elif((arr[2][-1])=='A'):
        lst.append(1)
    else:
        lst.append(2)

def get_lang(arr, lst):
    #Function that grabs the languages a student knows from CSV
    #Takes in an array read in from CSV and appends to the final list that the student info will be placed in
    langlist = arr[3].split(";")
    lst.append(langlist)

def get_times(arr, lst):
    monlist = arr[4].split(';')
    tulist = arr[5].split(';')
    wedlist = arr[6].split(';')
    thlist = arr[7].split(';')
    frilist = arr[8].split(';')
    lst.append(monlist)
    lst.append(tulist)
    lst.append(wedlist)
    lst.append(thlist)
    lst.append(frilist)

def read_csv(filename):
    student_arr = []
    with open(filename) as csvfile:
        flagger = False
        for line in csvfile:
            if flagger == False:
                flagger = True
                continue
            line = line[:-1] #remove \n
            linesplit = line.split(',')
            del linesplit[0]
            finlist = []
            finlist.append(linesplit[0]) #Get first name
            finlist.append(linesplit[1]) #Get last name
            get_intent(linesplit,finlist)#Get intent
            get_lang(linesplit, finlist) #Get the languages
            get_times(linesplit, finlist)
            student_arr.append(finlist)
    
    return student_arr

read_csv('response.csv')

