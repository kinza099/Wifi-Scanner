import subprocess

# show all wlan 
devices=subprocess.check_output(['netsh' , 'wlan' ,'show' ,'profile', "key=clear"])
devices=devices.decode('ascii')
devices=devices.replace('\r',"")


# to write the the output in txt file:
with open("saved_passwords.txt", 'w') as wf:
    wf.write(devices)

print(devices)

