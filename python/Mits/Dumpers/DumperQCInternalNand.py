"""
Written By: Nadav Horesh
from IDumper import IDumper
class DumperQCInternalNand(IDumper):
    def dump(self,start = 0, end = 0, search_start = 0, search_end = 0, step = 1, name = "", profile = None, version = 1):
        data = self.protocol.internal_nand_init(search_start,search_end, version)
        if profile != None:
            self.protocol.internal_nand_update(page_size, total_page_size)

        if end == 0:
        self.open_output(name, "QC Internal Driver Nand", start, end)