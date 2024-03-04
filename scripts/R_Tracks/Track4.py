#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

rospy.init_node("cmd_vel")

publisher = rospy.Publisher("/cmd_vel", Float64, queue_size=1)
publisher2 = rospy.Publisher("/SteeringAngle", Float64, queue_size=1)
publisher3 = rospy.Publisher("/brakes", Float64, queue_size=1)


f=0
first_cycle=1
second_cycle=1

if __name__ == "__main__":
    start_time = rospy.get_time()
    while not rospy.is_shutdown():
            while(first_cycle):
                Steering = Float64()
                Steering.data = 18
                publisher2.publish(Steering)
                messageHigh = Float64()
                messageHigh.data = .2
                messageLow = Float64()
                messageLow.data = 0
                # message2=Float64()
                # message2.data=0.0
                publisher.publish(messageHigh)
                rospy.sleep(.1)
                # publisher.publish(message2)
                # rospy.sleep(3)
                if rospy.get_time() -start_time >11:
                    publisher.publish(messageLow)
                    publisher3.publish(.3)
                    rospy.loginfo(f"Message sent to /cmd_vel: {messageHigh.data}")
                    first_cycle=0
                    rospy.sleep(1)
            publisher3.publish(0)
            while(second_cycle):
                Steering = Float64()
                Steering.data = -18
                publisher2.publish(Steering)
                messageHigh = Float64()
                messageHigh.data = .2
                messageLow = Float64()
                messageLow.data = 0
                # message2=Float64()
                # message2.data=0.0
                publisher.publish(messageHigh)
                rospy.sleep(.1)
                if rospy.get_time() -start_time >21:
                    publisher.publish(messageLow)
                    publisher3.publish(.3)
                    rospy.loginfo(f"Message sent to /cmd_vel: {messageLow.data}")
                    rospy.sleep(.2)
                    break
            break

            
        
