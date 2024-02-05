#!/usr/bin/env python3

import rospy
import tf
from geometry_msgs.msg import TransformStamped
from math import radians

rospy.init_node('change_yaw_node', anonymous=True)

def change_yaw_angle():
    rate = rospy.Rate(30)  # 1 Hz
    z=0
    # Create a TF broadcaster
    tf_broadcaster = tf.TransformBroadcaster()
    yaw_angle_degrees=0
    sign=1
    while not rospy.is_shutdown():
        # Set the fixed frame and child frame
        fixed_frame = "fix_link"  # Replace with your fixed frame ID
        child_frame = "base_link"  # Replace with your model frame ID
        
        
        # Set the desired yaw angle in radians
        if (sign ):
            yaw_angle_degrees =yaw_angle_degrees+10
        if yaw_angle_degrees ==360 :
            sign=0
        if yaw_angle_degrees ==0 :
            sign=1
        if (sign ==0):
            yaw_angle_degrees =yaw_angle_degrees-10    
        
        print(yaw_angle_degrees%360)   # Change this to your desired yaw angle
        yaw_angle_radians = radians(yaw_angle_degrees)
        
               # Set the translation (assuming no translation)
        translation = (0, 0, 0)
        print(z)

        # Set the orientation to achieve the desired yaw angle
        quaternion = tf.transformations.quaternion_from_euler(0,yaw_angle_radians ,yaw_angle_radians)

        # Publish the TransformStamped message
        tf_broadcaster.sendTransform(translation, quaternion, rospy.Time.now(), child_frame, fixed_frame)
        #print("donnee")
        rate.sleep()

if __name__ == '__main__':
    change_yaw_angle()
