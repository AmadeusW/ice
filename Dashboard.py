import time, curses
from SerialDeviceConnector import SerialDeviceConnector

class Dashboard:
    def __init__(self, device):
        self.device = device

    def curses_loop(self, stdscr):
        # Enable keypad mode
        stdscr.keypad(True)

        # Initial state
        # TODO: should be a class, ideally dynamically created from configuration
        state = {'flag1': True, 'flag2': False, 'value': 10}

        # Display static instructions (only once)
        stdscr.addstr(4, 0, "Press '1' to toggle Flag1, '2' to toggle Flag2, '+' to increment Value, '-' to decrement Value, 'q' to quit.")
        stdscr.refresh()

        while True:
            try:
                stdscr.addstr(0, 0, f"Flag1: {'ON' if state['flag1'] else 'OFF'}   ")  # Trailing spaces erase leftovers
                stdscr.addstr(1, 0, f"Flag2: {'ON' if state['flag2'] else 'OFF'}   ")
                stdscr.addstr(2, 0, f"Value: {state['value']}   ")
                stdscr.refresh()

                # Get user input
                key = stdscr.getch()

                # Update state based on input
                if key == ord('1'):
                    state['flag1'] = not state['flag1']
                elif key == ord('2'):
                    state['flag2'] = not state['flag2']
                elif key == ord('+'):
                    state['value'] += 1
                elif key == ord('-'):
                    state['value'] -= 1
                elif key == ord('q'):
                    break

                # Send state to the device
                serialized_state = f"{int(state['flag1'])} {int(state['flag2'])} {state['value']}"
                stdscr.addstr(5, 0, f"Sending: {serialized_state}")
                stdscr.refresh()
                self.device.send_command(serialized_state)

                # Read response
                response = self.device.read_response()
                stdscr.addstr(6, 0, f"Response: {response}")
                stdscr.refresh()

            except KeyboardInterrupt:
                print("\nSession interrupted. Exiting.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

    def begin_session(self):
        # INIT is just an example
        self.device.send_command("INIT")
        time.sleep(0.5)
        self.device.read_response()
        
        # Start interactive session
        # EDIT: commented out because we'll use CURSES approach
        # self.device.interactive_session()
        curses.wrapper(self.curses_loop)
