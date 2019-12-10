
# Cops & Robbers Simulation

Project Name: brandon_and_ben 

Team Members:
- Ben Greatrix, bengreat@buffalo.edu
- Brandon Andreu, bandreu@buffalo.edu

---

## Project Description

This project was inspired from the children's game known as cops and robbers. There are two game modes. An introduction and description of each game mode can be acessed through the link below.

### Game Mode 1:

![Game_Annotation](Images/Game_Annotation.JPG)

In this mode, only one person will be playing. You will be contolling a Turtlebot which is a "Robber". The Robber is always the Turtlebot with the red base and the cop is always the Turtlebot with the blue base. Your goal as the robber is to first steal a piece of gold and then exit the area, all while not being discovered by the autonomously controlled "Copbot".

Once you are close enough, a message will appear in the Robber.py terminal alerting you that you have the gold.

![Youve_got_The_gold2](Images/Youve_got_the_gold2.JPG)

You must then drive into one of the two green exits.

Be careful not to be caught by the Copbot. If the Copbot gets too close to you (roughly a half meter) you will see the message below in your Robber.py terminal, signifying that you have lost the game.

![youve_been_caught2](Images/youve_been_caught2.JPG)

---

### Game Mode 2:

In this mode, two people will be playing. One player will be the Copbot while the other player will connect to the Robber over a linked network. The rules of the game are the same. However, the area is larger and more complex.

---

## Contributions

This project encorporates gamification into the ROS world. Our team is able to demonstrate an understanding of components of ROS such as networking, visualization, manual and autonomous control, finitie state machines, and logic all while creating a fun, interactive program.

---

## Installation Instructions

List of Prerequisite Software:
- Gazebo

"This project does not require you to generate any mazes but if you wish to develope your own area, you may do so by ...

1. Create the Package:
    ```
    cd ~/catkin_ws/src
    catkin_create_pkg brandon_and_ben rospy geometry_msgs sensor_msgs nav_msgs
    ```
2. Create our `scripts`, `robots`, `msg`, and `srv` directories:
    ```
    cd ~/catkin_ws/src/brandon_and_ben
    mkdir scripts robots msg srv
    cd ~/catkin_ws/src/brandon_and_ben/robots
    mkdir meshes urdf
    cd ~/catkin_ws/src/brandon_and_ben/robots/meshes
    mkdir images
    ```
3. Get the source code from the course github site:
    ```
    cd ~/Downloads
    rm -rf course-project-brandon_and_ben
    git clone https://github.com/IE-482-582/course-project-brandon_and_ben.git
    ```
4. Copy the Python scripts and robots to our project workspace
    ```
    cd course-project-brandon_and_ben/code/brandon_and_ben
    cp scripts/* ~/catkin_ws/src/brandon_and_ben/scripts
    cp msg/* ~/catkin_ws/brandon_and_ben/msg
    cp srv/* ~/catkin_ws/brandon_and_ben/srv
    cp robots/*.urdf.xacro ~/catkin_ws/src/brandon_and_ben/robots
    cp robots/urdf/*.urdf.xacro ~/catkin_ws/src/brandon_and_ben/robots/urdf
    cp robots/meshes/*.dae ~/catkin_ws/src/brandon_and_ben/robots/meshes
    cp robots/meshes/images/*.jpg ~/catkin_ws/src/brandon_and_ben/robots/meshes/images
    ```
    
5. Make everything executable
    ```
    cd ~/catkin_ws/src/brandon_and_ben/scripts
    chmod +x *
    ```
    
6. Compile/make our package
    ```
    cd ~/catkin_ws
    catkin_make
    ```

---

## Running the Code

*NOTE 2:  If you're generating mazes, for example, the task of GENERATING a new maze would go here.*

### Game Mode 1

We'll need four (4) terminal tabs across two (2) terminal window 

1. Open up a terminal and launch the course.
    ```
    cd ~/catkin_ws/src/brandon_and_ben/scripts
    roslaunch brandon_and_ben Mode_1_Area.launch
    ```
    
2. As you will notice later, the camera feed from the Robber is quite glitchy. It is nice to have the third person view from gazebo for reference. Go full screen on gazebo and position the area so that it is in the lower right corner of your screen, as shown below.

