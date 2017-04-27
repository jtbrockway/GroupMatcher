from tkinter import *
from tkinter import ttk
import algo
import spinbox
from tkinter import filedialog

filename = ""
root = Tk()
root.title("Group Matcher")
titles = {}
selected = {}
counter = 0
groupnum = 0

# set up framework
mainframe = ttk.Frame(root, padding="30 30 80 80")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# labels for weighting attributes
ttk.Label(mainframe, text="Rank your attributes").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Intention of Project").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="Known Additional Languages").grid(column=1, row=5, sticky=E)
ttk.Label(mainframe, text="").grid(column=1, row=6, sticky=W)
ttk.Label(mainframe, text="Time to Meet").grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, text="").grid(column=1, row=8, sticky=W)

# set up group size
groupSize = StringVar(root)

# spinbox to choose group size
ttk.Label(mainframe, text="Enter group size").grid(column=1, row=9, sticky=W)
ttk.Label(mainframe, text="").grid(column=1, row=10, sticky=W)
Spinbox(mainframe, textvariable=groupSize, from_=2, to=6, increment=1, width=6, ).grid(column=2, row=9)

# set up class size
classSize = StringVar(root)

# text field to enter class size
ttk.Label(mainframe, text="Enter class size").grid(column=1, row=11, sticky=W)
ttk.Entry(mainframe, text='', textvariable=classSize, width=8).grid(column=2, row=11)
ttk.Label(mainframe, text="").grid(column=2, row=12, sticky=W)
ttk.Label(mainframe, text="").grid(column=3, row=12, sticky=W)
ttk.Label(mainframe, text="").grid(column=4, row=12, sticky=W)

# set up for weight options
w1 = IntVar(root)
oldW1 = IntVar(root)
w2 = IntVar(root)
oldW2 = IntVar(root)
w3 = IntVar(root)
oldW3 = IntVar(root)

# set up for weight options
w1.set(1)
oldW1.set(1)
w2.set(2)
oldW2.set(2)
w3.set(3)
oldW3.set(3)

# choices for weights
choices = [1,2,3]

# ensure weight1 is not the same as any other weights
def changeWeight1(val):
    if w1.get() == w2.get():
        w2.set(oldW1.get())
        oldW2.set(w2.get())
    if w1.get() == w3.get():
        w3.set(oldW1.get())
        oldW3.set(w3.get())

    oldW1.set(w1.get())

# ensure weight2 is not the same as any other weights
def changeWeight2(val):
    if w2.get() == w1.get():
        w1.set(oldW2.get())
        oldW1.set(w1.get())
    if w2.get() == w3.get():
        w3.set(oldW2.get())
        oldW3.set(w3.get())

    oldW2.set(w2.get())

# ensure weight3 is not the same as any other weights
def changeWeight3(val):
    if w3.get() == w1.get():
        w1.set(oldW3.get())
        oldW1.set(w1.get())
    if w3.get() == w2.get():
        w2.set(oldW3.get())
        oldW1.set(w1.get())

    oldW3.set(w3.get())

# create drop down menus to choose weights
OptionMenu(mainframe, w1, *choices, command=changeWeight1).grid(column=2, row=3)
OptionMenu(mainframe, w2, *choices, command=changeWeight2).grid(column=2, row=5)
OptionMenu(mainframe, w3, *choices, command=changeWeight3).grid(column=2, row=7)

# function to order weighted attributes and put them in a list
def weightAttributes():

    weightedAttributes = []

    if w1.get() == 1:
        weightedAttributes.append('I')
    if w2.get() == 1:
        weightedAttributes.append('K')
    if w3.get() == 1:
        weightedAttributes.append('T')

    if w1.get() == 2:
        weightedAttributes.append('I')
    if w2.get() == 2:
        weightedAttributes.append('K')
    if w3.get() == 2:
        weightedAttributes.append('T')

    if w1.get() == 3:
        weightedAttributes.append('I')
    if w2.get() == 3:
        weightedAttributes.append('K')
    if w3.get() == 3:
        weightedAttributes.append('T')

    return weightedAttributes

