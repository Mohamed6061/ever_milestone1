#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

rospy.init_node("cmd_vel")

publisher = rospy.Publisher("/cmd_vel", Float64, queue_size=1)
publisher2 = rospy.Publisher("/SteeringAngle", Float64, queue_size=1)
publisher3 = rospy.Publisher("/brakes", Float64, queue_size=1)


f=0

if __name__ == "__main__":
    start_time = rospy.get_time()
    while not rospy.is_shutdown():
            Steering = Float64()
            Steering.data = 18
            publisher2.publish(Steering)
            messageHigh = Float64()
            messageHigh.data = .2
            messageLow = Float64()
            messageLow.data = 0
            publisher.publish(messageHigh)
            rospy.sleep(.1)
            if rospy.get_time() -start_time >10:
                publisher.publish(messageLow)
                publisher3.publish(.3)
                # rospy.loginfo(f"Message sent to /cmd_vel: {messageHigh.data}")
                break
            
        
