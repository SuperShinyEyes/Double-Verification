import cv2

#vcap = cv2.VideoCapture("rtsp://192.168.1.4:8080/out.h264")
#vcap = cv2.VideoCapture("rtsp://admin:Cisco123@192.168.1.4:554/live/stream1")
#vcap = cv2.VideoCapture("rtsp://38.117.88.90/TenTV/video")
vcap = cv2.VideoCapture("http://192.168.1.16:8080/videofeed?dummy=param.mjpg")

while(1):

    ret, frame = vcap.read()
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)
