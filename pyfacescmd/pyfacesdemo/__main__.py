from pyfaces import pyfaces
import sys,time

# if __name__ == "__main__":
#     try:
#         start = time.time()
#         argsnum=len(sys.argv)
#         print "args:",argsnum
#         if(argsnum<5):
#             print "usage:python pyfacesdemo imgname dirname numofeigenfaces threshold "
#             sys.exit(2)
#         imgname=sys.argv[1]
#         dirname=sys.argv[2]
#         egfaces=int(sys.argv[3])
#         thrshld=float(sys.argv[4])
#         pyf=pyfaces.PyFaces(imgname,dirname,egfaces,thrshld)
#         end = time.time()
#         print 'took :',(end-start),'secs'
#     except Exception,detail:
#         print detail.args
#         print "usage:python pyfacesdemo imgname dirname numofeigenfaces threshold "

import sh, subprocess, os
from PIL import Image

def crop_img(img):
  X = 200
  Y = 60
  WIDTH = 240
  HEIGHT = 320
  img = Image.open(img)
  # img2 = img.crop((X, Y, X+WIDTH, Y+HEIGHT))
  # img2.save("image_cropped.jpg")
  img.crop((X, Y, X+WIDTH, Y+HEIGHT))
  img.save()
  print img.size

CWP = os.getcwd()   # Get current working directory
CWP_parent = '/'.join(CWP.split('/')[:-1])

def run_bash_cmd(cmd):
  process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
  output = process.communicate()[0]
  return output

print("Taking a photo!")
# CAPTURE_COMMAND = "fswebcam -r 1280x720 image.jpg"
CAPTURE_COMMAND = "fswebcam -r 640x426 %s /images/probes/image.jpg" % CWP_parent
print run_bash_cmd(CAPTURE_COMMAND)

print("Cropping...")
imgname = CWP + "/images/probes/image.jpg"
crop_img(imgname)
# imgname = CWP + "/image_cropped.jpg"

print("Run face recognition!")
# FACE_REC_COMMAND = "python pyfacescmd/pyfacesdemo %s 12 3" % image_path

dirname = CWP_parent + "/images/gallery/"
egfaces = 12
thrshld = 3
pyf=pyfaces.PyFaces(imgname,dirname,egfaces,thrshld)
print pyf.matchfile
