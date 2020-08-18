"""
The following is a python script that takes a URL
input from the command line, and using the
'scapy' python library, creates a TCP SYN
request to the website with the ECN-Echo and
CWR flags set to 1. The script then receives the
response, and checks if the SYN+ACK+ECN bits are
set in the TCP flags of the response. If the SYN+ACK
bits are set, it indicates that this is the response 
we are looking for to check for server-side ECN support; 
if the ECN-Echo bit is set in this packet, it
indicates that the website supports ECN.

Writes the output to a file name ECN_Support.txt

This script supports multiple websites - enter multiple websites
as command line arguments to check their ECN support.

How to use:
Ensure you have python3.6+ installed

Install scapy by running
pip install --pre scapy[complete]

Usage: 
sudo python3 script.py [website_list]

Example:
sudo python3 script.py www.facebook.com www.twitter.com

"""

import sys  # to get the command line arguments
from scapy.all import *  # we will use the scapy library to create and receive
                         # the packets.


"""
This function creates and receives packets for 
all the websites entered in the command line
arguments, checks for their validity and returns
all the response packets.
"""
def get_packet(address):
    if len(address) == 0:
        print('Enter atleast one website!')
        return None

    recvd_pkts = []

    try:
        for website in address:
            p = sr1(IP(dst=website)/TCP(flags="SEC"))
            recvd_pkts.append(p)
    except:
        print(f'{website} is an invalid address!')  # if any of the websites entered are invalid.
        return None
    
    return recvd_pkts  # returns the list of received packets.


"""
This function checks if the packet received has
the correct TCP headers for ECN support set or not.
"""
def check_packet(p):  # this function checks if the correct TCP flags are
                      # set in the response packet.

    if p[TCP].flags == 'SAE':  # are the SYN + ACK + ECN bits set?
        return 'YES'
    else:
        return 'NO'


"""
Driver function for the program
"""
def main():
    address = sys.argv[1:]  # get all the websites entered as command
                            # line arguments in a list form.
    recvd_pkts = get_packet(address)

    if recvd_pkts is None:  # one or more addresses was incorrect.
        exit()

    ecn_support = []

    for packet in recvd_pkts:
        ecn_support.append(check_packet(packet))  # checks for ECN support and
                                                  # appends 'YES' or 'NO'

    # only after checking if all entered websites are valid and
    # getting the response packets from all of them, we
    # write to the file.
    with open("ECN_Support.txt", "a") as file:
        for i in range(len(ecn_support)):
            file.write(str(address[i]) + ' ' + recvd_pkts[i][IP].src + ' ' + ecn_support[i] + '\n')


# this program should only work when executed directly
# from the command line. When it is, the main() function
# is initially called with the help of the below code.
if __name__ == '__main__':  
    main()