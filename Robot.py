from RPi import GPIO
import time


class Robot:
    def __init__(self, name, lwheel, rwheel):
        self.name = name
        # getting GPIO #'s in sets for R & L
        self.rwheel = tuple(rwheel)
        self.lwheel = tuple(lwheel)

        # identifiying indv #'s as ints
        self.rwheel_f = int(rwheel[0])
        self.rwheel_b = int(rwheel[1])

        self.lwheel_f = int(lwheel[0])
        self.lwheel_b = int(lwheel[1])
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.rwheel_f, GPIO.OUT)
        GPIO.setup(self.rwheel_b, GPIO.OUT)
        GPIO.setup(self.lwheel_f, GPIO.OUT)
        GPIO.setup(self.lwheel_b, GPIO.OUT)

    def forward(self, sec):
        GPIO.output(self.rwheel_f, True)
        GPIO.output(self.lwheel_f, True)
        time.sleep(sec)
        # stop
        GPIO.output(self.rwheel_f, False)
        GPIO.output(self.lwheel_f, False)

    def backward(self, sec):
        GPIO.output(self.rwheel_b, True)
        GPIO.output(self.lwheel_b, True)
        time.sleep(sec)
        # stop
        GPIO.output(self.rwheel_b, False)
        GPIO.output(self.lwheel_b, False)

    def lturn(self, sec):  # turn left
        GPIO.output(self.rwheel_f, True)
        GPIO.output(self.lwheel_f, False)
        time.sleep(sec)
        # stop
        GPIO.output(self.rwheel_f, False)
        GPIO.output(self.lwheel_f, False)

    def rturn(self, sec):  # turn right
        GPIO.output(self.rwheel_f, False)
        GPIO.output(self.lwheel_f, True)
        time.sleep(sec)
        # stop
        GPIO.output(self.rwheel_f, False)
        GPIO.output(self.lwheel_f, False)

    def cleanup(self):
        GPIO.cleanup([self.rwheel_f, self.rwheel_b,
                     self.lwheel_f, self.lwheel_b])


def main():
    # Test if the robot move successfully
    it = 20 # Run the robot 20 times, which is about 20 * 20 = 400 seconds ~ 6.67 minutes
    i = 0
    try:
        while i < it:
            robot1 = Robot("player", (18, 17), (23, 22))
            robot1.forward(5)
            robot1.lturn(5)
            robot1.rturn(5)
            robot1.backward(5)
            robot1.cleanup()
            i += 1
    except KeyboardInterrupt:
        pass
    finally:
        robot1.cleanup()

if __name__ == "__main__":
    main()
