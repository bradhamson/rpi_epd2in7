'''

Fake implimentation of spidev for developing raspberry pi stuff on my local non-linux system.
Credit goes to original creators of the module (below). Original license included below:

 * spidev_module.c - Python bindings for Linux SPI access through spidev
 *
 * MIT License
 *
 * Copyright (C) 2009 Volker Thoms <unconnected@gmx.de>
 * Copyright (C) 2012 Stephen Caudle <scaudle@doceme.com>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
'''


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