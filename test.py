from phue import Bridge

bridge = Bridge("192.168.178.11")

lights = bridge.get_light_objects('name')

lights["Rick"].on = True
lights["Rick"].hue = 16000
lights["Rick"].saturation = 150
lights["Rick"].brightness = 250