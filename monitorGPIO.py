import RPi.GPIO as GPIO

class monitorGPIO(object):
    
    def __init__(self):
        GPIO.cleanup()

    def setup_simplemonitor(self, gpio_in, gpio_out):
        """
        Summary:
            Set up for monitoring single gpio.
            If it is called, next you should call simplemonitor().
        Arguments:
            gpio_in: (int) monitored gpio pin number.
            gpio_out: (int) gpio pin number outputting voltage.
        """

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(gpio_out, GPIO.OUT)
        GPIO.setup(gpio_in, GPIO.IN)
        GPIO.output(gpio_out, True)
        self.gpio_in = gpio_in
        self.gpio_out = gpio_out

    def simplemonitor(self):
        return GPIO.input(self.gpio_in)
