import rospy
from sensor_msgs.msg import LaserScan
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, radians, pi


def callback(msg):
    global ranges
    #print (len(msg.ranges))
    ranges=msg.ranges
    #print (msg.ranges[0], msg.ranges[89], msg.ranges[179], msg.ranges[269], msg.ranges[359])
    map(ranges)

def map(ranges):
    x=[]
    y=[]
    for i in range(len(ranges)):
        if ranges == 'inf':
            pass
        else:

            rad=i*2*pi/360
            x_new=-ranges[i]*sin(rad)
            y_new=ranges[i]*cos(rad)
            x.append(x_new)
            y.append(y_new)
    plt.clf()
    plt.scatter(x,y)
    plt.show()


rospy.init_node('scan_values')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
