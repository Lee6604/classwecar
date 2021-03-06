#!/usr/bin/env python
from __future__ import print_function

import roslib
import sys
import rospy
from std_msgs.msg import Float64

class motor_control:

    def __init__(self):
        self.rate = rospy.Rate(20)
        self.timer_to_sending_data = 0

        self.speed = rospy.Publisher('/commands/motor/speed', Float64, queue_size=1)
        self.position =rospy.Publisher('/commands/servo/postitom', Float64, queue_size=1)

        self.speed_value = 1700
        self.position_value = 0.5
        self.speed.publish(self.speed_value)
        self.position.publish(self.position_value)

def main(args):

    rospy.init_node('motor_control', anonymous=True)
    motor_control()
    rospy.spin()

if __name__ == '__main__':
    main(sys.argv)
