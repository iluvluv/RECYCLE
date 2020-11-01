import serial, requests

print('serial ' + serial.__version__) # Set a PORT Number & baud rate 
PORT = '/dev/cu.usbmodem141201' 
BaudRate = 9600 

ARD= serial.Serial(PORT,BaudRate)


while(True):
    if ARD.readable(): 
        LINE = ARD.readline() 
        print(LINE)
        requests.post("http://localhost:8000/update/", data={"data": LINE})
