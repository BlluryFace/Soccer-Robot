from RPi import GPIO
import time
class Robot:
    def __init__(self, name, rwheel, lwheel):
        self.name = name
        # getting GPIO #'s in sets for R & L
        self.rwheel = tuple(rwheel)
        self.lwheel = tuple(lwheel)

        #identifiying indv #'s as ints
        self.rwheel_f = int(rwheel[0])
        self. rwheeL_b = int(rwheel[1])
        
        self.lwheel_f = int(rwheel[0])
        self. lwheel_b = int(rwheel[1])

    def forward(self, sec):
        GPIO.output (self.rwheel_f, True)
        GPIO.output (self.lwheel_f, True)
        time.sleep (sec)
        # stop
        GPIO.output (self.rwheel_f, True)
        GPIO.output (self.lwheel_f, True)

    def backward(self, sec):
        GPIO.output (self.rwheel_b, True)
        GPIO.output (self.lwheel_b, True)
        time.sleep (sec)
        # stop
        GPIO.output (self.rwheel_f, False)
        GPIO.output (self.lwheel_f, False)

    def lturn(self, sec): # turn left
        GPIO.output (self.rwheel_f, True)
        GPIO.output (self.lwheel_f, False)
        time.sleep (sec)
        # stop
        GPIO.output (self.rwheel_f, False)
        GPIO.output (self.lwheel_f, False)

    def rturn(self, sec): # turn right
        GPIO.output (self.rwheel_f, False)
        GPIO.output (self.lwheel_f, True)
        time.sleep (sec)
        # stop
        GPIO.output (self.rwheel_f, False)
        GPIO.output (self.lwheel_f, False)
            
            
def main():
    # Test if the robot move successfully
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    
    robot1 = Robot("robot1", (18, 23), (24, 25))
    robot1.forward(2)
    robot1.lturn(2)
    robot1.rturn(2)
    robot1.backward(2)
    GPIO.cleanup()
    
if __name__ == "__main__":
    main()