This document (`README_template.md`) provides a template for your **final** documentation (**NOT YOUR PROPOSAL**).

- Your final document should be named simply `README.md`.  
- I've left several comments below.  These should obviously be removed from your document.
- You may add additional sections as you see fit, but you should not **remove** any of the sections defined below.
- Any supplementary images should go in a directory called `Images`.  See [README.md](README.md) for more information about the required directory structure.
- Please keep in mind that the audience for this document should be students in the Fall 2019 section of this class.  (In other words, write this such that 3-month-younger you would've been able to utilize this document.)

---

# [Provide a Brief Descriptive Project Title Here]

Project Name: [provide catkin_ws name here].  
*For example, `followbot`, `wanderbot`, and `redball` are project names we've used in class.  When I install your code, I want to know where I'll find it in `~/catkin_ws/src/`*

Team Members:
- [Ben Greatrix, bengreat@buffalo.edu]
- [Brandon Andreu, bandreu@buffalo.edu]

---

## Project Description

*In this section, describe what your project does. This should be descriptive.  Someone from next year's class should be able to fully understand the aims and scope of your project. I highly recommend using pictures to help explain things.  Maybe even post a YouTube video showing your code in action.*

*NOTE:  This is not a proposal.  This is a final report describing your actual completed project.*

This project was inspired from the children's game known as cops and robbers. There are two game modes.

# Game Mode 1:

In this mode, only one person will be playing. You will be contolling a Turtlebot which is a "Robber". Your goal is to first steal a piece of gold and then exit the area, all while not being discovered by the autonomoaly controlled "Copbot". You must drive up close enough to one of the gold ingets shown below.

*insert image*

Once you are close enough, a message will appear in the Robber.py terminal alerting you that you have the gold.

*insert image*

You must then drive into one of the two exits shown below.

*insert*

Be careful not to be caught by the Copbot. If the Copbot gets too close to you (roughly a half meter) you will see the message below in your Robber.py terminal and you will lose the game.


# Game mode 2:

In this mode, two people will be playing. One player will connect to the Robber and ther other player will connect to the Robber over the network. The rules of the game are the same.

### Contributions

*In this subsection, I want to know what is new/unique/interesting about your project.*

This project encorporates gamification into the ROS world. Our team is able to demonstrate an understanding of components of ROS such as networking, visualization, manual and autonomous control, finitie state machines, and logic all while creating a fun, interactive program.

---

## Installation Instructions

*In this section you should provide instructions for someone else to install all of the code necessary to execute your project.
Your target audience should be a student from the Fall 2020 class.
You may assume that the student has ROS Indigo installed on Ubuntu 14.04.*

List of Prerequisite Software:
- [software 1] 
- [software 2]
- [etc.]
*This is just a list, not installation instructions.  The idea is to provide a summary of the additional software/packages that need to be installed.  Instructions go below.*


*Now, provide detailed step-by-step instructions to install all necessary software for your project.*

*The expectation is that the user should only have to follow these steps one time.  For example, if your project requires generating Gazebo mazes, the task of INSTALLING the maze generation code should go in this section.*

1. Create the Package:
    ```
    cd ~/catkin_ws/src
    catkin_create_pkg $$$$$$$ rospy geometry_msgs sensor_msgs
    ```
2. Create our `scripts`, and `robots` directories:
    ```
    cd ~/catkin_ws/src/$$$$$$$
    mkdir scripts, robots
    ```
3. Get the source code from the course github site:
    ```
    cd ~/Downloads
    rm -rf fall2019
    git clone https://github.com/IE-482-582/course-project-brandon_and_ben.git
    ```
4. Copy the Python scripts and robots to our project workspace
    ```
    cd course-project-brandon_and_ben
    cp scripts/* ~/catkin_ws/src/$$$$$$$/scripts/
    cp robots/* ~/catkin_ws/src/$$$$$$$/robots/
    ```
    
5. Make our Python scripts executable
    ```
    cd ~catkin_ws/src/$$$$$$$
    chmod +x *.py
    ```
    
6. Compile/make our package
    ```
    cd ~catkin_ws
    catkin_make
    ```
--

## Running the Code

*Provide detailed step-by-step instructions to run your code.*

*NOTE 1:  At this point, the user should have already installed the necessary code.  This section should simply describe the steps for RUNNING your project.*  

*NOTE 2:  If you're generating mazes, for example, the task of GENERATING a new maze would go here.*

# Mode 1

We'll need ## (#) terminal windows

1. Launch the course
    ```
    cd ~catkin_ws/src/$$$$$$$/scripts
    roslaunch $$$$$$$ $$$$$$$
    ```
    
2. In a new terminal, launch the controls for the Robber
    ```
    cd ~/catkin_ws/src/$$$$$$$/scripts
    roslaunch $$$$$$$ keyboard_teleop.launch
    ```
    
3. In a new terminal, launch the robber.py script
    ```
    cd ~/catkin_ws/src/$$$$$$$/scripts
    rosrun $$$$$$$ robber.py
    ```
    
For a more realistic experience, it is reccomended that you go full screen on the ### window and play the game from the first person perspective of the robber. Do keep the robber.py terminal in view though so you know when you have got the gold.
    
4. In a new terminal, launch the copbot.py script

    ```
    cd ~catkin_ws/src/$$$$$$$/scripts
    rosrun $$$$$$$ copbot.py
    ```

Navigate back to the controls terminal so that your keystrokes are recorded. You can stay inside the terminal while it is minimized to allow for a better view of the ### window and robber.py terminal.

5. Play the game and have fun!

# Mode 2

We'll need ## (#) terminal windows




## Measures of Success

*You have already defined these measures of success (MoS) in your proposal, and updated them after your progress report.  The purpose of this section is to highlight how well you did.  Also, these MoS will be useful in assigning partial credit.*

*The MoS summary should be in table form.  A sample is provided below:*
<TABLE>
<TR>
	<TH>Measure of Success (from your PROPOSAL)</TH>
	<TH>Status (completion percentage)</TH>
</TR>
<TR>
	<TD>Install PR2 ROS Indigo Package</TD>
	<TD>100%</TD>
</TR>
<TR>
	<TD>Write brain reader software to move the robot</TD>
	<TD>25% (brain reader software detects brain waves, but does not translate to ROS commands.)</TD>
	
</TR>
<TR>
	<TD>Complete proposal document</TD>
	<TD>100%</TD>

</TR>
<TR>
	<TD>Generate complex gazebo world</TD>
	<TD>100%</TD>

</TR>
<TR>
	<TD>Color Turlebot bases two different colors</TD>
	<TD>100%</TD>
	
</TR>
<TR>
	<TD>Spawn two Turlebots in gazebo</TD>
	<TD>100%</TD>
	
</TR>
<TR>
	<TD>Allow two Turtlebots to be controlled at the same time (Not over a network)</TD>
	<TD>100%</TD>
	
</TR>
<TR>
	<TD>Allow Copbot to know when the Robber is in its feild of view</TD>
	<TD>100%</TD>
	
</TR>
<TR>
	<TD>Generate simple gazebo world</TD>
	<TD>100%</TD>
	
</TR>
<TR>
	<TD>Allow Copbot to autonomously wander the area in search of the Robber</TD>
	<TD>100%</TD>
	
</TR>
<TR>
	<TD>Allow Copbot to autonomously follow the Robber when he is in its field of view</TD>
	<TD>100%</TD>
	
</TR>
<TR>
	<TD>Allow Robber to know its coordinates within the area</TD>
	<TD>100%</TD>
	
</TR>
<TR>
	<TD>Write final launch files for the gazebo worlds</TD>
	<TD>100%</TD>
	
</TR>
<TR>
	<TD>Write final launch files for controlling the Turtlebots</TD>
	<TD>100%</TD>
	
</TR>
<TR>
	<TD>Write final script for the Robber</TD>
	<TD>100%</TD>
	
</TR>
<TR>
	<TD>Write final script for the Copbot</TD>
	<TD>100%</TD>
	
</TR>
<TR>
	<TD>Complete final report</TD>
	<TD>100%</TD>
	
</TR>
<TR>
	<TD>Submit final presentation</TD>
	<TD>100%</TD>

</TR>
</TABLE>

*NOTE 1:  I have your proposals...don't move the goal posts!*

*NOTE 2:  For activities less than 100% complete, you should differentiate between what you completed and what you were unable to complete. I suggest you add details in a bullet list below.* 


---

## What did you learn from this project?

*For example, what concepts from class do you now have a solid understanding of?  What new techniques did you learn?*

*Also, what challenges did you face, and how did you overcome these?  Be specific.*

We now have a solid understanding of editing urdf files for models, subscribing/publishing to topics, setting up networks, and writing logic for turtlebots. We learned techniques such as creating state machines, spinning code, and using callbacks.

---

## Future Work

*If a student from next year's class wants to build upon your project, what would you suggest they do?  What suggestions do you have to help get them started (e.g., are there particular Websites they should check out?).*

If a student wanted to imrove upon this project, some suggestions are as follows:
- Improve the speed at which the program runs
- improve upon the ## and ## script that the Copbot uses so that it is better at pursuing the Robber
- Make the program more user friendly (i.e. encorporate everything into one launch file)
- Build a map for the copbot so it can autonomsly pursue the robber in the complex area

---

## References/Resources

*What resources did you use to help finish this project?*
- Include links to Websites.  Explain what this Website enabled you to accomplish.
- Include references to particular chapters/pages from the ROS book.  Why was each chapter necessary/helpful?



