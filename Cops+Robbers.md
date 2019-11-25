# IE482-Project - Cops and Robbers

---

## Intro
The inspiration to this project is the childrens game known as cops and robbers. Inside of Gazebo we plan to simulate a total of 4 Turtlebots. One Patrolbot called the "Copbot" will survey an area in search of a criminal. There will two wanderbots perceived as "civilians" that will casually roam the generated world. Finally there will be a followbot known to be the "Robber" that will navigate a specific path in an attempt to steal a precious cargo all while avoiding the protrolling officer. If the robber is seen by a civilian, that civilian will flee in fear and immediate locate the officer. The copbot will then race to the scene in pursuit of the criminal now with both civilians as back up. The simulation will end once the copbot and the two civilians are within proximity and surround the robber or when the robber has successfully stole the precious cargo. 


## Project Function

There will be a floorplan laid out in gazebo where a wanderbot will patrol the area (copbot). There will be three other wanderbots, two of which are civilians and one of which is a criminal. If one of the civilians is the first to spot the criminal, they will alert the copbot by navigating to the copbot and sending the location of where they last saw the criminal. If the copbot sees the criminal first, he will follow the criminal and immediately alert the civilians by sending a continuous update of the criminal’s location. The civilians will then migrate towards the criminal and when both the civilians and copbot have a visual on the criminal the task will be complete. The criminal escaping will also end the simulation.


## Project Schedule
### Week 1 (10/25 - 11/1)(COMPLETE)
---
-  Generate Gazebo world/track for Cop and Robbers simulator 

### Week 2 (11/1 - 11/8)(COMPLETE)
--- 
- Be able to manually move Turtlebot with great accuracy (As if video game)
	- Try integrating video game controller

### Week 3 + Week 4(11/8 - 11/22)(COMPLETE)
--- 
- Populate world with both Turtlebots:
	- Create new but identical messages and topics so that both bots dont read off the same nodes
	- Get both bots to recognize each others color "skin" : Cop = Blue and Robber = Red

### Week 5 + Week 6(11/22 - 12/06) (In Progress)
---
- Turtlebot logic implementation: 
	- Copbot: Patrol world using a FSM 
	- Robber: Be able to follow given Followbot path
	- Simulation ends when Copbot is within ~3m of Robber
	- Once Cop sees Robber apply followbot code to tailgate Robber
	
### Week 7 (12/06 - 12/13)
---
- Turn the simulation into a video game
	- Player 1 controls the cop	(In Progress)
	- Player 2 controls the robber	(In Progress)
	- Create lives and a point system. 
