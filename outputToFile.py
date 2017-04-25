import csv

def group_names(group, student_arr):
    printGroup = []
    for i in range(len(group)):
        first = student_arr[group[i]][0]
        last = student_arr[group[i]][1]
        name = first + last
        printGroup.append(name)
    return printGroup

def write_csv(final_groups, student_arr):
    with open('Groups.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter = ' ',
                                quotechar=',', quoting = csv.QUOTE_MINIMAL)
        
        for i in range(len(final_groups)):
            group = group_names(final_groups[i],student_arr) 
            spamwriter.writerow(['Group']+ [i] + [":"] + group)

