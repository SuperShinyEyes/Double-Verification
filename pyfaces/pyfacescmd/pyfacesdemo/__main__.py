from pyfaces import pyfaces
import sys,time
import MySQLdb
import bluetooth
import os
import pickle
import serial

import sh, subprocess, os
from PIL import Image

start = time.time()

def crop_img(img):
  X = 200
  Y = 60
  WIDTH = 240
  HEIGHT = 320
  img = Image.open(img)
  # img2 = img.crop((X, Y, X+WIDTH, Y+HEIGHT))
  # img2.save("image_cropped.jpg")
  img_cropped = img.crop((X, Y, X+WIDTH, Y+HEIGHT))
  img_cropped.save('image_cropped.jpg')
  print img_cropped.size, '\n'

def read_mac_addr_db(filename):
  image_path = "/var/www/html/pictures" + filename
  # Open database connection
  db = MySQLdb.connect("localhost","root","doubleVDB","DVDB" )

  # prepare a cursor object using cursor() method
  cursor = db.cursor()

  # Prepare SQL query to INSERT a record into the database.
  sql = "SELECT GoogleAccount FROM registerTable WHERE imagePath = '%s'" % (image_path)

  try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    mac_addr = cursor.fetchall()
    sql_img_path = "SELECT imagePath FROM registerTable WHERE imagePath = '%s'" % (image_path)
    cursor.execute(sql_img_path)
    print cursor.fetchall()[0]
    print ">>>>>mac_addr:", mac_addr[0]
    print type(mac_addr)
  except:
    print "Error: unable to fecth data"

  else:
    if mac_addr != None:
      return mac_addr
    else:
      return False

  finally:
    # disconnect from server
    db.close()

def person_has_phone(mac_addr):
  print "Mac address:", mac_addr
  nearby_devices = bluetooth.discover_devices()
  return mac_addr in nearby_devices

def run_bash_cmd(cmd):
  process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
  output = process.communicate()[0]
  return output


CWP = os.getcwd()   # Get current working directory
CWP_parent = '/'.join(CWP.split('/')[:-1])

print("Taking a photo!")
# CAPTURE_COMMAND = "fswebcam -r 1280x720 image.jpg"
CAPTURE_COMMAND = "fswebcam -r 640x426 image.jpg"
print run_bash_cmd(CAPTURE_COMMAND)

print("Cropping...")
imgname = CWP + "/image.jpg"
crop_img(imgname)
imgname = CWP + "/image_cropped.jpg"

print("Run face recognition!")
# FACE_REC_COMMAND = "python pyfacescmd/pyfacesdemo %s 12 3" % image_path

dirname = CWP_parent + "/images/gallery/"
egfaces = 3
thrshld = 3
pyf=pyfaces.PyFaces(imgname,dirname,egfaces,thrshld)
end = time.time()
print 'took :',(end-start),'secs'

mac_addr = read_mac_addr_db(pyf.matchfile)
if mac_addr != False:
  if person_has_phone(mac_addr):
    print "Welcome!!!"
  else:
    print "You are not supposed to do it!"
