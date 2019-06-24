"""
Important Note for the notification: for this to work you have to allow 'less secure apps' to acess your account.
You can do this from here: https://myaccount.google.com/lesssecureapps?pli=1
"""

import cv2
import numpy as np
import datetime
import os

font = cv2.FONT_HERSHEY_SIMPLEX
text = ""

red = (0,0,255) #BGR
green = (0,255,0)

cap = cv2.VideoCapture(0) #0 means first webcam

frames = []
counter = 0

threshold = 1
counter_threshold = 1000

def notify(frame):
    '''
    saves the moving frame and notifies the user

    arguments: 
        frame : the photo to be saved
        sender_email_id : The email id from which the notification email will be sent (e.g example_sender@gmail.com).
        sender_email_id_password: The password of the sender's email id. 
        receiver_email_id: The email id of the receiver of the notification email (e.g example_receiver@gmail.com).
    '''
    dt = str(datetime.datetime.now())
    filename = 'frames/' + dt + ".png"
    cv2.imwrite(filename, frame)

    os.system("python3 email.py")

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    #converts captured frame to Grayscale for easier analysis
    
    frames.append(gray)

    cv2.putText(frame,text,(5,30), font, 1, red, 3, cv2.LINE_AA) 

    dt = str(datetime.datetime.now())
    cv2.putText(frame,dt,(5,70), font, 1, green, 3, cv2.LINE_AA)

    cv2.imshow('Camera',frame)
    
    
    if counter > 0:
        difference = cv2.subtract(cv2.medianBlur(frames[counter],15),cv2.medianBlur(frames[counter-1],15)) 
        #applies median blur before subtracting for noise reduction 
        
        #cv2.imshow('difference',difference)
        mean = np.mean(difference)
        #print(mean)
        if mean > threshold:
            text = "Motion Detected"
            #when movement is detected, it notifies the user
            notify(frame)
        else:
            text = ""
    
    #clears "frames" and "counter" every "counter_threshold" frames
    #so that the program can run for longer time
    if counter > counter_threshold:
        frames = [frames[counter-1], frames[counter]]
        counter = 0

    if cv2.waitKey(1) & 0xFF == ord('q'): 
    #Press q to quit video capture
        break
    
    counter = counter + 1
    

cap.release()
cv2.destroyAllWindows()
