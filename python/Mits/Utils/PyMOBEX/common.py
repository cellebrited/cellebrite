#!/usr/bin/env python



"""

common.py - Classes providing common facilities for other modules.



Copyright (C) 2007 David Boddie <david@boddie.org.uk>



This file is part of the PyOBEX Python package.



This program is free software: you can redistribute it and/or modify

it under the terms of the GNU General Public License as published by

the Free Software Foundation, either version 3 of the License, or

(at your option) any later version.



This program is distributed in the hope that it will be useful,

but WITHOUT ANY WARRANTY; without even the implied warranty of

MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

GNU General Public License for more details.



You should have received a copy of the GNU General Public License

along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""



import socket, sys

import time

import struct

import headers





class OBEX_Version(object):



    major = 1

    minor = 1

    

    def to_byte(self):

        return (self.major & 0x0f) << 4 | (self.minor & 0xf)

    

    def from_byte(self, byte):

        self.major = (byte >> 4) & 0x0f

        self.minor = byte & 0x0f

    

    def __gt__(self, other):

        return (self.major, self.minor) > (other.major, other.minor)





class Message(object):



    format = ">BH"

    

    def __init__(self, data = (), header_data = ()):

    

        self.data = data

        self.header_data = list(header_data)

        self.minimum_length = self.length(Message.format)

    

    def length(self, format):

    

        return format.count("B") + format.count("H") * 2

    

    def read_data(self, data):

    

        # Extract the header data from the complete data.

        header_data = data[self.minimum_length:]

        self.read_headers(header_data)

    

    def read_headers(self, header_data):

    

        i = 0

        header_list = []

        while i < len(header_data):

        

            # Read header ID and data type.

            ID = struct.unpack(">B", header_data[i])[0]

            ID_type = ID & 0xc0

            if ID_type == 0x00:

                # text

                length = struct.unpack(">H", header_data[i+1:i+3])[0] - 3

                data = header_data[i+3:i+3+length]

                i += 3 + length

            elif ID_type == 0x40:

                # bytes

                length = struct.unpack(">H", header_data[i+1:i+3])[0] - 3

                data = header_data[i+3:i+3+length]

                i += 3 + length

            elif ID_type == 0x80:

                # 1 byte

                data = header_data[i+1]

                i += 2

            elif ID_type == 0xc0:

                # 4 bytes

                data = header_data[i+1:i+5]

                i += 5

            

            HeaderClass = headers.header_dict.get(ID, headers.Header)

            header_list.append(HeaderClass(data, encoded = True))

        

        self.header_data = header_list

    

    def add_header(self, header, max_length):

    

        if self.minimum_length + len(header.data) > max_length:

            return False

        else:

            self.header_data.append(header)

            return True

    

    def reset_headers(self):

        self.header_data = []

    

    def encode(self):

    

        length = self.minimum_length + sum(map(lambda h: len(h.data), self.header_data))

        args = (Message.format + self.format, self.code, length) + self.data

        return struct.pack(*args) + "".join(map(lambda h: h.data, self.header_data))

        

    def __str__(self):

        s = ""

        hdrStrings = []

        for hdr in self.header_data:

            hdrStrings.append("%d(%s)" % (hdr.code, repr(hdr.data)))

        return "Headers: %s. Data: %s" % (", ".join(hdrStrings), self.data)

            





class MessageHandler(object):



    format = ">BH"

    

    if sys.platform == "win32":

    

        def _read_packet(self, socket_):

        

            data = ""

            t = time.time()

            while len(data) < 3:

                data += socket_.recv(3 - len(data))

                if time.time() - t > 2:

                    raise Exception("Timeout in _read_packet")

            type, length = struct.unpack(self.format, data)

            while len(data) < length:

                data += socket_.recv(length - len(data))

            return type, length, data

    else:

    

        def _read_packet(self, socket_):

        

            data = socket_.recv(3, socket.MSG_WAITALL)

            type, length = struct.unpack(self.format, data)

            if length > 3:

                data += socket_.recv(length - 3, socket.MSG_WAITALL)

            return type, length, data

    

    def decode(self, socket):

        code, length, data = self._read_packet(socket)

        if self.message_dict.has_key(code):

            message = self.message_dict[code]()

            message.read_data(data)

            return message

        else:

            return self.UnknownMessageClass(code, length, data)

