#!/usr/bin/env python3
 
import rospy
from std_msgs.msg import Float64

rospy.init_node('Track3', anonymous=True)
rate = rospy.Rate(10)  # Set the loop rate to 10 Hz

Throttle = rospy.Publisher("/cmd_vel", Float64, queue_size=1)
Brakes = rospy.Publisher("/brakes", Float64, queue_size=1)
SteeringAngle = rospy.Publisher("/SteeringAngle", Float64, queue_size=1)
Steering = Float64()
Steering.data = 0
ThrottleHigh = Float64()
ThrottleLow = Float64()
stop = Float64()

timer = rospy.get_time()
if __name__ == '__main__':
    while not rospy.is_shutdown():
        current_time = rospy.get_time()
        elapsed_time = current_time - timer

        #move in stright line for 75m
        if elapsed_time < 11.5 :
            ThrottleHigh.data = .3
            Throttle.publish(ThrottleHigh)
            rospy.loginfo("Start moving with spped 0.6")

        # turn 
        elif elapsed_time > 11.5 and elapsed_time < 12.1 :
            ThrottleHigh.data = .2
            Throttle.publish(ThrottleHigh)
            Steering.data = 30
            SteeringAngle.publish(Steering)
            rospy.loginfo("turnung Car")

        #steering -30 to make the car move stright
        elif elapsed_time > 12.1 and elapsed_time < 13.3:
                ThrottleHigh.data = .2
                Throttle.publish(ThrottleHigh)
                Steering.data = -30
                SteeringAngle.publish(Steering)
                rospy.loginfo("truning opp Car")

        #move in stright line
        elif elapsed_time >= 13.3 and elapsed_time < 20.5:
            Steering.data = 0
            SteeringAngle.publish(Steering)
            ThrottleHigh.data = .3
            Throttle.publish(ThrottleHigh)
            rospy.loginfo("go other path Car")

        # stop
        elif elapsed_time > 21 :
            ThrottleLow.data = 0
            Throttle.publish(ThrottleLow)
            stop.data = 0.5
            Brakes.publish(stop)
            rospy.loginfo("stopped Car")
            break
    rate = rospy.Rate(10)
