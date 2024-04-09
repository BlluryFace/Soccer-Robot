from lgpio import gpiochip_open, gpiochip_close, gpio_claim_output, gpio_write, gpio_free
import time

class Robot:
    def __init__(self, name, lwheel, rwheel):
        self.name = name
        self.rwheel = tuple(rwheel)
        self.lwheel = tuple(lwheel)

        self.rwheel_f = int(rwheel[0])
        self.rwheel_b = int(rwheel[1])

        self.lwheel_f = int(lwheel[0])
        self.lwheel_b = int(lwheel[1])

        self.chip = gpiochip_open(0)

        gpio_claim_output(self.chip, self.rwheel_f)
        gpio_claim_output(self.chip, self.rwheel_b)
        gpio_claim_output(self.chip, self.lwheel_f)
        gpio_claim_output(self.chip, self.lwheel_b)

    def forward(self, sec):
        gpio_write(self.chip, self.rwheel_f, 1)
        gpio_write(self.chip, self.lwheel_f, 1)
        time.sleep(sec)
        gpio_write(self.chip, self.rwheel_f, 0)
        gpio_write(self.chip, self.lwheel_f, 0)

    def backward(self, sec):
        gpio_write(self.chip, self.rwheel_b, 1)
        gpio_write(self.chip, self.lwheel_b, 1)
        time.sleep(sec)
        gpio_write(self.chip, self.rwheel_b, 0)
        gpio_write(self.chip, self.lwheel_b, 0)

    def lturn(self, sec):
        gpio_write(self.chip, self.rwheel_f, 1)
        gpio_write(self.chip, self.lwheel_f, 0)
        time.sleep(sec)
        gpio_write(self.chip, self.rwheel_f, 0)
        gpio_write(self.chip, self.lwheel_f, 0)

    def rturn(self, sec):
        gpio_write(self.chip, self.rwheel_f, 0)
        gpio_write(self.chip, self.lwheel_f, 1)
        time.sleep(sec)
        gpio_write(self.chip, self.rwheel_f, 0)
        gpio_write(self.chip, self.lwheel_f, 0)

    def cleanup(self):
        gpio_write(self.chip, self.rwheel_f, 0)
        gpio_write(self.chip, self.rwheel_b, 0)
        gpio_write(self.chip, self.lwheel_f, 0)
        gpio_write(self.chip, self.lwheel_b, 0)
        gpio_free(self.chip, self.rwheel_f)
        gpio_free(self.chip, self.rwheel_b)
        gpio_free(self.chip, self.lwheel_f)
        gpio_free(self.chip, self.lwheel_b)
        gpiochip_close(self.chip)

def main():
    it = 20
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