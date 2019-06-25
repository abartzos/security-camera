# security-camera

Turns a webcam to a wireless security camera that not only
detects motion, saves the detected frames and notifies the user,
but also works wirelessly and lets you check the camera using VNC
to the computer running the software.

### Running the software
To run the software all you need to do is run the following command from your terminal: 
```
$ python3 main.py sender@gmail.com receiver@gmail.com sender-password
```
Keep in mind that you can use the same address for both the sender and the receiver. 

### Requirements
- Python3
- open-cv for Python3

The motion-detection algorithm was built by [Pavlos Makridis](https://github.com/PavlosMak/Motion_Detection)
