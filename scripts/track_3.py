#!/usr/bin/env python3
 
import rospy
from std_msgs.msg import Float64

rospy.init_node('cmd_vel_publisher', anonymous=True)
rate = rospy.Rate(10)  # Set the loop rate to 10 Hz

publisher = rospy.Publisher("/cmd_vel", Float64, queue_size=1)
publisher2 = rospy.Publisher("/brakes", Float64, queue_size=1)
publisher3 = rospy.Publisher("/SteeringAngle", Float64, queue_size=1)
Steering = Float64()
Steering.data = 0
ThrottleHigh = Float64()
stop = Float64()

timer = rospy.get_time()
if __name__ == '__main__':
    while not rospy.is_shutdown():
        current_time = rospy.get_time()
        elapsed_time = current_time - timer

        #move in stright line for 75m
        if elapsed_time < 11.5 :
            ThrottleHigh.data = .3
            publisher.publish(ThrottleHigh)
            rospy.loginfo("Start moving with spped 0.6")

        # turn 
        elif elapsed_time > 11.5 and elapsed_time < 12.1 :
            ThrottleHigh.data = .2
            publisher.publish(ThrottleHigh)
            Steering.data = 30
            publisher3.publish(Steering)
            rospy.loginfo("turnung Car")

        #steering -25 to make the car move stright
        elif elapsed_time > 12.1 and elapsed_time < 13.3:
                ThrottleHigh.data = .2
                publisher.publish(ThrottleHigh)
                Steering.data = -30
                publisher3.publish(Steering)
                rospy.loginfo("truning opp Car")

        #move in stright line
        elif elapsed_time >= 13.3 and elapsed_time < 20.5:
            Steering.data = 0
            publisher3.publish(Steering)
            ThrottleHigh.data = .3
            publisher.publish(ThrottleHigh)
            rospy.loginfo("go other path Car")

        # stop
        elif elapsed_time > 21 :
            ThrottleHigh.data = 0
            publisher.publish(0)
            stop.data = 0.5
            publisher2.publish(stop)
            rospy.loginfo("stopped Car")
            break
    rate = rospy.Rate(10)


# if __name__ == '__main__':
#     while not rospy.is_shutdown():
#         current_time = rospy.get_time()
#         elapsed_time = current_time - timer

#         #move in stright line for 75m
#         if elapsed_time < 9:
#             rospy.sleep(.1)
#             ThrottleHigh.data = .6
#             publisher.publish(ThrottleHigh)
#             rospy.loginfo("Start moving with spped 0.6")

#         # turn 
#         elif elapsed_time > 9 and elapsed_time < 9.5 :
#             ThrottleHigh.data = .4
#             publisher.publish(ThrottleHigh)
#             Steering.data = 30
#             publisher3.publish(Steering)
#             rospy.loginfo("turnung Car")

#         #steering -25 to make the car move stright
#         elif elapsed_time > 9.5 and elapsed_time < 10.2:
#                 ThrottleHigh.data = .4
#                 publisher.publish(ThrottleHigh)
#                 Steering.data = -30
#                 publisher3.publish(Steering)
#                 rospy.loginfo("truning opp Car")
        
#         #move in stright line
#         elif elapsed_time >= 10 and elapsed_time < 11:
#             Steering.data = 0
#             publisher3.publish(Steering)
#             ThrottleHigh.data = .6
#             publisher.publish(ThrottleHigh)
#             rospy.loginfo("go other path Car")
        
#         # stop
#         elif elapsed_time > 12 :
#             ThrottleHigh.data = 0
#             publisher.publish(0)
#             stop.data = 0.5
#             publisher2.publish(stop)
#             rospy.loginfo("stopped Car")
#             break
#     rate = rospy.Rate(10)