import serial

ser = serial.Serial('COM3', 9600, timeout=5)


#command = ''
#ser.write(command.encode('UTF-8'))

#b'\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\xef\x20'
#    ^first 2 bytes are the field ID         ^this byte is the command (ROTn_CMD_CFG_GET= config get?)
ser.write(b'\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\xef\x20')

response = ser.readline().decode().strip()
print(f"Response: {response}")

ser.close()
