#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

# ------------------------Newten---------------------------------#
if __name__ == '__main__':
    rospy.init_node('cmd_vel_publisher', anonymous=True)
    rate = rospy.Rate(10)  # Set the loop rate to 10 Hz

    cmd_vel_pub = rospy.Publisher('/cmd_vel', Float64, queue_size=10)
    break_pub = rospy.Publisher('/brakes', Float64, queue_size=10)

    timer = rospy.get_time()

    while not rospy.is_shutdown():
        current_time = rospy.get_time()
        elapsed_time = current_time - timer

        if elapsed_time < 7:
            gas_pedal_force = .8
            rospy.loginfo("Publishing Gas Pedal Force: %.2f", gas_pedal_force)
            cmd_vel_pub.publish(gas_pedal_force)
        else:
            cmd_vel_pub.publish(0)
            break_force = 1
            break_pub.publish(break_force)
            rospy.loginfo("Publishing Brake Force: %.2f", break_force)

        rate.sleep()