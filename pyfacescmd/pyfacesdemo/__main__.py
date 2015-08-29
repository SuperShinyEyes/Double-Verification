from pyfaces import pyfaces
# import sys,time
#
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

CWP = os.getcwd()   # Get current working directory
CWP = '/'.join(CWP.split('/')[:-1])

def run_bash_cmd(cmd):
  process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
  output = process.communicate()[0]
  return output

print("Taking a photo!")
# CAPTURE_COMMAND = "fswebcam -r 1280x720 image.jpg"
CAPTURE_COMMAND = "fswebcam -r 640x426 image.jpg"
print run_bash_cmd(CAPTURE_COMMAND)

print("Run face recognition!")
# FACE_REC_COMMAND = "python pyfacescmd/pyfacesdemo %s 12 3" % image_path
imgname = CWP + "/image.jpg"
dirname = CWP + "/images/gallery/"
egfaces = 12
thrshld = 3
pyf=pyfaces.PyFaces(imgname,dirname,egfaces,thrshld)
print pyf.matchfile
