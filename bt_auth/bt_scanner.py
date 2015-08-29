#!/usr/bin/python

import MySQLdb
import bluetooth
import os
import pickle
import time
import serial


target_name = "My Phone"
target_address = None

# blink Arduino LED
def blink_led(isOn)

def scan_bt():
    bt_list_file = "existing_bt_list"

    nearby_devices = bluetooth.discover_devices()

    existing_bt_list = None
    # read list from files
    if os.path.isfile(bt_list_file):
        print "read list"
        with open(bt_list_file, 'rb') as f:
            existing_bt_list = pickle.load(f)
    else:
        existing_bt_list = []

    print existing_bt_list

    for bdaddr in nearby_devices:
        bt_new = True 
        if bdaddr in existing_bt_list:
            print "old"   
        else:
            print "new"
            if read_bt_db(bdaddr):
                print "AUTHORIZE"

        print "bt ", bdaddr
        print "name ", bluetooth.lookup_name( bdaddr ) 
        #if target_name == bluetooth.lookup_name( bdaddr ):
        #    target_address = bdaddr
        #    break

    #if target_address is not None:
    #    print "found target bluetooth device with address ", target_address
    #else:
    #    print "could not find target bluetooth device nearby"

    if os.path.isfile(bt_list_file):
         os.remove(bt_list_file)
    else:    ## Show an error ##
         print "Error file not found: ", bt_list_file
    with open(bt_list_file, 'wb') as f:
        pickle.dump(nearby_devices, f)

# if bt_mac in DB return True
def read_bt_db(bt_mac):
    # Open database connection
    db = MySQLdb.connect("localhost","root","doubleVDB","DVDB" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM registerTable \
        WHERE GoogleAccount = '%s'" % (bt_mac)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()

        if not results:
            return False
        else:
            return True

#        for row in results:
#            fname = row[0]
#            lname = row[1]
#            age = row[2]
#            sex = row[3]
#            income = row[4]
#            # Now print fetched result
#            print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
#                (fname, lname, age, sex, income )
    except:
        print "Error: unable to fecth data"

    # disconnect from server
    db.close()

    return False
    

while True:
    scan_bt()
    time.sleep(5) # 5 seconds
