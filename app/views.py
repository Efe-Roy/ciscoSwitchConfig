from django.shortcuts import render
from netmiko import ConnectHandler
from .forms import CiscoSwitchForm

def configure_switch(request):
    device = {
    "device_type": "cisco_ios",
    "host": "router01",
    "username": "username",
    "password": "password"}

    form = CiscoSwitchForm()

    if request.method == 'POST':
        form = CiscoSwitchForm(request.POST)
        if form.is_valid():
            cd_device = form.cleaned_data
            print(cd_device)
            
            net_connect = ConnectHandler(**cd_device)
            config_commands = ['interface fastEthernet 0/1', 'switchport mode access', 'switchport access vlan 10']
            output = net_connect.send_config_set(config_commands)
            print(output)
            net_connect.disconnect()
            
            return render(request, 'switch_config.html', {'output': output, 'form': form})
    else:
        form = CiscoSwitchForm()

    return render(request, 'switch_config.html', {'form': form})
    # return render(request, 'switch_config.html', {'output': output, 'form': form})
