import serial

class SerialDeviceConnector:
    def __init__(self, port_path, baudrate=115200, timeout=1):
        """
        Initialize serial connection to the virtual port
        
        :param port_path: Path to the virtual serial port 
        :param baudrate: Communication speed (default 115200)
        :param timeout: Read timeout in seconds
        """
        try:
            self.ser = serial.Serial(
                port=port_path,
                baudrate=baudrate,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=timeout
            )
            print(f"Connected to serial port: {port_path}")
        except serial.SerialException as e:
            print(f"Error connecting to serial port: {e}")
            raise

    def send_command(self, command):
        """
        Send a command to the serial device
        
        :param command: Command string to send
        """
        try:
            # Ensure command ends with newline if needed
            if not command.endswith('\n'):
                command += '\n'
            
            # Convert to bytes and send
            self.ser.write(command.encode('utf-8'))
            #print(f"Sent command: {command.strip()}")
        except Exception as e:
            print(f"Error sending command: {e}")

    def read_response(self, max_bytes=1024):
        """
        Read response from the serial device
        
        :param max_bytes: Maximum bytes to read
        :return: Decoded response string
        """
        try:
            # Read available bytes
            response = self.ser.read(max_bytes)
            
            if response:
                decoded_response = response.decode('utf-8').strip()
                #print(f"Received response: {decoded_response}")
                return decoded_response
            else:
                #print("No response received")
                return None
        except Exception as e:
            print(f"Error reading response: {e}")
            return None

    def interactive_session(self):
        """
        Start an interactive session for sending commands
        """
        print("Starting interactive serial device simulation.")
        print("Type commands to send, 'quit' to exit.")
        
        while True:
            try:
                # Get user input
                user_input = input("Enter command (or 'quit'): ")
                
                # Exit condition
                if user_input.lower() == 'quit':
                    break
                
                # Send command
                self.send_command(user_input)
                
                # Read response
                response = self.read_response()
                
            except KeyboardInterrupt:
                print("\nSession interrupted. Exiting.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

    def close(self):
        """
        Close the serial connection
        """
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("Serial port connection closed.")
