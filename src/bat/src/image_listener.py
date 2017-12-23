import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

bridge = CvBridge()

def image_callback():
    rospy.init_node('image_listener')
    image_topic = '/cameras/right_hand_camera/image'
    msg = rospy.wait_for_message(image_topic,Image)
    print 'Received an image'
    cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    cv2.imwrite('camera_image.png', cv2_img)
    return cv2_img

if __name__ == '__main__':
    image_callback()
