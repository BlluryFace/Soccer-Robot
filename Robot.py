class Robot：
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

        
        # def forward(self, sec):
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

        def lturn(self, sec):
            GPIO.output (self.rwheel_f, True)
            GPIO.output (self.lwheel_f, False)
            time.sleep (sec)
            # stop
            GPIO.output (self.rwheel_f, False)
            GPIO.output (self.lwheel_f, False)

        def rturn(self, sec):
            GPIO.output (self.rwheel_f, False)
            GPIO.output (self.lwheel_f, True)
            time.sleep (sec)
            # stop
            GPIO.output (self.rwheel_f, False)
            GPIO.output (self.lwheel_f, False)