#! /usr/bin/env python

from gazebo_msgs.srv import GetModelState
import rospy, time, numpy

class Position:

    def __init__(self):
		rospy.init_node('show_gazebo_models')
		self.state = 1
		print ('\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n Make your way to the gold!')
		
    def show_gazebo_models(self):
		model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
		while not rospy.is_shutdown():
			robot1pose = model_coordinates('Robot1', "")
			robot2pose = model_coordinates('Robot2', "")
			self.rate = rospy.Rate(1)
			if self.state == 1:
				if  ((1 < robot1pose.pose.position.x < 3) and (0 < robot1pose.pose.position.y < 2)) or ((21 < robot1pose.pose.position.x < 23) and (13 < robot1pose.pose.position.y < 15)):
					print('\n \n \n \n \n \n Youve got the gold! Make your way to the exit!')
					self.state = 2
				if (abs(robot1pose.pose.position.x - robot2pose.pose.position.x) <= .5) or (abs(robot1pose.pose.position.y - robot2pose.pose.position.y) <= .5):
					print('\n \n \n \n \n \n Youve been caught! You Lose! Game Over!')
					self.state = 3
			if self.state == 2:
				if ((13 < robot1pose.pose.position.x < 15) and (-3 < robot1pose.pose.position.y < 0)) or ((13 < robot1pose.pose.position.x < 15) and (14 < robot1pose.pose.position.y < 16)):
					print('\n \n \n \n \n \n You win! Game Over!')
					self.state = 3
				if (abs(robot1pose.pose.position.x - robot2pose.pose.position.x) <= .5) or (abs(robot1pose.pose.position.y - robot2pose.pose.position.y) <= .5):
					print('\n \n \n \n \n \n Youve been caught! You Lose! Game Over!')
					self.state = 3
			self.rate.sleep()   
            
if __name__ == '__main__':
    pose = Position()
    pose.show_gazebo_models()
