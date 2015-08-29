# Double-Verification
Hack@Seoul2015 item<br>
We are using [pyfaces](https://code.google.com/p/pyfaces/) for face recognition.

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
