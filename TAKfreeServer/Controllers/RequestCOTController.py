#######################################################
# 
# RequestCOTController.py
# Python implementation of the Class RequestCOTController
# Generated by Enterprise Architect
# Created on:      26-Mar-2020 6:32:34 PM
# Original author: Corvo
# 
#######################################################
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from Model.Event import Event
import Controllers.constant as con
conn = con.vars()

class RequestCOTController:
    """this controller manage all the different types of COTS, including the geochat
    """
    
    # default constructor  
    def __init__(self):  
        pass

    def timeout(self, lat="00.00000000", lon='00.00000000', le = "9999999.0", ce = "9999999.0", hae = "00.00000000", linkuid='abc', linktype='a-f-G-U-C', linkrelation='p-p', eventhow ='h-g-i-g-o', eventuid = None):
       event = Event(eventhow = eventhow, eventuid = eventuid,eventType = 'timeout',eventconnType = 'timeout',linkType='timeout' ,pointlat=lat, pointlon=lon, pointle=le, pointce=ce, pointhae=hae, linkuid=linkuid, linktype=linktype, linkrelation=linkrelation) 
       return event

    def ping(self, lat="00.00000000", lon='00.00000000', le = "9999999.0", ce = "9999999.0", hae = "00.00000000", eventuid=None):
       event = Event(eventconnType = conn.PING, eventisPing = 1, pointlat=lat, pointlon=lon, pointle=le, pointce=ce, pointhae=hae) 
       return event

    def chat(self, lat="00.00000000", lon='00.00000000', le = "9999999.0", ce = "9999999.0", hae = "00.00000000",isChat = 1,chatType = None, senderCallsign = None, chatroom = None, groupOwner = None, id = None, parent = None, uid0 = None, uid1 = None):
        event = Event(connType = 'chat', chatType = chatType, senderCallsign = senderCallsign, chatroom = chatroom, groupOwner = groupOwner, id = id, parent = parent, uid0 = uid0, uid1 = uid1, chatgrpid = chatgrpid, lat=lat, lon=lon, le=le, ce=ce, hae=hae)
        return event
