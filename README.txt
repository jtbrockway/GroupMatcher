---------------------------------------
   Requirements to Run GroupMatcher
---------------------------------------
	-Must have Python3.6 installed on computer that is running GroupMatcher program
	-Some users may need to install ActiveTcl 8.6
		-Link to ActiveTcl 8.6: https://www.activestate.com/activetcl/downloads


---------------------------------------
	How to Run GroupMatcher
	    On MacOS/Linux
---------------------------------------
	-Open command line/Terminal 
	-Navigate to and enter GroupMatcher folder
	-Type into command line "python3 GroupMatcher.py" (Without quotes)
	-Press Enter

---------------------------------------
	How to Run GroupMatcher
	      On Windows
---------------------------------------
	If Python is a part of Your PATH:
		-Navigate to and enter GroupMatcher folder
		-Type into command line "python.exe GroupMatcher.py" (Without quotes)
		-Press Enter
	Otherwise:
		-Navigate to and enter GroupMatcher folder
		-Type into command line "FULL_PATH_TO_PYTHON_INTERPRETER GroupMatcher.py" (Without quotes)
		-Press Enter
		Example:		
		C:\Python36\python.exe C:\Users\Username\Desktop\GroupMatcher\GroupMatcher.py

---------------------------------------
	How to Use GroupMatcher
---------------------------------------
	Steps:
	1). Rank your filters priorities
	2). Set your Group size
	3). Enter your Class size
	4). Press "Browse Files" and select the csv file that will be used for input
	5). Press "Create Groups" button to run the GroupMatcher algorithm
 	(Optional: If you would like to run certain groups through the algorithm again)
		6). Select the groups that you would like to keep
		7). Change the priorities for the filters to determine in which order the filters will be applied to the groups being run through the GroupMatcher algorithm again.
		8). Press the "Regenerate Groups" Button
		9). Repeat until satisfied with the groups
	10). Press "Export Groups" button

	To View Groups:
	11). Navigate to folder that GroupMatcher.py is in
	12). Open "Groups.csv"

	Filters:
		-The first three pieces of text following "Rank your Attributes" in the GroupMatcher GUI,
			-"Intention of Project"
			-"Known Additonal Languages"
			-"Time to meet"
		are "Filters"
		-The "Filters" are what the GroupMatcher algorithm uses to determine which groups are viable
		-The numbers next to the filters indicate the priority of the filter
			-The lower the number next to a filter is, the higher priority that filter has
		-The priority of a filter indicates when the GroupMatcher algorithm will pass the possible groups through that filter
			-If a filter has priority 1 then the GroupMatcher algorithm passes the possible groups through that filter first

	Group Size:
		-The fourth piece of text is the group size
		-The group size number dictates how many people are placed in a group
		
	Class Size:
		-The fifth piece of text is class size
		-The class size number tells the GroupMatcher algorithm how many people need to be placed into groups

	Browse Files Button:
		-The browse files button will open up a file browser
			-Use the file browser to browse to the csv file that has the student responses to the survey
			-Once you have located the csv file you want to use, left click the file and press the "Open" button in the file browser

	Create Groups Button:
		-The Create Groups button will execute the GroupMatcher Algorithm
		-The Create Groups button should be pressed after you have:
			-Set Filter priorities
			-Entered your desired group size
			-Entered your class size
			-Browsed and selected the csv file you will be using
	
	"Groups" section of GUI:
		-After pressing the Create Groups button, the GroupMatcher algorithm will execute
		-When the algorithm is finished, the groups that the algorithm created will be displayed in the section on the right side of the GUI labled "Groups"
		-You may click on individual groups that you would like to keep by clicking on the groups name in the "Groups" display
			(ie: click on "Group 1" if you would like to keep Group 1 together)
		-The non-selected groups will be reformed if the "Regenerate Groups" button is pressed
	
	Regenerate Groups Button:
		-The Regenerate Groups button will take all non-selected groups and run the people in those groups through the algorithm again
		-Before clicking on the Regenerate Groups button you need to:
			-Select the groups in the "Groups" section of the GUI that you do not want to run through the algorithm again
			-Set the priorities for the filters again if you would like the people to be filtered through the algorithm differently

	Export Groups Button:
		-When clicked, the Export Groups button will export the final groups seen in the "Groups" section of the GUI into a CSV file named "Groups"
			-The "Groups" csv file can be found in the GroupMatcher folder, or the same folder in which the GroupMatcher.py is being ran in.
		Note: When the Export Groups Button is clicked, the GUI will close and GroupMatcher.py will be finished executing.


	To change which filter groups get passed through first:
		-Left click on the number box to the right of the filter you want to change the priority of
		-Select which priority you would like that filter to have
		-Priority 1 means that the selected filter runs first
		-Priority 3 means the selected filter runs last

---------------------------------------
	GUI: How to add to it
---------------------------------------

	To add a button:
		- Use ttk.Button(mainframe, text="Button Name", command=commandYouWantToHookUp))
		- Create a function to call when your button is clicked

	To add a text box:
		- Use ttk.Entry(mainframe, text="Text", textvariable=variableToHookItUpTo)

	To add a label:
		- Use ttk.Label(mainframe, text="Text for label")

	To add a spinbox:
		- Use Spinbox(mainframe, textvariable=variableToHookItUpTo, from_=lowesgtValue, to=highestValue, increment=valueToIncrementBy)

	To add a treeview:
		- Use ttk.Treeview(mainframe, selectmode='extended', height=whatEverHeightYouWant)
		- treeview.heading('#0', text='Name of treeview')

	To layout widgets in the grid (all of the above are widgets):
		- widgetName.grid(column=int, row=int)

Program outputs to a csv file named "Groups.csv"

Number of students and groupsize need to be divisible