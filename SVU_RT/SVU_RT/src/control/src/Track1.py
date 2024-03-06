#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

rospy.init_node("Track1")

publisher = rospy.Publisher("/cmd_vel", Float64, queue_size=1)
publisher2 = rospy.Publisher("/brakes", Float64, queue_size=1)

if __name__ == "__main__":
    start_time = rospy.get_time()
    while not rospy.is_shutdown():
        rospy.sleep(.1)
        ThrottleHigh = Float64()
        ThrottleHigh.data = .7
        ThrottleLow = Float64()
        ThrottleLow.data = 0
        publisher.publish(ThrottleHigh)
        if rospy.get_time()-start_time > 7.7:
            publisher.publish(ThrottleLow)
            time1=rospy.get_time() + 1
            while time1>rospy.get_time():
                Brake = Float64()
                Brake.data = 1
                publisher2.publish(Brake)
            break
        
