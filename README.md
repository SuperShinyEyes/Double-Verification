# Double-Verification
Double-Verification enables seamless workflow by auto-authenticating users. Double-Verification first recognizes your face and then scans your phone by bluetooth. If both your face and phone(bluetooth mac address) are in the database you will be authenticated.<br>
Double-Verification is an item for Hack@Seoul2015.<br>
We use [pyfaces](https://code.google.com/p/pyfaces/) for face recognition.

## Prerequisite
https://www.youtube.com/watch?v=MRMbZJ1IP6c

## Dependencies
PIL: ```pip install pillow```<br>
MySQLdb<br>
sh: ```pip install sh```<br>

## Requirement
Webcam

## Development Environment
CISCO Edge 340<br>
Linux version 3.6.11-3.fc16.edge340.i686 (CentOS / Red Hat 4.6.3-2)<br>
Python 2.7.3<br>

## How to run
```
# At /pyfaces/pyfacescmd/
python pyfacesdemo/     # This will create two image files from webcam.
```

## Limit
The accuracy depends on the characteristics of test images; light, noise, sharpness and angle.

## Collaborators
Seyoung Park: Face Recognition
[Nikolay Akatyev](https://github.com/kolyaak): Bluetooth
Maeng Seonjoo: DB
Jurgen Germeys: Business Developer
