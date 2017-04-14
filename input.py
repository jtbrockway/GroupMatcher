import csv

file = ""
def set_file(filename):
    file = filename

def read_csv(filename):
    student_arr = []
    with open(filename) as csvfile:
        #blank = fgetcsv(filename)
        flagger = False
        for line in csvfile:
            if flagger == False:
                flagger = True
                continue
            line = line[:-1] #remove \n
            linesplit = line.split(',')
            del linesplit[0]
            finlist = []
            finlist.append(linesplit[0])
            finlist.append(linesplit[1])
            if((linesplit[2][-1])=='s'):
                finlist.append(0)
            elif((linesplit[2][-1])=='A'):
                finlist.append(1)
            else:
                finlist.append(2)
            langlist = linesplit[3].split(';')
            finlist.append(langlist)
            monlist = linesplit[4].split(';')
            tulist = linesplit[5].split(';')
            wedlist = linesplit[6].split(';')
            thlist = linesplit[7].split(';')
            frilist = linesplit[8].split(';')
            finlist.append(monlist)
            finlist.append(tulist)
            finlist.append(wedlist)
            finlist.append(thlist)
            finlist.append(frilist)
            
            student_arr.append(finlist)

        print(student_arr)

            

read_csv('response.csv')

