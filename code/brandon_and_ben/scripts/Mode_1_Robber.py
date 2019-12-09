#! /usr/bin/env python

from gazebo_msgs.srv import GetModelState
import rospy, time, numpy, cv2, cv_bridge
from sensor_msgs.msg import Image

class Finder:
	def __init__(self):
		self.bridge = cv_bridge.CvBridge()
		cv2.namedWindow("window", 1)
		self.image_sub = rospy.Subscriber('/robot1/camera/rgb/image_raw', Image, self.image_callback)
		self.state = 1
		print ('\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n Make your way to the gold!')
		
	def image_callback(self, msg):
		model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
		robot1pose = model_coordinates('Robot1', "")
		robot2pose = model_coordinates('Robot2', "")
		if self.state == 1:
			if  ((-9.5 < robot1pose.pose.position.x < -6.5) and (-9.5 < robot1pose.pose.position.y < -6.5)) or ((6.5 < robot1pose.pose.position.x < 9.5) and (6.5 < robot1pose.pose.position.y < 9.5)):
				print('\n \n \n \n \n \n Youve got the gold! Make your way to the exit!')
				self.state = 2
			if (abs(robot1pose.pose.position.x - robot2pose.pose.position.x) <= .5) and (abs(robot1pose.pose.position.y - robot2pose.pose.position.y) <= .5):
				print('\n \n \n \n \n \n Youve been caught! You Lose! Game Over!')
				self.state = 3
		if self.state == 2:
			if ((-.5 < robot1pose.pose.position.x < .5) and (-9.5 < robot1pose.pose.position.y < -12.5)) or ((-.5 < robot1pose.pose.position.x < .5) and (9.5 < robot1pose.pose.position.y < 12.5)):
				print('\n \n \n \n \n \n You win! Game Over!')
				self.state = 3
			if (abs(robot1pose.pose.position.x - robot2pose.pose.position.x) <= .5) and (abs(robot1pose.pose.position.y - robot2pose.pose.position.y) <= .5):
				print('\n \n \n \n \n \n Youve been caught! You Lose! Game Over!')
				self.state = 3
		image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
		cv2.imshow("window", image)
		cv2.waitKey(3)
	
rospy.init_node('finder')
finder = Finder()
rospy.spin()
