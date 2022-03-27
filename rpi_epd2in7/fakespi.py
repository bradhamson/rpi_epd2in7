class SpiDev:
    
    def __init__(self, mode: int = 0, max_speed_hz: int = 0) -> None:
        self._mode = 0
        self._max_speed_hz = 0
        self._bits_per_word = 0
        self.cshigh = None
        self.loop = False
        self.no_cs = False
        self.lsbfirst = None
        self.threewire = None

    @property
    def max_speed_hz(self) -> int:
        pass

    @max_speed_hz.setter
    def max_speed_hz(self, value: int) -> None:
        self._max_speed_hz = value

    @property
    def mode(self) -> int:
        pass

    @mode.setter
    def mode(self, value: int) -> None:
        self.mode = value

    @property
    def bits_per_word(self) -> int:
        pass

    @bits_per_word.setter
    def bits_per_word(self, value: int) -> None:
        self._bits_per_word = value

    def open(self, bus, device) -> None:
        print(f'opening /dev/spidev{bus}.{device}')

    def read_bytes(self, n: int) -> None:
        pass


    def write_bytes(self, values: list) -> None:
        pass

    def write_bytes2(self, values: list) -> None:
        pass

    def xfer(self, values: list) -> None:
        pass

    def xfer2(self, values: list) -> None:
        pass

    def xfer3(self, values: list) -> None:
        pass

    def close(self) -> None:
        pass