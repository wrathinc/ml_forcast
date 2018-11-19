from netmiko import ConnectHandler
ip = 
cisco_881 = {
    'device_type': 'cisco_ios',
    'ip':   '10.10.10.10',
    'username': 'test',
    'password': 'password',
}

net_connect = ConnectHandler(**cisco_881)
output = net_connect.send_command('show ip int brief')
print output