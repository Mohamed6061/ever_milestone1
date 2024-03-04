#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

rospy.init_node("cmd_vel")

publisher = rospy.Publisher("/cmd_vel", Float64, queue_size=1)
publisher2 = rospy.Publisher("/brakes", Float64, queue_size=1)
publisher3 = rospy.Publisher("/SteeringAngle", Float64, queue_size=1)

m = 1
n = 0
line1=1
line2=1
f=1
f2=1
flag=1
if __name__ == "__main__":
    start_time = rospy.get_time()
    while not rospy.is_shutdown():
        time1=rospy.get_time() + 7
        #move in stright line for 75m
        while(line1):
            Steering = Float64()
            Steering.data = 0
            publisher3.publish(Steering)
            rospy.sleep(.1)
            ThrottleHigh = Float64()
            ThrottleHigh.data = .6
            ThrottleLow = Float64()
            ThrottleLow.data = 0
            publisher.publish(ThrottleHigh)
            #stop
            if time1 <= rospy.get_time():
                line1=0
                publisher.publish(ThrottleLow)
                publisher2.publish(.5)
                message1 = Float64()
                message1.data = .5
                publisher2.publish(message1)
                rospy.loginfo("finish stright-line")

                break
        rospy.sleep(1)
        time4=rospy.get_time()+ .2
        #stop
        while time4>rospy.get_time():
            message1 = Float64()
            message1.data = 1
            publisher2.publish(message1)
        #break off //move
        
        message1.data = 0
        publisher2.publish(message1)
        publisher2.publish(message1)
        time2=rospy.get_time()+ .3
        #move 30 degree
        if f:
            while time2>rospy.get_time():
                # rospy.loginfo(n)
                publisher.publish(ThrottleHigh)
                Steering.data = 30
                publisher3.publish(Steering)
                # n=n+1
                f=0
            #steering stright
            publisher.publish(ThrottleLow)
            Steering.data = 0
            publisher3.publish(Steering)
            rospy.loginfo("finish 30D")
            rospy.sleep(.5)


        time3=rospy.get_time()+ 2
        #break
        while time3>rospy.get_time():
            message1 = Float64()
            message1.data = 1
            publisher2.publish(message1)
        #break off
        message1 = Float64()
        message1.data = 0
        publisher2.publish(message1)
        publisher2.publish(message1)

        time5=rospy.get_time()+ .4
        #steering -25 to make the car move stright
        if f2:
            while time5>rospy.get_time():
                # rospy.loginfo(n)
                publisher.publish(ThrottleHigh)
                Steering.data = -40
                publisher3.publish(Steering)
                # n=n+1
                f2=0
            publisher.publish(ThrottleLow)
            Steering.data = 0
            publisher3.publish(Steering)
            rospy.loginfo("finish -25D")
            rospy.sleep(.5)

        time9=rospy.get_time() + 5
        #move in stright line
        while(line2):
            Steering = Float64()
            Steering.data = 0
            publisher3.publish(Steering)
            rospy.sleep(.1)
            ThrottleHigh = Float64()
            ThrottleHigh.data = .6
            ThrottleLow = Float64()
            ThrottleLow.data = 0
            publisher.publish(ThrottleHigh)
            
            if time9 <= rospy.get_time():
                line2=0
                publisher.publish(ThrottleLow)
                publisher2.publish(.5)
                message1 = Float64()
                message1.data = .5
                publisher2.publish(message1)
                rospy.loginfo(m)
                break
        break