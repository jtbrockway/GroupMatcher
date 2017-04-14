from Tkinter import *
import ttk
    
root = Tk()
root.title("Group Matcher")

mainframe = ttk.Frame(root, padding="30 30 120 120")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))

# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Weight your attributes:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Intention of Project").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="Known Additional Languages").grid(column=1, row=5, sticky=E)
ttk.Label(mainframe, text="").grid(column=1, row=6, sticky=W)
ttk.Label(mainframe, text="Time to Meet").grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, text="").grid(column=1, row=8, sticky=W)
ttk.Label(mainframe, text="Enter group size:").grid(column=1, row=9, sticky=W)
ttk.Label(mainframe, text="").grid(column=1, row=10, sticky=W)

def createGroups():
    print "initial groups!"

b = ttk.Button(mainframe, text="Create Groups", command=createGroups)
b.grid(column=1, row=11, sticky=E)

# Create a Tkinter variable
tkvar = StringVar(root)
 
# Dictionary with options
choices = { '1','2','3'}
tkvar.set('1') # set the default option
 
popupMenu1 = OptionMenu(mainframe, tkvar, *choices)
popupMenu1.grid(column=2, row=3)

popupMenu2 = OptionMenu(mainframe, tkvar, *choices)
popupMenu2.grid(column=2, row=5)

popupMenu3 = OptionMenu(mainframe, tkvar, *choices)
popupMenu3.grid(column=2, row=7)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )
 
# link function to change dropdown
tkvar.trace('w', change_dropdown)

ttk.Checkbutton(mainframe, text="Group 1:    ").grid(column=4, row=1, sticky=E)
ttk.Label(mainframe, text="").grid(column=4, row=2, sticky=E)
ttk.Checkbutton(mainframe, text="Group 2:    ").grid(column=4, row=3, sticky=E)
ttk.Label(mainframe, text="").grid(column=4, row=4, sticky=E)
ttk.Checkbutton(mainframe, text="Group 3:    ").grid(column=4, row=5, sticky=E)
ttk.Label(mainframe, text="").grid(column=4, row=6, sticky=E)
ttk.Checkbutton(mainframe, text="Group 4:    ").grid(column=4, row=7, sticky=E)
ttk.Label(mainframe, text="").grid(column=4, row=8, sticky=E)
ttk.Checkbutton(mainframe, text="Group 5:    ").grid(column=4, row=9, sticky=E)
ttk.Label(mainframe, text="").grid(column=4, row=10, sticky=E)

def regenerateGroups():
    print "regenerate unselected groups!"

b2 = ttk.Button(mainframe, text="Regenerate Groups", command=regenerateGroups)
b2.grid(column=4, row=11, sticky=E)

root.mainloop()