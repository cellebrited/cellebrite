"""
Written by: Nadav Horesh
import struct
from IFramer        import IFramer
class FramerRETeam(IFramer):
    class Results:
    def __init__(self, framer):
    def set_oem_magic(self, magic):

    def send(self, cmd, data=''):
        buf = cmd
        if data:
        buf += self.eom_magic
        self.base.send(buf)

    def recv(self):
        #read header
        if head != self.Results.REPLAY:
        cmd  = self.base.recv(4)           #read command
        if (self.Results.OK_COM == res):
        # read all data
        if (compress):
            data_len = unpack32L(data[:4])
        if (length != 0):
        i = 0
        if ((res != self.Results.OK) and (res != self.Results.OK_COM)):
        return(head, data)