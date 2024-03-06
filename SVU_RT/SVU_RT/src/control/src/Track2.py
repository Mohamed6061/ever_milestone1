#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

rospy.init_node("Track2")

publisher = rospy.Publisher("/cmd_vel", Float64, queue_size=1)
publisher2 = rospy.Publisher("/SteeringAngle", Float64, queue_size=1)
publisher3 = rospy.Publisher("/brakes", Float64, queue_size=1)


f=0

if __name__ == "__main__":
    start_time = rospy.get_time()
    while not rospy.is_shutdown():
            Steering = Float64()
            Steering.data = 21
            publisher2.publish(Steering)
            messageHigh = Float64()
            messageHigh.data = .2
            messageLow = Float64()
            messageLow.data = 0
            publisher.publish(messageHigh)
            rospy.sleep(.1)
            if rospy.get_time() -start_time >9:
                publisher.publish(messageLow)
                publisher3.publish(.3)
                break
            
        
