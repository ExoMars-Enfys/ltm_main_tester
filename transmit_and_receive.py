import serial.rs485


def initialise_rs485(com_port: str) -> serial.rs485.RS485:
    # create a blank RS485 class ready to open as per OB EGSE
    port = serial.rs485.RS485(
        port=None,
        baudrate=115200,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_ONE,
        timeout=10,
    )

    port.rs485_mode = serial.rs485.RS485Settings(
        rts_level_for_tx=False,
        rts_level_for_rx=True,
        loopback=False,
        delay_before_tx=0,
        delay_before_rx=0,
    )

    port.port = com_port  # Assign com_port afterwards to prevent opening immediately
    port.open()

    port.flushOutput()  # Port Flushing to clear port
    port.flushInput()

    return port


def read_rs485(port: serial.rs485.RS485) -> None:
    data = port.read(5)  # Read 100 bytes from the RS485 port
    if data:
        print(f"Received: {data}")  # Process the received data as needed


def close_rs485(port: serial.rs485.RS485) -> None:
    port.close()
    return


def initialise_teensy(com_port: str) -> serial.Serial:
    ten_port = serial.Serial(
        port=com_port,
        baudrate=115200,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_ODD,
        timeout=1.0,
    )
    return ten_port


def main():
    rs_485_com = "COM10"  # Example COM port for RS485, change as needed
    teensy_com = "COM5"  # Example Teensy COM port, change as needed

    transmit_text = b"12345"

    rs485_port = initialise_rs485(rs_485_com)
    teensy_port = initialise_teensy(teensy_com)

    while True:
        print("\n Select serial command:\n 1. LTM Receiving\n 2. LTM Transmit\n 3. Exit\n")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            print("LTM Receiving...")
            print(f"Writing to RS485 port: {transmit_text}")
            rs485_port.write(transmit_text)
        elif choice == "2":
            print("LTM Transmitting...")
            teensy_port.write(transmit_text)
            read_rs485(rs485_port)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

    close_rs485(rs485_port)  # Close the RS485 port
    teensy_port.close()  # Close the Teensy port


if __name__ == "__main__":
    main()
