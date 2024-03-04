#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

if __name__ == '__main__':
    rospy.init_node('cmd_vel_publisher', anonymous=True)
    rate = rospy.Rate(10)  # Set the loop rate to 10 Hz
    steering_pub = rospy.Publisher('/SteeringAngle', Float64, queue_size=10)
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Float64, queue_size=10)

    timer = rospy.get_time()

    while not rospy.is_shutdown():
        steering_angle = 18
        gas_pedal_force = .2
        cmd_vel_pub.publish(gas_pedal_force)
        steering_pub.publish(steering_angle)
        rospy.loginfo("Publishing Steering Angle: %.2f", steering_angle)
        rospy.loginfo("Publishing Gas Pedal Force: %.2f", gas_pedal_force)

        rate.sleep()
