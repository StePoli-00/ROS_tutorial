import rospy
from first_package.srv import multiplier,multiplierResponse #input,output

def callback(request):
    return multiplierResponse(request.a * request.b)

def multiply():
    rospy.init_node("multplier_service")
    #1=name of the service, #2=type of service,#3=callback function to call
    service=rospy.Service("multiplier",multiplier,multiplierResponse)
    rospy.spin()

if __name__=="__main__":
    multiply()