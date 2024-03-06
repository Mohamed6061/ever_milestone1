#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

rospy.init_node("Track4")

Throttle = rospy.Publisher("/cmd_vel", Float64, queue_size=1)
SteeringAngle = rospy.Publisher("/SteeringAngle", Float64, queue_size=1)
Brakes = rospy.Publisher("/brakes", Float64, queue_size=1)


first_cycle=1
second_cycle=1

if __name__ == "__main__":
    start_time = rospy.get_time()
    while not rospy.is_shutdown():
            #First circle
            while(first_cycle):
                Steering = Float64()
                Steering.data = 21
                SteeringAngle.publish(Steering)
                ThrottleHigh = Float64()
                ThrottleHigh.data = .2
                ThrottleLow = Float64()
                ThrottleLow.data = 0
                Throttle.publish(ThrottleHigh)
                rospy.sleep(.1)
                if rospy.get_time() -start_time >9:
                    Throttle.publish(ThrottleLow)
                    Brakes.publish(.3)
                    first_cycle=0
                    rospy.sleep(1)

            rospy.loginfo("First Circle Done")

            #Brake OFF
            Brakes.publish(0)

            #Second Circle
            while(second_cycle):
                Steering = Float64()
                Steering.data = -21
                SteeringAngle.publish(Steering)
                ThrottleHigh = Float64()
                ThrottleHigh.data = .2
                ThrottleLow = Float64()
                ThrottleLow.data = 0
                Throttle.publish(ThrottleHigh)
                rospy.sleep(.1)
                if rospy.get_time() -start_time >17.4:
                    Throttle.publish(ThrottleLow)
                    Brakes.publish(.3)
                    rospy.sleep(.2)
                    break
            rospy.loginfo("Second Circle Done")
            break

            
        
