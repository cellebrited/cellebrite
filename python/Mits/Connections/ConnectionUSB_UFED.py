"""
from Mits.Utils.upy import upy
from Mits.Connections.IConnection import IConnection
LOGS_ENABLED = False
import time
# descriptor type
# endpoint direction
# endpoint type
# control request type
# control request recipient
# control request direction

class ConnectionUSB(IConnection):
    def __init__(self, vid, pid, configuration = 1, interface = 2, 
        if LOGS_ENABLED:
        if to_open_connection==True:
        self.set_timeout(timeout)
    @staticmethod
    def __repr__(self):

    def __del__(self):

    def __to_ufed_probing_mode(self, probing_mode):


    def connect(self, busy_waiting=False, configuration=None, interface=0, write_endpoint=1, read_endpoint=2, probing_mode_list = None):
        if self.is_init:
        print "#### connect(%s)" % probing_mode_list
        upy.instance.com_set_config(0x80, True)
        if probing_mode_list != None :
        for probing_mode_i in probing_mode :
        time.sleep(0.02)
        self.is_init = True
        if LOGS_ENABLED:
        return True

    def close(self):
        upy.instance.com_disconnect()
        self.is_init = False
        if LOGS_ENABLED:


    def control_msg(self, requesttype, request, buffer, value=0, index=0, timeout=0.1):
        if (requesttype & 0x80) == 0: # out
        if LOGS_ENABLED:
    def clear_halt(self, endpoint):
        # TODO

    def get_timeout(self):

    def set_timeout(self, timeout):
        if LOGS_ENABLED:
        print "#### setting timeout to " + str(timeout)
        upy.instance.usb_set_read_timeout(self.seconds_to_ms(timeout))
    def send(self, buf):
        if LOGS_ENABLED:
        #print "#### sending:" + repr(buf)
        return upy.instance.io_send(buf, len(buf))

    def recv(self, size):
        chunk_size = 4096
            if read < chunk_size:
        result = self.recv_buffer[:size]
        if LOGS_ENABLED:
        return result

    def flush(self):
        if LOGS_ENABLED:
        while (self.recv(1024)):