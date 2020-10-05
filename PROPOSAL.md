
# IE482 Project - Cops and Robbers

Team Members:
- Ben Greatrix, bengreatrix@buffalo.edu
- Brandon Andreu, bandreu@buffalo.edu

--- 

## Project Objective
The inspiration behind this project is the children's game known as cops and robbers. Inside of Gazebo we plan to simulate 2 Turtlebots. One Turtlebot will be the "Copbot" and it will patrol the area in search of a "criminal". The criminal will be another Turtlebot. The goal of the criminal is to steal one of two pieces of goal and escape the area without the Copbot catching him. The goal of the Copbot is to find the criminal and capture him before he can get away with the gold.


## Contributions
There will be two modes for this game. In the firt mode, the area will be small and simple. The criminal will be controlled manually by a player and the Copbot will autonomosly patrol the area. If you are seen by the Copbot he will follow and if he gets close enough you will have been "captured" and the game will be over.

In the second mode, the area will be larger and more complex. The criminal will still be controlled manually by a player but the Coptbot will also be controlled manually by a second player over a network. The same game rules will apply.

This project demostrates the understaing of how to network computers, subcribe/publish to topics, edit .urdf files, model worlds in gazebo, apply logic statements to robots, and use states to control robots.


## Project Plan
We will achieve with the help of:
- The textbook (with special attention paid towards chapters 6, 7, 8, and 12)
- The IE-482-582/fall2019 repository (with special attention paid towards 03_Wanderbot, 05_Teleopbot, and 06_Followbot)
- The IE-482-582/fall2018 repository (with special attention paid towards (09_redball_code, maze_generator, and world_demo)
- The optimatorlab/turtlebotrace repository
- ROS wiki
- Youtube

A modified version of the turtlbotrace scripts will be used to launch the gazebo worlds with multiple Turtlebots. The Copbot will wander the area with a modified version of the wander.py script from chapter 7. The Copbot will know when it has seen the Robber and follow it with a modified version of the move_robot.py script from the 09_redball_code repositiry. The Turtlebots will be controlled using a modified version of the keyboard_teleop.py script and they will be networked using .............


## Milestones/Schedule Checklist
{What are the tasks that you need to complete?  Who is going to do them?  When will they be completed?}
- [x] Complete this proposal document.  *Due Oct. 25*
- [x] Generate complex gazebo world.  *Due Sep. 24*
- [x] Color Turtlebot bases two different colors.  *Due Sep. 26*
- [x] Spawn two turtlebots in Gazebo.  *Due Sep. 28*
- [x] Allow multiple Turtlebots to be controlled at the same time (Not over a network).  *Due Sep. 29*
- [x] Allow Copbot to know when the Robber is in its feild of view.  *Due Dec. 1*
- [x] Generate simple gazebo world.  *Due Dec. 1*
- [ ] Network Turtlebots.  *Due Dec. 2*
- [x] Allow Copbot to autonomously wander the area in search of the Robber.  *Due Dec.3*
- [x] Allow Copbot to autonomosly follow the Robber when he is in its field of view.  *Due Dec. 4*
- [x] Allow Robber to know its coordinates within the area.  *Due Dec. 4*
- [x] Write final launch files for the gazebo worlds.  *Due Dec. 5*
- [x] Write final launch files for controlling the Turtlebots.  *Due Dec. 6*
- [x] Write final script for the Robber.  *Due Dec. 8*
- [x] Write final script for the Copbot.  *Due Dec. 8*
- [x] Complete final report.  *Due Dec. 16*
- [X] Submit final presentation  *Due Dec. 16*


## Measures of Success
The project will be considered a success if we are able to check off all the items in the checklist. Partial crdit may be given in accordance to how many items we were able to check off the checklist. Some additional measures off sucess are:

- [X] View robot models in gazebo with appropriate colors.
- [X] Show the camera view of the Robber.
- [X] Demonstarte that the Copbot autonomously follows the robber in mode 1.
- [X] Hvae classmates follow the steps in the README to sucessfully run the simulation without any help.
