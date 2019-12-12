#!/usr/bin/env python

import rospy, cv2, cv_bridge, random, time
import numpy as np
from sensor_msgs.msg import Image, LaserScan
from gazebo_msgs.srv import GetModelState
from geometry_msgs.msg import Twist
import math

class Follower:
	def __init__(self):
		self.bridge = cv_bridge.CvBridge()
		cv2.namedWindow("window", 1)
		self.image_sub = rospy.Subscriber('/robot2/camera/rgb/image_raw', Image, self.image_callback)
		self.scan_sub = rospy.Subscriber('/robot2/scan', LaserScan, self.scan_callback) 
		self.cmd_vel_pub = rospy.Publisher('/robot2/cmd_vel_mux/input/teleop', Twist, queue_size=1)
		self.twist = Twist()
		self.state_robot = 1
		self.state = 1
		self.state_change_time_one = rospy.Time.now() + rospy.Duration(5)
		self.state_change_time_two = rospy.Time.now()
		self.random_int = random.randint(1,2)
		self.left_turn = False
		self.right_turn = False



		# ============================================================================
		# EDIT THESE VALUES AS NECESSARY:
		# ============================================================================
		# Red Mask
		self.lower_red = np.array([  0, 220,  50]) 
		self.upper_red = np.array([  0, 255, 255])

		self.goal_radius = 50		# [pixels]
		self.goal_area   = 255 * math.pi * self.goal_radius ** 2		# [sum of pixel values]
		
		#Using Moments
		
		self.maxSpeed = 1		# [m/s].  Maximum speed of our robot.
		# ============================================================================

		
		# Initialize our rotation direction.  -1 --> CW, 1 --> CCW
		self.rotationDir = -1
		
	def image_callback(self, msg):
		
		image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')	
		
		h, w, d = image.shape

		model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
		robot1pose = model_coordinates('Robot1', "")
		robot2pose = model_coordinates('Robot2', "")
		if self.state == 1:
			if  ((.5 < robot1pose.pose.position.x < 3.5) and (-.5 < robot1pose.pose.position.y < 2.5)) or ((20.5 < robot1pose.pose.position.x < 23.5) and (12.5 < robot1pose.pose.position.y < 15.5)):
				print('\n \n \n \n \n \n The criminal has the gold! Stop him from getting to the exit!')
				self.state = 2
			if (abs(robot1pose.pose.position.x - robot2pose.pose.position.x) <= .5) and (abs(robot1pose.pose.position.y - robot2pose.pose.position.y) <= .5):
				print('\n \n \n \n \n \n You caught the criminal! You Win! Game Over!')
				self.state = 3
		if self.state == 2:
			if ((12.5 < robot1pose.pose.position.x < 13.5) and (-2.5 < robot1pose.pose.position.y < -.5)) or ((12.5 < robot1pose.pose.position.x < 13.5) and (15.5 < robot1pose.pose.position.y < 17.5)):
				print('\n \n \n \n \n \n The criminal escaped! You lose! Game Over!')
				self.state = 3
			if (abs(robot1pose.pose.position.x - robot2pose.pose.position.x) <= .5) and (abs(robot1pose.pose.position.y - robot2pose.pose.position.y) <= .5):
				print('\n \n \n \n \n \n You caught the criminal! You Win! Game Over!')
				self.state = 3
		image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
		cv2.imshow("window", image)
		cv2.waitKey(3)
		
		# Define the range (rows) for our mask:
		search_top = 0
		search_bot = 3*h/4 + 20
				
		(x, y) = (None, None)
		area = None
		radius = None

		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

		red_mask = cv2.inRange(hsv, self.lower_red, self.upper_red)
		red_mask[0:search_top, 0:w] = 0
		red_mask[search_bot:h, 0:w] = 0		

		M = cv2.moments(red_mask)
		if M['m00'] > 0:
			x = int(M['m10']/M['m00'])
			y = int(M['m01']/M['m00'])
			
			calcRadius   = int(math.sqrt(M['m00'] / (255 * math.pi)))
			cv2.circle(image, (x, y), calcRadius, (200, 255, 200), 2)
			cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

			area = int(M['m00'])

		# Move the robot.
		# NOTE:  This method uses the AREA of a circle.
		self.moveMe(x, w, self.goal_area, area)
		
		if (x is not None):
			# Print a blue circle on the image, showing the goal radius
			cv2.circle(image, (x, y), int(self.goal_radius), (255, 0, 0), 2)
			
		#cv2.imshow("window", image)
		#cv2.waitKey(3)

	def moveMe(self, x, w, goal, observed):
		if (x == None):
			if self.state_robot == 2:
			# We lost sight of the ball.
			# Stop linear movement / Start rotating.
				self.twist.linear.x = 0.0 
				self.twist.angular.z = self.rotationDir * math.pi / 8	# FIXME -- Scaling by Pi/8 is arbitrary.
				if rospy.Time.now() >= self.state_change_time_two:
					# Stop rotating / Start Wandering
					self.state_robot = 1
		else:
			# We found the ball.
			self.state_robot = 2
			self.state_change_time_two = rospy.Time.now() + rospy.Duration(10)
			# Rotation
			errRotate = x - w/2
			thetaRad = math.atan(errRotate/1024.0)		# FIXME -- Dividing by 1024 is arbitrary
			self.twist.angular.z = -thetaRad
	
			# Keep track of our direction of rotation.
			# We'll use this direction if we lose sight of the ball.
			if (thetaRad > 0):
				self.rotationDir = -1
			else:
				self.rotationDir =  1
			
			# Set our linear speed and direction
			# NOTE:  The "goal" value could be an AREA or a RADIUS.
			#        The "observed" value should be in the same units.
			errLinear = goal - observed
			rateLinear = errLinear / float(goal)		
			self.twist.linear.x = self.maxSpeed * rateLinear 
			
			#print errRotate, rateLinear

		self.cmd_vel_pub.publish(self.twist)
			
	def scan_callback(self, scan_msg):
		if self.state_robot == 1:
			self.g_range_ahead_right = max(scan_msg.ranges[0:len(scan_msg.ranges)/2])
			self.g_range_ahead_left = max(scan_msg.ranges[len(scan_msg.ranges)/2:len(scan_msg.ranges)])
			is_right_nan = np.isnan(self.g_range_ahead_right)
			is_left_nan = np.isnan(self.g_range_ahead_left)
			if self.state == 1:
				if rospy.Time.now() <= self.state_change_time_one:
					if self.random_int == 1:
						#right turning
						self.twist.linear.x = 1.5
						self.twist.angular.z = -.3
					if self.random_int == 2:
						#left_turning
						self.twist.linear.x = 1.5
						self.twist.angular.z = .3

				else:
					self.state = 2
					if self.random_int == 1:
						self.right_turn = False
						self.left_turn = True
					if self.random_int == 2:
						self.left_turn = False
						self.right_turn = True

			if self.state == 2:
				if is_right_nan == True and is_left_nan == False:
					#right turning here
					self.twist.linear.x = 1
					self.twist.angular.z = -.3
					self.right_turn = True
					self.left_turn = False
				elif is_right_nan == False and is_left_nan == True:
					#left turning here
					self.twist.linear.x = 1
					self.twist.angular.z = .3
					self.right_turn = False
					self.left_turn = True
				elif is_right_nan == False and is_right_nan == False:
					if self.g_range_ahead_right > self.g_range_ahead_left:
						#turn right here
						err_right = 6 - self.g_range_ahead_right
						self.twist.linear.x = self.g_range_ahead_right / 5.6
						self.twist.angular.z = -err_right * 1.15
						self.right_turn = True
						self.left_turn = False
					if self.g_range_ahead_right < self.g_range_ahead_left:
						#turn left here
						err_left = 6 - self.g_range_ahead_left
						self.twist.linear.x = self.g_range_ahead_left / 5.6
						self.twist.angular.z = err_left * 1.15
						self.right_turn = False
						self.left_turn = True
				else:
					if self.right_turn == True and self.left_turn == False:
						#turn right here
						self.twist.linear.x = 1
						self.twist.angular.z = -.3
					if self.left_turn == True and self.right_turn == False:
						#turn left here
						self.twist.linear.x = 1
						self.twist.angular.z = .3

		#print "range ahead right", self.g_range_ahead_right
		#print "range ahead left", self.g_range_ahead_left
		self.cmd_vel_pub.publish(self.twist)


rospy.init_node('robberfollower')
follower = Follower()
rospy.spin()
