#!/usr/bin/env python

import RPi.GPIO as GPIO, feedparser, time
import getpass
DEBUG = 1

#USERNAME = "maskoken"
USERNAME = raw_input("Username (ex. username@gmail.com): ")
PASSWORD = getpass.getpass(prompt="Password: ")

NEWMAIL_OFFSET = 0        # Set your own zero
MAIL_CHECK_FREQ = 30      # check mail every 30 seconds

GPIO.setmode(GPIO.BCM)
GREEN_LED = 23
RED_LED = 18
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
last = -1
while True:

        newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])

        if DEBUG:
		if (last!=newmails):
	                print "You have", newmails, "new emails!"

        if newmails > NEWMAIL_OFFSET:
                GPIO.output(GREEN_LED, True)
                GPIO.output(RED_LED, False)
        else:
                GPIO.output(GREEN_LED, False)
                GPIO.output(RED_LED, True)
	last = newmails
        time.sleep(MAIL_CHECK_FREQ)

