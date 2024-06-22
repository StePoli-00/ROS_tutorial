import rospy
from first_package.srv import multiplier,multiplierResponse #input,output

def callback(request):
    return multiplierResponse(request.a * request.b)

def multiplier_client(x,y):
    rospy.init_node("client_node")
    #wait the exitance of multiplier service into roscore
    rospy.wait_for_service("multiplier")
    rate=rospy.Rate(1)
    while not rospy.is_shutdown():

        try:
            multiplier_two_ints=rospy.ServiceProxy("multiplier",multiplier)
            response=multiplier_two_ints(x,y)
            rospy.loginfo(response.result)
            rate.sleep()
        except rospy.ServiceException as e:
            print("Service call failder %s",e)
    

if __name__=="__main__":
    multiplier_client(2,6)