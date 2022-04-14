import yaml
from collections import OrderedDict

file_name = 'fdevsec.yaml'

appid='75b7731d-c8fa-4f0a-b742-d1c38233a915'

with open(file_name, "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print(type(data))
    data['id']['app']=appid
    print("Read successful")
    print(data)
    yamlfile.close()

with open(file_name, 'w') as yamlfile:
    data1 = yaml.dump(data, yamlfile,sort_keys=False)
    print(data)
    print("Write successful")
    yamlfile.close()
