from Mits.Families.Qualcomm.LgDload0x30 import *

"""
  For VS870 and phones alike its a must to pull off the battery and the usb cable before starting to dump
"""
upy.ui_async_operation("Connecting", "Please wait")
c = Client_LG_30(f)
c.dump()

print "Finished."