# make a tree view and put it in the grid
tv = ttk.Treeview(mainframe, selectmode='extended', height=17)
tv.grid(column=4, row=2, rowspan=10)

# set the column heading text
tv.heading('#0', text='Groups')
buttonholder = []
def displayList(numStus):
        global counter
        global groupnum
        tv.delete(*tv.get_children())
        if(counter == 0):
            groupnum = int(numStus // algo.groupsize)
            counter += 1
        for i in range(groupnum):
            button = tv.insert('', i, text = 'Group ' + str(i+1), open = True)
            grouptemp = algo.final_groups[i]
            for person in grouptemp:
                name = algo.student_arr[person][0], algo.student_arr[person][1]
                tv.insert(button, 0 , text = name)
            buttonholder.append(button)
            titles[buttonholder[i]] ='Group ' + str(i+1)
            selected[buttonholder[i]] = False


        

# setup some dictionaries to track group titles and selected state



# this function is called when the user clicks on an item in the Treeview
def onClick(event):
    iid = tv.identify('item', event.x, event.y)
    if not iid in selected:
        return
    
    isSelected = selected[iid]
    isSelected = not isSelected
    selected[iid] = isSelected
    #print("you clicked on", tv.item(iid, "text"), isSelected)
    newTitle = ''
    if isSelected:
        newTitle = '✔ ' + titles[iid]
    else:
        newTitle = titles[iid]
    tv.item(iid, text=newTitle)

# this is how the function to get clicks is hooked up
tv.bind("<Button-1>", onClick)

def createGroups():

    # get ordered list of weighted attributes
    weightedAttributes = weightAttributes()
    gs = int(groupSize.get())
    cs = int(classSize.get())
    
    algo.setPrio(weightedAttributes)
    algo.setGroupSize(gs)
    algo.setReadFile(filename)
    algo.createStudents()
    #algo.setStuNum(cs)
    algo.create(cs)
    #algo.driver()
    displayList(cs)
    
    print (weightedAttributes)

    # get inputted group size
    
    print(gs)
    print(cs)

# create groups button
b = ttk.Button(mainframe, text="Create Groups", command=createGroups)
b.grid(column=3, row=13, sticky=S)

def regenerateGroups():
    # send list of leftover people to be re-shuffled and list of saved people

    # get ordered list of re-weighted attributes
    reweightedAttributes = weightAttributes()
    algo.setPrio(reweightedAttributes)

    # get new inputted group size
    gs = int(groupSize.get())
    keepgrouplist = []
    for child in tv.get_children():
            print(tv.item(child))
    for i in range(gs):
            if selected[buttonholder[i]] == True:
                    print ('True')
                    print('List', algo.final_groups[i])
                    keepgrouplist.append(algo.final_groups[i])
            else:
                    print('False')

    
    print(gs)
    print(keepgrouplist)
    cs = algo.regen(keepgrouplist)
    displayList(cs)

# regenerate groups button
b2 = ttk.Button(mainframe, text="Regenerate Groups", command=regenerateGroups)
b2.grid(column=3, row=14, sticky=S)

def exportGroups():
    # export csv file of groups
    print ("export groups!")
    algo.output()
    root.destroy()

# export button
b3 = ttk.Button(mainframe, text="Export Groups", command=exportGroups)
b3.grid(column=4, row=13, sticky=W)

def browseFiles():
        global filename
        filename = filedialog.askopenfilename()
        pathlabel.config(text=filename)
        print(filename)
    

pathlabel = Label(root)

# export button
b4 = ttk.Button(mainframe, text="Browse Files", command=browseFiles)
b4.grid(column=2, row=13, sticky=E)

# mainframe.configure(background='blue')

root.mainloop()
