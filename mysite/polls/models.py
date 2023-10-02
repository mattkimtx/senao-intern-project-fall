from django.db import models

#     category = models.CharField(max_length=100)
     # subTypeNew = models.CharField(max_length=100)
     # eventID = models.CharField(max_length=100)

class logFileUnfiltered(models.Model):
     ## default
     # id = models.BigAutoField(primary_key=True) 
     category = models.CharField(max_length=100)
     subType = models.CharField(max_length=100)
     eventID = models.CharField(max_length=100)
     eventTitle = models.CharField(max_length=100)
     priority = models.CharField(max_length=100)
     source = models.CharField(max_length=100)
     description = models.CharField(max_length=100)
     details = models.CharField(max_length=100)
     details2 = models.CharField(max_length=100)
     JSON = models.CharField(max_length=100)
     JSON2 = models.CharField(max_length=100)
     ## Each below are basically booleans. Could make tables for each of their values, but might be difficult
     clientTimelineTitle = models.CharField(max_length=100)
     APPdestination = models.CharField(max_length=100)
     AlertLicense = models.CharField(max_length=100)
     ESIndex =  models.CharField(max_length=100)
     APAlertLicenseBasic = models.CharField(max_length=100)
     APAlertLicensePro = models.CharField(max_length=100)
     APAlertLicenseProV = models.CharField(max_length=100)
     APAlertLicenseProR = models.CharField(max_length=100)
     switchAlertLicenseBasic = models.CharField(max_length=100)
     switchAlertLicensePro = models.CharField(max_length=100)
     switchAlertLicenseProV = models.CharField(max_length=100)
     switchAlertLicenseProR = models.CharField(max_length=100)
     GatewayAlertLicenseBasic = models.CharField(max_length=100)
     GatewayAlertLicensePro = models.CharField(max_length=100)
     GatewayAlertLicenseProV = models.CharField(max_length=100)
     GatewayAlertLicenseProR = models.CharField(max_length=100)
     PDUAlertLicenseBasic = models.CharField(max_length=100)
     PDUAlertLicensePro = models.CharField(max_length=100)
     PDUAlertLicenseProV = models.CharField(max_length=100)
     PDUAlertLicenseProR = models.CharField(max_length=100)
     SwitchExtenderAlertLicensePro = models.CharField(max_length=100)
     GatewayAlertLicenseSPC = models.CharField(max_length=100)

class allLogs(models.Model):
     

# Create your models here
class deviceEvent(models.Model):
     ## default
     # id = models.BigAutoField(primary_key=True)
     time = models.DateTimeField()
     deviceID = models.CharField(max_length=100)
     deviceType = models.CharField(max_length=10) ### EX: AP1
     SSID = models.CharField(max_length=100)
     clientType = models.CharField(max_length=100)
     clientIP = models.CharField(max_length=100) #
     eventType = models.CharField(max_length=100)
     description = models.CharField(max_length=100)

class systemEvent(models.Model):
     ## default
     # id = models.BigAutoField(primary_key=True)
     time = models.DateTimeField()
     eventType = models.CharField(max_length=100)
     target = models.CharField(max_length=100)
     description = models.CharField(max_length=100)
     admin = models.CharField(max_length=100)
     
class changeLog(models.Model):
     ## default
     # id = models.BigAutoField(primary_key=True)
     time = models.DateTimeField()
     SSID = models.CharField(max_length=100)
     eventType = models.CharField(max_length=100)
     page = models.CharField(max_length=100) 
     description = models.CharField(max_length=100)
     admin = models.CharField(max_length=100)