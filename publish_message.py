import paho.mqtt.client as mqtt
import time

############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################
broker_address="broker.hivemq.com"

print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback


print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop


print("Subscribing to a topic","parkingStand/cars/")
client.subscribe("parkingStand/cars/")


print("Publishing message to a topic","parkingStand/cars/")
client.publish("parkingStand/cars/","13-filled") # '13-filled' message indicates that  13th space is filled now


time.sleep(4) # wait
# client.loop_stop() #stop the loop