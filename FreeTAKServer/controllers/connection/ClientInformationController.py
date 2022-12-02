#######################################################
# 
# ClientInformationController.py
# Python implementation of the Class ClientInformationController
# Generated by Enterprise Architect
# Created on:      19-May-2020 6:56:00 PM
#
#######################################################
from FreeTAKServer.controllers.domian.BasicModelInstantiate import BasicModelInstantiate
import uuid
from FreeTAKServer.controllers.configuration.LoggingConstants import LoggingConstants
from FreeTAKServer.controllers.configuration.CreateLoggerController import CreateLoggerController
from FreeTAKServer.model.FTSModel.Event import Event
from FreeTAKServer.model.ClientInformation import ClientInformation
from FreeTAKServer.controllers.serializers.xml_serializer import XmlSerializer

loggingConstants = LoggingConstants(log_name="FTS_ClientInformationController")
logger = CreateLoggerController("FTS_ClientInformationController", logging_constants=loggingConstants).getLogger()

loggingConstants = LoggingConstants()

class ClientInformationController(BasicModelInstantiate):
    def __init__(self):
        pass
    '''
    connection setup is obsolete with intstantiateClientInformationModelFromController
    '''

    def intstantiateClientInformationModelFromConnection(self, rawClientInformation, queue):
        try:
            tempObject = Event.Connection()
            self.clientInformation = ClientInformation()
            argument = "initialConnection"
            self.clientInformation.dataQueue = queue
            self.clientInformation.socket = rawClientInformation.socket
            self.clientInformation.IP = rawClientInformation.ip
            self.clientInformation.idData = rawClientInformation.xmlString
            self.clientInformation.alive = 1
            self.clientInformation.ID = uuid.uuid1().int
            self.clientInformation.modelObject = XmlSerializer().from_format_to_fts_object(rawClientInformation.xmlString.encode(), tempObject)
            return self.clientInformation
        except Exception as e:
            logger.debug('error in client information controller '+str(e)+' '+str(rawClientInformation.xmlString))
            return -1