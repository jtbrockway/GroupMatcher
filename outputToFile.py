import csv


def group_names(group, student_arr):
    printGroup = []
    for i in range(len(group)-1):
        first = student_arr[group[i]][0]
        last = student_arr[group[i]][1]
        name = " ".join([first,last])
        printGroup.append(name)
    printGroup.append(student_arr[group[-1]][0] + ' ' + student_arr[group[-1]][1])
    return printGroup

def write_csv(final_groups, student_arr):
    with open('Groups.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter = ',')
        
        for i in range(len(final_groups)):
            j = i+1
            group = group_names(final_groups[i],student_arr) 
            spamwriter.writerow(['Group'  + " " + str(j) + ":"] + group)
   
