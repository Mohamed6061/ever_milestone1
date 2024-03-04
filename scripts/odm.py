#!/usr/bin/env python3

# import rospy
# from nav_msgs.msg import Odometry
# import csv
# import os
 
# # Print the current working directory
# print("Current Working Directory:", os.getcwd())

# rospy.init_node('odom_to_csv_node', anonymous=True)

# file_path = 'Track3.csv'
# if os.path.exists(file_path):
#     os.remove(file_path)
#     rospy.loginfo(f"Deleted existing file: {file_path}")

# csv_file = open(file_path, 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Time', 'X-position', 'Y-position'])

# def odom_callback(odom_msg):
#     time_stamp = str(rospy.Time.now().to_sec())  # Convert time to seconds and then to a string
#     x_position = format(odom_msg.pose.pose.position.x, '.15f')  # Set the precision to 15 decimal places
#     y_position = format(odom_msg.pose.pose.position.y, '.15f')  # Set the precision to 15 decimal places

#     csv_writer.writerow([time_stamp, x_position, y_position])
#     print(f"time: {time_stamp}, x: {x_position}, y: {y_position}")

# odom_sub = rospy.Subscriber('/odom', Odometry, odom_callback)
# rospy.spin()

# csv_file.close()

# !/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
import csv
t = 25.4262154
class CmdVelSubscriber:
    def __init__(self):
        rospy.init_node('cmd_vel_subscriber')

        self.cmd_vel_values = []
        
        rospy.Subscriber('/cmd_vel', Float64, self.cmd_vel_callback)

        self.csv_file = open('pedal_4.csv', 'w')
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(['Time', 'Pedal Value', 'Total Time'])

    def cmd_vel_callback(self, msg):
        current_time = rospy.get_time()
        self.cmd_vel_values.append([current_time, msg.data, t])
        self.csv_writer.writerow([current_time, msg.data,t])

    def save_data_to_csv(self):
        for data_point in self.cmd_vel_values:
            self.csv_writer.writerow(data_point)
        self.csv_file.close()

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    cmd_vel_subscriber = CmdVelSubscriber()
    rospy.on_shutdown(cmd_vel_subscriber.save_data_to_csv)
    cmd_vel_subscriber.run()
