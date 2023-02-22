import json
print(r'''Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------''')
f = open("C:\\Users\Валихан\Desktop\pp2\pp2\lab4\sample-data.json")
data = json.loads(f.read())
for i in data['imdata']:
    parsed_data = parsed_data.append({"DN":i['l1PhysIf']['attributes']['dn'],
        "Description":i['l1PhysIf']['attributes']['descr'],
        "Speed":i['l1PhysIf']['attributes']['speed'],
        "MTU":i['l1PhysIf']['attributes']['mtu']},ignore_index=True)
print(parsed_data)