![Mode_1_Are_1_Setup](Images/Mode_1_Area_Setup_1.JPG)

3. In the same terminal, open up a new tab and launch the Robber controls.
    ```
    rosrun brandon_and_ben Robber_Controls.py
    ```
    
*Note: that the Copbot has been given a maximum linear speed of 1 m/s and maximum angular rotation of .3 rads/s. Adjust the speed of your Robber accordingly if you want to give the Copbot a fair shot... or don't... doesn't matter either way.*

    
4. In a new terminal, launch the Robber script.
    ```
    rosrun brandon_and_ben Mode_1_Robber.py
    ```
    
    You will see that a window appears, this is the camera feed from the Robber. If you feel confident, you can minimize gazebo and try to get away with the gold using only the view from the camera.
    
5. Take a moment to position your terminals appropriately. One good arangement is shown below

![Mode_1_Area_Setup_2](Images/Mode_1_Area_Setup_2.JPG)

6. In the same terminal as your Robber Controls, open up a new tab and launch the Copbot. The Copbot waits for no one and will begin patrolling as soon as the script is launch. Be ready to navigate back to your Robber control window as soon as you launch the Copbot.
    ```
    rosrun brandon_and_ben Mode_1_Copbot.py
    ```
    
7. Navigate to your Robber control window and try and steal the gold. Good Luck!

---

### Game Mode 2

We'll need ## (#) terminal windows

---

## Measures of Success

<TABLE>
<TR>
	<TH>Measure of Success (from your PROPOSAL)</TH>
	<TH>Status (completion percentage)</TH>
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
	<TD>Network Turtlebots</TD>
	<TD>50% Some things aren't in place yet</TD>
	
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
	<TD>75% Some more things have to be completed</TD>
	
</TR>
<TR>
	<TD>Submit final presentation</TD>
	<TD>0% Not due for another week</TD>

</TR>
</TABLE>

---

## What did you learn from this project?

We now have a solid understanding of editing urdf files for models, subscribing/publishing to topics, setting up networks, and writing logic for turtlebots. We learned techniques such as creating state machines, spinning code, and using callbacks.

---

## Future Work

*If a student from next year's class wants to build upon your project, what would you suggest they do?  What suggestions do you have to help get them started (e.g., are there particular Websites they should check out?).*

If a student wanted to imrove upon this project, some suggestions are as follows:
- Improve the speed at which the program runs
- improve upon the copbot.py script that the Copbot uses so that it is better at pursuing the Robber
- Make the program more user friendly (i.e. encorporate everything into one launch file)
- Build a map for the copbot so it can autonomsly pursue the robber in the complex area

---

## References/Resources

From The tetbook:
- Chapter 6
	- helped with understanding how to connect and use the camera on the Turtlebots
- Chapter 7
	- helped with getting started on the logicstatements for a wanderbot
- Chapter 8
	- helped with controlling a robot using the keypad
- Chapter 12
	- helped with understadning the masking used to develope a followbot
	
From Github:
- 03_wanderbot
	- used a variation of the wander.py scripts in the final project
- 05 Teleopbot
	- used the teleop_key.py script for the controls of robots in mode 2 and a variation of the keys_to_twist.py scripts in mode 1
- 06_Followbot
	- used a variation  of the move_robot.py scripts in mode 1
- 09_redball_code
	- helped with understanding how to vidualize the red base of the robber
- maze_generator
	- used to generate the courses for modes 1 and 2
- world_demo
	- helped understand how the courses were being generated
- optimatorlab/turtlebotrace
	- helped with understanding how to edit the urdf files for the turtlebots so the bases could be different colors

From ROS wiki:
- https://answers.ros.org/question/261782/how-to-use-getmodelstate-service-from-gazebo-in-python/
	- helped with figuring out how to get coordinates of Turtlebots in gazebo world
	
- http://wiki.ros.org/navigation/Tutorials/RobotSetup/Sensors
	- helped with understanding how to use information from LaserScan

From Youtube:
- https://www.youtube.com/watch?v=WqK2IY5_9OQ&feature=youtu.be
	- walked through code behind getting coordinates of multiple objects/models in gazebo

- https://www.youtube.com/watch?v=RFNNsDI2b6c
	- walked through how to read and use LaserScan data

---
