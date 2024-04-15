def main():
    import serial.tools.list_ports
    import os
    import sys

    print('Your operating system is: ' + str(sys.platform))
    
    ports = serial.tools.list_ports.comports()
    
    for port, desc, hwid in sorted(ports):
            #print("{}: {} [{}]".format(port, desc, hwid))
            #print("{}: {}".format(port, desc))
            print("{}".format(port))
    
    #print("Hit Any Key to continue...")
    #input()

main()