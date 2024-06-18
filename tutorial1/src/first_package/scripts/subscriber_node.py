#!/usr/bin/env
import rospy 
from std_msgs.msg import String 

#String obj contains the data inside obj data
def callback(data):
    rospy.loginfo("Received data: %s",data.data)

def listener():
   rospy.init_node("Subscriber_Node",anonymous=True)
   #1:topic to subscribe, 2:type, 3:function to call when a message arrive into topic
   rospy.Subscriber("talking_topic",String,callback)
   #allow to run the node until will be killed
   rospy.spin()
   return 


if __name__=="__main__":
    try: 
        listener()
    except rospy.ROSInterruptException:
        pass 