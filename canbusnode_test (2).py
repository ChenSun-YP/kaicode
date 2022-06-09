#!/usr/bin/env python3
from email import message
import rospy

# import  python_ics as ics
# ics.override_library_name("libicsneolegacy.so")
import cantools
# devices = ics.find_devices()
# print(devices)
import ctypes

class CanbusNodePublish(object):
    def __init__(self):
        super().__init__()
        self.publishers()
        self.now = rospy.Time.now()

    def subscribers(self):
        pass


    def publishers(self):
        encoded_message = b'\x20\x00\x8c\x01\x00\x00\x00\x00'

        data = [0xf0,0xdd,0x62,0x2a,0x4b,0x40,0x0]
        arbitration_id =0x31
        data =encoded_message
        db = cantools.database.load_file("Scoring_Year1_v4.dbc") 
        x = db.decode_message( arbitration_id,data) 
        print(x)
        vis_topic = '/topic'
        pub = rospy.Publisher(vis_topic, x, queue_size=1)

        self.visualize_pub = pub
        pub.publish([arbitration_id,data])


if __name__ == '__main__':
    rospy.init_node('canbus_publisher_node')
    r = CanbusNodePublish()
    rospy.spin()



    
# def dev_name(device):
#     # Return a friendly name of the device (ie. neoVI FIRE2 CY1234)
#     if int("AA0000", 36) <= device.SerialNumber <= int("ZZZZZZ", 36):
#         return device.Name + " " + ics.base36enc(device.SerialNumber)
#     else:
#         return device.Name + " " + str(device.SerialNumber)
        
# def open_device(index=0):
#     device = None
#     if enable_use_server:
#         # ics.open_device() won't open a device if we have handles open already
#         # so we need to find them and specify which ones to connect to.
#         devices = ics.find_devices()
#         print("Opening Device {} (Open Client handles: {})...".format(dev_name(devices[index]), devices[index].NumberOfClients))
#         ics.open_device(devices[index])
#         device = devices[index]
#     else:
#         print("Opening Device...")
#         device = ics.open_device()
#     print("Opened Device %s." % dev_name(device))
#     return device
    
# def transmit_can(device):
#     msg = ics.SpyMessage()
#     msg.ArbIDOrHeader = 0x01 # CAN Arbitration ID
#     msg.Data = (1,2,3,4,5,6,7,8) # Data Bytes go here
#     msg.NetworkID = ics.NETID_HSCAN # First channel of CAN on the device
    
#     # msg parameter here can also be a tuple of messages
#     ics.transmit_messages(device, msg)

# def receive_can(device):
#     msgs, error_count = ics.get_messages(device)
#     print("Received {} messages with {} errors.".format(len(msgs), error_count))
#     # for i, m in enumerate(msgs):
#     #     print('Message #{}\t'.format(i+1), end='')
#     #     print('\tArbID: {}\tData: {}'.format(hex(m.ArbIDOrHeader), [hex(x) for x in m.Data]))
    
    
# if __name__ == "__main__":
#     import time
#     # Lets figure out how many are connected to the PC and display it
#     ics
#     connected_count = len(ics.find_devices())
#     print("Found {} connected device(s)...".format(connected_count))
    
#     tx_dev = open_device(0)
#     rx_dev = open_device(1)
    
#     transmit_can(tx_dev)
#     receive_can(rx_dev)
    


#     while true:
#         receive_can(rx_dev)
    
