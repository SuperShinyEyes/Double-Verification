import sh, subprocess, os

CWP = os.getcwd()   # Get current working directory

def run_bash_cmd(cmd):
  process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
  output = process.communicate()[0]
  return output

print("Taking a photo!")
CAPTURE_COMMAND = "fswebcam -r 1280x720 image.jpg
print run_bash_cmd(CAPTURE_COMMAND)

print("Run face recognition!")
image_path = CWP + "/image.jpg"
FACE_REC_COMMAND = "python pyfacescmd/pyfacesdemo %s 12 3" % image_path
print run_bash_cmd(FACE_REC_COMMAND)
