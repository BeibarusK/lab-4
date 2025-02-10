import json


with open('data.json', 'r') as file:
    data = json.load(file)
data1 = """
Interface Status
================================================================================
DN                                                 Description           Speed   MTU  
--------------------------------------------------  -------------------  ------ ------
"""
print(data1)
for i in data['imdata']:
    print(i['l1PhysIf']['attributes']['dn'],end="          ")
    print(i['l1PhysIf']['attributes']['descr'],end="                    ")
    print(i['l1PhysIf']['attributes']['speed'],end="   ")
    print(i['l1PhysIf']['attributes']['mtu'])
