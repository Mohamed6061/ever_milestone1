#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

rospy.init_node("cmd_vel")

publisher = rospy.Publisher("/cmd_vel", Float64, queue_size=1)
publisher2 = rospy.Publisher("/brakes", Float64, queue_size=1)


m = 0
n = 0

if __name__ == "__main__":
    start_time = rospy.get_time()
    while not rospy.is_shutdown():
        rospy.sleep(.1)
        ThrottleHigh = Float64()
        ThrottleHigh.data = .7
        ThrottleLow = Float64()
        ThrottleLow.data = 0
        publisher.publish(ThrottleHigh)
        rospy.loginfo("high %f", rospy.get_time())
        if rospy.get_time()-start_time > 7.3:
            publisher.publish(ThrottleLow)
            # publisher2.publish(1)
            time1=rospy.get_time() + 1
            while time1>rospy.get_time():
                message1 = Float64()
                message1.data = 1
                publisher2.publish(message1)
            break
        
