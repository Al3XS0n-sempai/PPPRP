class Counter:
    """Simple counter

    :param value: Value of the counter, initial 0
    """

    def __init__(self):
        self.__value: int = 0

    def inc(self) -> None:
        """Increment value of counter by 1
        """
        self.__value += 1

    @property
    def value(self) -> int:
        """Value of the counter
        """
        return self.__value

