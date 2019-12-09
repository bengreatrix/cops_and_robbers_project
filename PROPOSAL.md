*NOTE TO STUDENTS:  This is a template for your **proposal**.  Items wrapped inside `{}` should be replaced accordingly.*

*You will have 5 minutes to present your proposal document on Friday, Oct. 25.*

**Please delete this line, and the comments above.**

--- 

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

A modified version of the turtlbotrace scripts will be used to launch the gazebo worlds with multiple Turtlebots. The Copbot will wander the area with a modified version of the wander.py script from chapter 7. The Copbot will know when it has seen the Robber and follow it with a modified version of the move_robot.py script from the 09_redball_code repositiry. The Turtlebots will be controlled using a modified version of the keyboard_teleop launch file and they will be networked using .............


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
- [ ] Submit final presentation  *Due Dec. 16*


## Measures of Success
The project will be considered a success if we are able to check off all the items in the checklist. Partial crdit may be given in accordance to how many items we were able to check off the checklist. Some additional measures off sucess are:

- [] View robot models in gazebo with appropriate colors.
- [] Show the camera view of the Robber.
- [] Demonstarte that the Copbot autonomously follows the robber in mode 1.
- [] Hvae classmates follow the steps in the README to sucessfully run the simulation without any help.

---
**A Sample Proposal Appears Below**
---

# Creating a Gazebo Model of the Duckiebot

Team Members:
- Chase Murray, cmurray3@buffalo.edu
- Jane Student, j@buffalo.edu


## Project Objective
The goal of this project is to create a Gazebo model of the Duckiebot. This model will accurately reflect the dimensions of the Duckiebot, will include the Duckiebot's sensors (a fisheye lens camera and a magnetometer), and will have the same drive train (two motors controlling the two motorized wheels).


## Contributions
There are currently no Gazebo models of this robot.  By creating such a model, we will be able to test control algorithms in a simulated environment (without the need for the physical robot itself).  However, after training the control algorithms in Gazebo, it will be easy to execute them on a real Duckiebot, since the simulated version will be an accurate representation.


## Project Plan
The textbook contains two chapters (Chapters 15--17) that describe how to build a custom robot.
However, these chapters do not discuss the use of a fisheye lens.  We will use the ros.org Website to learn how to model such cameras.
We will also consult the Duckiebot specs to determine the dimensions and weight of the robot, as well as the capabilities of the motors.


## Milestones/Schedule Checklist
- [x] Complete this proposal document.  *Due Oct. 25*
- [ ] Capture the specs of the actual/physical robot.  *JS, Nov. 16*
- [ ] Build a sample model using the textbook examples. *CM, Nov. 16*
- [ ] Modify the sample model to match the specs of the Duckiebot.  *CM, Nov. 19*
- [ ] Add a fisheye lens camera. *JS, Nov. 20*
- [ ] Create progress report.  *Due Nov. 25*
- [ ] Create Gazebo .launch files to test the robot.  *CM, Dec. 1*
- [ ] Create a simple controller to test the interaction with the robot. *JS, Dec. 3*
- [ ] Create final presentation.  *Due Dec. 5*
- [ ] Update documentation based on presentation feedback. *CM, Dec. 7*
- [ ] Provide system documentation (README.md).  *Due Dec. 13*


## Measures of Success
- [ ] View robot model in Gazebo.
- [ ] Demonstrate that the fisheye lens camera is appropriately distorted.
- [ ] Demonstrate that robot moves when given commands.
- [ ] Implement code on a real Duckiebot.
- [ ] Have a classmate follow the steps in the README to successfully run the simulation without any help.


