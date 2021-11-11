#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
import time

rospy.init_node('by_path', anonymous=True)
path_pub = rospy.Publisher('trajectory', Path, queue_size = 10)
pose_pub = rospy.Publisher('pose', PoseStamped, queue_size = 10)
rate = rospy.Rate(1)
hehe = False
def run():
	global hehe	
	abc = True
	a = -0.01
	b = 0.01
	y = -0.2
	z = 0.2
	j = 0
	seq = 0
	path = Path()
	path.header.stamp = rospy.Time.now()
	path.header.frame_id="base_link"
	for i in range(40):
		if(abc):
			y += a
			if (i >= 39):
				hehe = True
			if hehe:
				time.sleep(1)
			if (y >= -0.2 or y <= -0.3):
				a *= -1
				abc = False		
		else:
			z += b
			if (i >= 39):
				hehe = True
			if hehe:
				time.sleep(1)
				
			if (z >= 0.3 or z <= 0.2):
				b *= -1
				abc = True
		if (y <= -0.3):
			y = -0.3
		elif (y >= -0.2):
			y = -0.2
		if (z >= 0.3):
			z = 0.3
		elif (z <= 0.2):
			z = 0.2
			
		poseSt = PoseStamped()	
		poseSt.header.stamp = rospy.Time.now()
		poseSt.header.frame_id="base_link"
		poseSt.header.seq = seq
		poseSt.pose.position.x = 0.4
		poseSt.pose.position.y = y
		poseSt.pose.position.z = z
		poseSt.pose.orientation.x = 0
		poseSt.pose.orientation.y = 0
		poseSt.pose.orientation.z = 0
		poseSt.pose.orientation.w = 1
		rospy.loginfo(poseSt)
		pose_pub.publish(poseSt)
		

		path.poses.append(poseSt)
	rospy.loginfo(path)
	seq +=1
	print("====================")
	path_pub.publish(path)
	rate.sleep()
			
if __name__ == '__main__':
	while not rospy.is_shutdown():
		run()
		
