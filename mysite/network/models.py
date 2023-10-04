from django.db import models

#     category = models.CharField(max_length=100)
     # subTypeNew = models.CharField(max_length=100)
     # eventID = models.CharField(max_length=100)
maxChar = 100

class logFileUnfiltered(models.Model):
     ## default
     # id = models.BigAutoField(primary_key=True) 
     category = models.CharField(max_length=maxChar)
     subType = models.CharField(max_length=maxChar)
     eventID = models.CharField(max_length=maxChar, uniqute = True)
     eventTitle = models.CharField(max_length=maxChar)
     priority = models.CharField(max_length=maxChar)
     source = models.CharField(max_length=maxChar)
     description = models.CharField(max_length=maxChar)
     details = models.CharField(max_length=maxChar)
     details2 = models.CharField(max_length=maxChar)
     JSON = models.CharField(max_length=maxChar)
     JSON2 = models.CharField(max_length=maxChar)
     ## Each below are basically booleans. Could make tables for each of their values, but might be difficult
     clientTimelineTitle = models.CharField(max_length=maxChar)
     APPdestination = models.CharField(max_length=maxChar)
     AlertLicense = models.CharField(max_length=maxChar)
     ESIndex =  models.CharField(max_length=maxChar)
     APAlertLicenseBasic = models.CharField(max_length=maxChar)
     APAlertLicensePro = models.CharField(max_length=maxChar)
     APAlertLicenseProV = models.CharField(max_length=maxChar)
     APAlertLicenseProR = models.CharField(max_length=maxChar)
     switchAlertLicenseBasic = models.CharField(max_length=maxChar)
     switchAlertLicensePro = models.CharField(max_length=maxChar)
     switchAlertLicenseProV = models.CharField(max_length=maxChar)
     switchAlertLicenseProR = models.CharField(max_length=maxChar)
     GatewayAlertLicenseBasic = models.CharField(max_length=maxChar)
     GatewayAlertLicensePro = models.CharField(max_length=maxChar)
     GatewayAlertLicenseProV = models.CharField(max_length=maxChar)
     GatewayAlertLicenseProR = models.CharField(max_length=maxChar)
     PDUAlertLicenseBasic = models.CharField(max_length=maxChar)
     PDUAlertLicensePro = models.CharField(max_length=maxChar)
     PDUAlertLicenseProV = models.CharField(max_length=maxChar)
     PDUAlertLicenseProR = models.CharField(max_length=maxChar)
     SwitchExtenderAlertLicensePro = models.CharField(max_length=maxChar)
     GatewayAlertLicenseSPC = models.CharField(max_length=maxChar)
     def __str__(self):
          return self.logFileUnfiltered

# class allLogs(models.Model):

# Create your models here
class deviceEvent(models.Model):
     ## default
     # id = models.BigAutoField(primary_key=True)
     time = models.DateTimeField("Access Date")
     deviceID = models.CharField(max_length=maxChar)
     deviceType = models.CharField(max_length=maxChar) ### EX: AP1
     SSID = models.CharField(max_length=maxChar)
     clientType = models.CharField(max_length=maxChar)
     clientIP = models.CharField(max_length=maxChar) #
     eventType = models.CharField(max_length=maxChar)
     description = models.CharField(max_length=maxChar)
     def __str__(self):
          return self.deviceEvent

class systemEvent(models.Model):
     ## default
     # id = models.BigAutoField(primary_key=True)
     time = models.DateTimeField()
     eventType = models.CharField(max_length=maxChar)
     target = models.CharField(max_length=maxChar)
     description = models.CharField(max_length=maxChar)
     admin = models.CharField(max_length=maxChar)
     def __str__(self):
          return self.systemEvent

class changeLog(models.Model):
     ## default
     # id = models.BigAutoField(primary_key=True)
     time = models.DateTimeField()
     SSID = models.CharField(max_length=maxChar)
     eventType = models.CharField(max_length=maxChar)
     page = models.CharField(max_length=maxChar) 
     description = models.CharField(max_length=maxChar)
     admin = models.CharField(max_length=maxChar)
     def __str__(self):
          return self.changeLog