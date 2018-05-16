#!/usr/bin/env python

import rospy
import std_msgs
import pubsub

def callback_sub_0(data):
    print(data.data)

def callback_sub_1(data):
    print(data.data)

if __name__ == '__main__':
    rospy.init_node('your_package', anonymous=True)
    r = rospy.Rate(10)

    # pub/sub initialization
    pubsub.init({'sub_0': callback_sub_0, 'sub_1': callback_sub_1})

    i = 0
    while not rospy.is_shutdown():

        # publish something
        pubsub.pub_0.publish("Hello world")
        pubsub.pub_1.publish(i)

        i += 1

        r.sleep()
