import sys
import time                                                                          
from beautifulhue.api import Bridge                                                 
username = 'newdeveloper'                                                       
bridge = Bridge(device={'ip':'192.168.0.100'}, user={'name':username})

# def createConfig():                                                                 
#     created = False                                                                 
#     print 'Press the button on the Hue bridge'                                      
#     while not created:                                                              
#         resource = {'user':{'devicetype': 'beautifulhuetest', 'name': username}}    
#         response = bridge.config.create(resource)['resource']                       
#         if 'error' in response[0]:                                                  
#             if response[0]['error']['type'] != 101:                                 
#                 print 'Unhandled error creating configuration on the Hue'           
#                 sys.exit(response)                                                  
#         else:                                                                       
#             created = True                                                          

# def getSystemData():                                                                    
#   resource = {'which':'system'}                                                     
#   return bridge.config.get(resource)['resource']                                    

def main():
   turnOnAll()
   time.sleep(2)
   turnOffAll()
   time.sleep(2)
   turnOnAll()

def turnOnAll():
    for i in range(1,5):
        resourceOn = {
        'which':i,
        'data':{
            'state':{'on':True, "sat":255, "bri":255,"hue":10000}
            }
        }
        bridge.light.update(resourceOn)

def turnOffAll():
    for i in range(1,5):
        resourceOff = {
        'which':i,
        'data':{
            'state':{'on':False}
            }
        }
        bridge.light.update(resourceOff)

main()     