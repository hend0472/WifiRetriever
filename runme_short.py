import re
import sys
import subprocess

profiled = []   # list for the initial list of connected networks
i = 0


print ("Finding previously used Wifi Networks\n")
k=subprocess.Popen(['netsh', 'wlan', 'show', 'profiles'],stdout=subprocess.PIPE)
profiles=re.findall(b': (.*)\r',k.communicate()[0])
for x in profiles:
    x=str(x)
    x=x[2:]
    x=str(x[:-1])
    profiled.append(str(x))
    i = i + 1

k.terminate()
k.kill()

def get_password():
    for i in profiled:
        command = 'name=' + '' + str(i) + ''
        mega_command = 'netsh wlan show profiles ' + str(command) + ' key=clear'
        second_command = 'show profiles ' + str(command) + ' key=clear'
        l=subprocess.Popen(['netsh', 'wlan', 'show', 'profiles', command, 'key=clear'],stdout=subprocess.PIPE)
        output=re.findall(b'Key Content[\s]+: (.*?)\r',l.communicate()[0])       # this is the second try
        
        for yep in output:
            yep=str(yep)
            yep=yep[2:]
            yep=yep[:-1]
            print('Network Name:  ' + str(i)) 
            print('Password:      ' + str(yep))
            print('\n')
            profiled.remove(i)
        l.terminate()
        l.kill()

def get_password2():
    for i in profiled:
        command = 'name=' + '"' + str(i) + '"'
        mega_command = 'netsh wlan show profiles ' + str(command) + ' key=clear'
        second_command = 'show profiles ' + str(command) + ' key=clear'
        l=subprocess.Popen(['netsh', 'wlan', 'show', 'profiles', command, 'key=clear'],stdout=subprocess.PIPE)
        output=re.findall(b'Key Content[\s]+: (.*?)\r',l.communicate()[0])       # this is the second try
        
        for yep in output:
            yep=str(yep)
            yep=yep[2:]
            yep=yep[:-1]
            print('Network Name:  ' + str(i)) 
            print('Password:      ' + str(yep))
            print('\n')
            profiled.remove(i)
        l.terminate()
        l.kill()

get_password()
get_password2()

check = input("Press Enter to Exit.")