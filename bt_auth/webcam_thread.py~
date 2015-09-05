import cv2
import sys
import time
import subprocess
import os
import paramiko
import threading

class FuncThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)
 
    def run(self):
        self._target(*self._args)
 
# Example usage
def someOtherFunc(data):
    cv2.imwrite("image.jpg", data)
    ssh = paramiko.SSHClient() 
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect("192.168.1.2", username="root", password="aDMIN123#")
    sftp = ssh.open_sftp()
    sftp.put("/home/nicol/workspace/seoultech/hackatseoul/Double-Verification/bt_auth/image.jpg", "/home/Double-Verification/pyfaces/pyfacescmd/image.jpg")
    sftp.close()
    print "save image"
    #stdin, stdout, stderr = ssh.exec_command('cd /home/Double-Verification/pyfaces/pyfacescmd/')
    #stdin, stdout, stderr = ssh.exec_command('pwd')
    #print 'This is output =',stdout.readlines()
    #print 'This is error =',stderr.readlines()
    #stdin, stdout, stderr = ssh.exec_command('python /home/Double-Verification/pyfaces/pyfacescmd/pyfacesdemo/')
    stdin, stdout, stderr = ssh.exec_command('./run_dver.sh')
    print 'This is output =',stdout.readlines()
    #print 'This is error =',stderr.readlines()
    #channel = ssh.invoke_shell()
    #stdin = channel.makefile('wb')
    #stdout = channel.makefile('rb')

    ssh.close()
       
    time.sleep(5)
    if os.path.isfile("image.jpg"):
        os.remove("image.jpg") 

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture("http://192.168.1.16:8080/videofeed?dummy=param.mjpg")

t1 = None

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=2,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #print "t1 is None", (t1 is None)
    #if ((t1 is None) is False):
    #    print "t1.isAlive is False", (t1.isAlive() is False)
    #if False:
    if len(faces) == 1:
        if (t1 is None) or (t1.isAlive() is False):
	    t1 = FuncThread(someOtherFunc, frame)
            t1.start()
            #t1.join()
       
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
