"""
    Families
    This module contains the concrete families definitions,
    Family definition is a combination of Chain and Connection
"""
import os
from Mits.Configuration.Config import BOOTLOADER_ROOT_PATH


from Mits.Connections.ConnectionUSBProbing import USBProbing
from Mits.Families.BaseFamily               import BaseFamilySerial, BaseFamilyUSB, BaseFamilyUSBoSerial
from Mits.Chains.ChainQualcomm              import ChainQualcomm


"""
These families support dumping the flash using Qualcomm's dload_mode protocol,
all by itself.
"""


class FamilyQcDownload_ReadEmmc(BaseFamilyUSBoSerial):
    """Dump the flash using Qualcomm's download protocol, with the command 0x50 (read EMMC flash)."""


    def __init__(self, port = None, _timeout = 0.5):
        BaseFamilyUSBoSerial.__init__(self, "QualcommDownload_ReadEmmc", ChainQualcomm, True, 5, 
                                      usb_busy_waiting= False, usb_probing_mode = [USBProbing.vendor_no_probing, USBProbing.com_data_no_probing], com_port = port)
        self.flash_type = "emmc"
        self.conn.set_timeout(_timeout)






class FamilyQcDownload_ReadNand(BaseFamilySerial):
    """Dump the flash using Qualcomm's download protocol, with the command 0x31 (read NAND flash)."""


    def __init__(self, port = None):
        BaseFamilySerial.__init__(self, "QualcommDownload_ReadNand", ChainQualcomm, port)
        self.flash_type = "nand"




"""
These families support dumping the flash using Qualcomm's dload_mode protocol,
with help from our trusted bootloader, uploaded and run from memory.
"""


class FamilyQcDownload_BootloaderGeneric(BaseFamilySerial):
    """Dump the flash by uploading a bootloader using the Qualcomm's download protocol"""
    def __init__(self, port = None):
        BaseFamilySerial.__init__(self, "QualcommDownload_BootloaderGeneric", ChainQualcomm, port)
        self.bootloader_path = os.path.join(BOOTLOADER_ROOT_PATH, 'Qualcomm', 'Download', 'QC_Download.bin')




class FamilyQCDownloadUSB_ACER(BaseFamilyUSB):
    def __init__(self):
        vid = [0x502]
        pid = [0x9002]
        BaseFamilyUSB.__init__(self, "ACER", ChainQualcomm, vid, pid, \
                               configuration = 1, interface=0, write_endpoint = 1, read_endpoint=1)
        self.bootloader_path = os.path.join(BOOTLOADER_ROOT_PATH, 'Qualcomm', 'Download', 'QC_Download.bin')


class FamilyQCDownloadUSB_ZTE(BaseFamilyUSB):
    def __init__(self):
        vid = [0x19D2]
        pid = [0x112]
        BaseFamilyUSB.__init__(self, "ZTE", ChainQualcomm, vid, pid, \
                               configuration = 1, interface=0, write_endpoint = 1, read_endpoint=1)
        self.bootloader_path = os.path.join(BOOTLOADER_ROOT_PATH, 'Qualcomm', 'Download', 'QC_Download.bin')


class FamilyQCDownloadUSB_Huawei(BaseFamilyUSB):
    def __init__(self):
        vid = [0x12D1]
        pid = [0x1038]
        BaseFamilyUSB.__init__(self, "Huawei", ChainQualcomm, vid, pid, \
                               configuration = 1, interface=0, write_endpoint = 1, read_endpoint=1)
        self.bootloader_path = os.path.join(BOOTLOADER_ROOT_PATH, 'Qualcomm', 'Download', 'QC_Download.bin')


class FamilyQCDownloadUSB_KS20(BaseFamilyUSB):
    def __init__(self):
        vid = [0x1004]
        pid = [0x6061]
        BaseFamilyUSB.__init__(self, "KS20", ChainQualcomm, vid, pid, \
                               configuration = 1, interface=2, write_endpoint = 5, read_endpoint=4)


class FamilyQCDownloadUSB_Pantech(BaseFamilyUSB):
    def __init__(self):
        vid = [0x106C]
        pid = [0x2402, 0x240C]
        BaseFamilyUSB.__init__(self, "Pantech", ChainQualcomm, vid, pid, \
                               configuration = 1, interface=1, write_endpoint = 2, read_endpoint=2)
