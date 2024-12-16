import time
from SerialDeviceConnector import SerialDeviceConnector

class Dashboard:
    def __init__(self, device):
        self.device = device

    def begin_session(self):
        # INIT is just an example
        self.device.send_command("INIT")
        time.sleep(0.5)
        self.device.read_response()
        
        # Start interactive session
        self.device.interactive_session()
