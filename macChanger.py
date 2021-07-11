#!/usr/bin/python
import subprocess
import optparse
import string
import random
import threading
import time

alphabet = [x for x in string.ascii_uppercase[:6]]
number = [x for x in range(10)]
allList = alphabet + number
valid = ['2','6','A','E'] # first octet should be even


def get_arguments():
    # get arguments from cli
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-o", "--mode", dest="mode", help="Mode:\n0.random(specify time interval to change the MAC) \n1. Manual(specify the new MAC)")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    parser.add_option("-t", "--time", dest="delay", help="MAC will change depending on this time interval(sec)")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Specify interface, use --help for more info.")
    if not options.mode:
        parser.error("[-] Specify mode, use --help for more info.")
    if options.mode == '0' and not options.delay:
        parser.error("[-] Random MAC mode need time interval to change the MAC")
    if options.mode == '1' and not options.new_mac:
        parser.error("[-] Manual mode need the new MAC address")
    return options


def generate_mac(allList):
    newMac = ""
    for _ in range(6):
        newMac +=  str(random.choice(allList))+str(random.choice(allList))+":"
    if check_value(newMac[:2]) is True:
        if newMac is not None:
            return newMac[:17]
    else:
        generate_mac(allList)


def check_value(char):
    if char[1] in valid:
        return True
    else:
        return False


def change_mac(interface, new_mac):
    print(f"Changing MAC address for {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw",  "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


if __name__ == '__main__':
    options = get_arguments()
    if options.mode == '0':
        while True:
            ranMac = generate_mac(allList)
            if ranMac is not None:
                change_mac(options.interface, ranMac)
                time.sleep(int(options.delay))
    elif options.mode == '1':
        change_mac(options.interface, options.new_mac)
