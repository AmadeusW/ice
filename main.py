import sys, argparse
from SerialDeviceConnector import SerialDeviceConnector
from Dashboard import Dashboard

def main():
    parser = argparse.ArgumentParser(description='Serial Device Simulator')
    parser.add_argument('port', type=str, help='Path to the serial port')
    parser.add_argument('--baudrate', type=int, default=115200, 
                        help='Baud rate (default: 115200)')
    try:
        args = parser.parse_args()
    except Exception as e:
        print(f"Argument parsing error: {e}")
        sys.exit(1)

    try:
        device = SerialDeviceConnector(args.port, baudrate=args.baudrate)
        configuration = Configuration('icecold.yaml')
        dashboard = Dashboard(device, configuration)
        dashboard.begin_session()
    except Exception as e:
        print(f"Error in main: {e}")
    finally:
        device.close()

if __name__ == "__main__":
    main()
