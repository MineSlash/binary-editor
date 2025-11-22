# Copyright (c) 2025 Alex Papdi
# SPDX-License-Identifier: MIT

from dataclasses import dataclass
from typing import Union

# Type alias for HEX-like input
HexLike = Union[str, int]

class BinaryFile:
    def __init__(self):
        self.data: bytearray = bytearray()
        self.start_address: int = 0x00000000

    def load_file(self, filepath: str):
        """
        Loads a binary file

        :param filepath: Path of the binary file
        """
        with open(filepath, 'rb') as file:
            self.data = bytearray(file.read())

    def read_memory(self, address: HexLike, length: HexLike = 1) -> str:
        """
        Reads a sequence of bytes from memory starting at the given address

        :param address: Memory address of the data to read
        :param length: Length of the data to read
        :return: Returns the read memory data
        """
        addr = int(address, 16) if isinstance(address, str) else address
        length = int(length, 16) if isinstance(length, str) else length
        return ''.join(f'{i:02X}' for i in self.data[addr : addr + length])

    def write_memory(self, address: HexLike, data: HexLike):
        """
        Writes a sequence of bytes to memory at the given address

        :param address: Memory address of the data to overwrite
        :param data: Data to overwrite with
        """
        addr = int(address, 16) if isinstance(address, str) else address

        if isinstance(data, int):
            int_data = data
        elif isinstance(data, str):
            int_data = int(data.lstrip('0x').upper(), 16)
        else:
            raise TypeError("Data must be str or int")

        length = (int_data.bit_length() + 7) // 8

        self.data[addr : addr + length] = int_data.to_bytes(length, byteorder='big')

    def save_file(self, filepath: str):
        """
        Saves the current memory map to a binary file.

        :param filepath: Output file path
        """
        with open(filepath, 'wb') as file:
            file.write(self.data)


@dataclass
class BinaryEditor:
    file: str

    def __post_init__(self):
        self.parser = BinaryFile()
        self.parser.load_file(self.file)

    @property
    def start_address(self) -> str:
        """
        :return: Returns the start address of the binary file
        """
        return f'0x{self.parser.start_address:08X}'

    @property
    def length(self) -> int:
        """
        :return: Returns the total length of the memory block in bytes
        """
        return len(self.parser.data)

    def read(self, address: HexLike, length: HexLike = 1) -> str:
        """
        Reads memory content from the given address

        :param address: Memory address of the data to read
        :param length: Length of the data to read
        :return: Returns the read memory data
        """
        return self.parser.read_memory(address, length)

    def write(self, address: HexLike, data: HexLike, output: str = None):
        """
        Writes data to memory and saves the result to a new binary file

        :param address: Memory address of the data to overwrite
        :param data: Data to overwrite with
        :param output: Output file path
        """
        self.parser.write_memory(address, data)
        self.parser.save_file(output if output is not None else self.file)


if __name__ == '__main__':
    bin_parser = BinaryEditor('Sample.bin')

    print("Start address:", bin_parser.start_address)
    print("Length:", bin_parser.length)
    print("Read:", bin_parser.read('0x00000020', 0x10))

    bin_parser.write(
        address='0x00000020',
        data='B0C1F0C1B0C1C1CADEADBEEF1EE7FEE7',
        output='Sample_modified.bin'
    )
