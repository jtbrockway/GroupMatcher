from tkinter import *
from tkinter import ttk
import spinbox
    
root = Tk()
root.title("Group Matcher")

# set up framework
mainframe = ttk.Frame(root, padding="30 30 120 120")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# labels for weighting attributes
ttk.Label(mainframe, text="Weight your attributes:").grid(column=1, row=1, sticky=W)
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
ttk.Label(mainframe, text="Enter group size:").grid(column=1, row=9, sticky=W)
ttk.Label(mainframe, text="").grid(column=1, row=10, sticky=W)
Spinbox(mainframe, textvariable=groupSize, from_=2, to=6, increment=1, width=6).grid(column=2, row=9)

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

#initialize checkbuttons to un-checked
cb1 = IntVar(0)
cb2 = IntVar(0)
cb3 = IntVar(0)
cb4 = IntVar(0)
cb5 = IntVar(0)

# add scrolling
# checkbuttons for list of groups
ttk.Checkbutton(mainframe, variable=cb1, text="Group 1:    ").grid(column=4, row=1, sticky=E)
ttk.Label(mainframe, text="").grid(column=4, row=2, sticky=E)
ttk.Checkbutton(mainframe, variable=cb2, text="Group 2:    ").grid(column=4, row=3, sticky=E)
ttk.Label(mainframe, text="").grid(column=4, row=4, sticky=E)
ttk.Checkbutton(mainframe, variable=cb3, text="Group 3:    ").grid(column=4, row=5, sticky=E)
ttk.Label(mainframe, text="").grid(column=4, row=6, sticky=E)
ttk.Checkbutton(mainframe, variable=cb4, text="Group 4:    ").grid(column=4, row=7, sticky=E)
ttk.Label(mainframe, text="").grid(column=4, row=8, sticky=E)
ttk.Checkbutton(mainframe, variable=cb5, text="Group 5:    ").grid(column=4, row=9, sticky=E)
ttk.Label(mainframe, text="").grid(column=4, row=10, sticky=E)

def createGroups():

	# get ordered list of weighted attributes
	weightedAttributes = weightAttributes()
	print (weightedAttributes)

	# get inputted group size
	gs = int(groupSize.get())
	print(gs)

# create groups button
b = ttk.Button(mainframe, text="Create Groups", command=createGroups)
b.grid(column=1, row=11, sticky=E)

def regenerateGroups():
	# send list of leftover people to be re-shuffled and list of saved people

	# get ordered list of re-weighted attributes
	reweightedAttributes = weightAttributes()

	# get new inputted group size
	gs = int(groupSize.get())
	print(gs)

# regenerate groups button
b2 = ttk.Button(mainframe, text="Regenerate Groups", command=regenerateGroups)
b2.grid(column=4, row=11, sticky=E)

def exportGroups():
	# export csv file of groups
    print ("export groups!")

# export button
b3 = ttk.Button(mainframe, text="Export Groups", command=exportGroups)
b3.grid(column=2, row=13, sticky=S)

root.mainloop()
