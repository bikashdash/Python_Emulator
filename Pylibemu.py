#!/usr/bin/python
import sys
import pylibemu
print "************Shellcode Emulation********************"
print"Wellcome to the Python Emulaton section"
def greet():
        print
        greet = "Author: Bikash Dash (www.vulnerableghost.com)"
        print "\t\t"+"*"*(len(greet)+18)
        print "\t\t"+"*\t"+greet+"\t\t*"
        print "\t\t"+"*"*(len(greet)+18)
def emu():
        data = ""
        try:
                for line in sys.stdin.readlines():
        #               if len(sys.argv)<1:
         #                      print "enter the input in hex format(/x format)%s",input
          #                     sys.exit(0)

                        data += line
        except e:
                print "error"
        print "[+]testing data of size %dB......"% (len(data))
        emu = pylibemu.Emulator()
        offset = emu.shellcode_getpc_test(data)
        if offset >=0:
                print "[+] IS SHELLCODE!"
        else:
                print "[-] IS Not A SHELLCODE"
