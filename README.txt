Group Name: Munder Difflin Paperless Co.
Group Members:
	-Jack Brockway
	-Kristen Splonskowski
	-Elizabeth Olson

---------------------------------------
   Requirements to Run GroupMatcher
---------------------------------------
	-Must have Python3.6 installed on computer that is running GroupMatcher program
	-Some users may need to install ActiveTcl 8.6
		-Link to ActiveTcl 8.6: https://www.activestate.com/activetcl/downloads
	-The survey used to obtain the csv input for this program is at:
		https://docs.google.com/forms/d/19ffTN3xbHsEepRt_AJltbJFMf-ycbING9uv_HM9Gt6c/edit?usp=sharing
	Please Note:
		-Included in the GroupMatcher git repository is a file named "responses.csv"
			This file can be used as test input to see the functionality of this program.
		-responses.csv has 30 entries
			-When entering class size, please use 30 if using responses.csv
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
		(Please Note: Class Size needs to be evenly divisible by Group Size)
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

	To change Group Size:
		-Highlight number in text box next to "Enter group size"
		-Enter the number for how large you want groups to be
			OR
		-Use the Up arrow or down arrow in the text box next to "Enter group size" until you've reached the desired group size

	To enter class size:
		-Left click on text box next to "Enter class size"
		-Enter the number indicating the size of your class into the text box
			(Note: This number should be the same as the number of students in the csv input file)

--------------------------------------
	Algorithm: How to add to it
--------------------------------------
	To add another filter:
		-Define a function inside algo.py for your filter that takes in
			-Possible groups array
			-Students array
			-Number of students
		-Assign a single character tag for your filter
		-In the first while loop in algo.py's driver function add:
			if charnew == 'yourChar':
            			pos_groups = yourFilter(pos_groups, student_arr, numStudent)
		-In GroupMatcher.py:
			Add the code:
				wn = IntVar(root)
				oldWn = IntVar(root)
				wn.set(n)
				oldWn.set(n)
				(Where n is the number of the filter you are adding
					(ie: if just adding one filter, you would do w4=IntVar(root), etc...))
				Add n to the choices array
				Create a changeWeightn function identical to changeWeight1 except where n is the n from wn
				Add: OptionMenu(mainframe, wn, *choices, command=changeWeight3).grid(column=2, row=(3+2n))
				Add the necessary if statements in the weightAttributes function
					(These should be similar to the 3 sets of if statements already in weight attributes
						(ie: if wn.get() == 1: weightedAttributes.append("yourChar")))
		
	Use the intention function in algo.py as template with which to design your filter
---------------------------------------
	GUI: How to add to it
---------------------------------------
	Open GroupMatcher.py

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

---------------------------------------
	How GroupMatcher Outputs
---------------------------------------
	-After running "Create Groups" or "Regenerate Groups", the GroupMatcher GUI will display the groups it created in the "Groups" section of the GUI
	-Once you see the groups in the "Groups" section, you can press the "Export Groups" button
	-After pressing the "Export Groups" button, the GroupMatcher GUI will close
	-The final groups output will be in a csv file named "Groups" which will be located in the same folder as GroupMatcher.py

---------------------------------------
	Effictiveness of Algorithm
---------------------------------------
	When running GroupMatcher using 'responses.csv', with a class size 30 and a group size of 3,
		any ranking of priorities for filters results in 8/10 groups in which
			-All members can meet a tleast twice a week, each meeting being at least 2 days apart.
			-All members share at least 1 common language
			-All members share a similar intention for the project
