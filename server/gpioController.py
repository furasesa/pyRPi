try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None
    print("error when import RPi.GPIO")


class Controller:
    """
        :param mode_value GPIO mode BCM or Board. The Default is BCM (11):
    """
    def __init__(self, mode_value=11):
        self._gpio = GPIO
        self._gpio.setmode(mode_value)

    @property
    def mode(self):
        return self._gpio.getmode()

    @mode.setter
    def mode(self, new_value):
        if self.mode != new_value:
            self._gpio.setmode(new_value)


if __name__ == '__main__':
    con = Controller().__doc__

    # EOF
