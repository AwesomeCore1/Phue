from phue import Bridge
from utils.secrets import BRIDGE_IP

bridge = Bridge(BRIDGE_IP)
bridge.connect()

lights = bridge.get_light_objects("name")

def get_lights():
    return lights