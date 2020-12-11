from netmiko import ConnectHandler
from getpass import getpass
passwd = getpass('Password : ')
device  = {
    'device_type' : 'cisco_ios',
    'ip' : '10.215.26.214',
    'username' : 'admin',
    'password' : '123',
    'secret' : '321'
}

# device1  = {
#     'device_type' : 'cisco_ios',
#     'ip' : '10.215.26.214',
#     'username' : 'admin',
#     'password' : '123',
#     'secret' : '321'
# }

ssh = ConnectHandler(**device)
ssh.enable()
for i in range (10,21):
    ssh.send_config_set(['int vlan {}'.format(i),'ip add 10.1.{}.1 255.255.255.0'.format(i),'no sh'])
print(ssh.send_command('sh ip  int br'))
ssh.disconnect()

# list_device = [device,device1]
# for device in list_device:
#     ssh = ConnectHandler(**device)
#     ssh.enable()
#     #print('========='+ device['IP']+'======')
#     print('===== {} ====='.format(device['ip']))
#     print(ssh.send_command('sh ip int br'))
#     ssh.disconnect()

ssh = ConnectHandler(**device)
ssh.enable()
#send_command()
#send_config_set()
#print(ssh.send_config_set('hostname Bi'))
data = ssh.send_config_set('hostname Bi')
# Cach mo file log 1
# file_log = open('log.txt','w')
# file_log = open('log.txt','a')
# file_log.write(data)
# file_log.close()

# Cach mo file log 2
# with open('log.txt','w') as file_log:
#     file_log.write(data)
# output = ssh.find_prompt()
# print(output)



cmd = [
    'int e0/3','no sw','ip add 192.168.0.1 255.255.255.0','no sh'
]
ssh.send_config_set(cmd)
#print(ssh.send_config_set('do sho ip int br'))
print(ssh.send_command('sho ip int br'))
ssh.disconnect()

