import json
import requests
import csv

payload = {'username':'fortidevsecqa0007@qatest.com','password':'Fortinet@2015'}
r4 = requests.post('https://fortidevsec.forticloud.com/api/v1/login/access-token', verify=False,data=payload)
print (r4.json())
print("status_code-",r4.status_code)

if(r4.status_code == requests.codes.ok):
    print("status code True")

print("Headers-",r4.headers)

r4_data = json.loads(r4.text)
print("r4_data --> ",r4_data)
print("json_data-",r4_data['access_token']);

headers_details={'Authorization': r4_data['token_type'] + ' ' + r4_data['access_token'],'accept':r4.headers['Content-Type']}
print("headers_details",headers_details)
r5 = requests.get('https://fortidevsec.forticloud.com/api/v1/dashboard/get_orgs',headers=headers_details,verify=False)
#print (r5.json())
r5_data = json.loads(r5.text)
print("r5_data --> ",r5_data)

params_data  = {'org_id': r5_data[0]['id']}
print("payload-->",payload)

headers_details={'Authorization': r4_data['token_type'] + ' ' + r4_data['access_token'],'accept':r4.headers['Content-Type']}
r6 = requests.get('https://fortidevsec.forticloud.com/api/v1/dashboard/get_apps', headers=headers_details, params = params_data, verify=False)
print (r6.json())
item_dict = json.loads(r6.text)
appCount=len(item_dict['apps'])

for x in range(appCount):
    app_id=item_dict['apps'][x]['id']
    print("app_id",app_id)
    r7 = requests.post('https://fortidevsec.forticloud.com/api/v1/dashboard/delete_app', headers=headers_details, params = {'app_id':app_id}, verify=False)
    #print (r7.text)

#params_data  = {'app_name':"naren",'org_id': r5_data[0]['id']}
#print("payload-->",payload)

#headers_details={'Authorization': r4_data['token_type'] + ' ' + r4_data['access_token'],'accept':r4.headers['Content-Type']}
#r7 = requests.post('https://qa.fortidevsec.forticloud.com/api/v1/dashboard/create_app', headers=headers_details, params = params_data, verify=False)
#print (r7.json())
