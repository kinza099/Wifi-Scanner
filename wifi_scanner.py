import subprocess
devices=subprocess.check_output(['netsh' , 'wlan' ,'show' ,'networks'])
devices=devices.decode('ascii')
devices=devices.replace('\r',"")

# to write the the output in txt file:
with open("result.txt", 'w') as wf:
    wf.write(devices)

print(devices)

