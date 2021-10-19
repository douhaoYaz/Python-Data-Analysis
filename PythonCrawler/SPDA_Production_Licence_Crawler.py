import requests
import json
import re
import pandas as pd
from time import sleep

base_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
IDlist = []

for page in range(1,2):
    data = {
        'on': 'true',
        'page': page,
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': ''
    }

    restext = requests.post(base_url, headers=headers,data=data)
    restext = restext.json()
    for id in restext['list']:
        IDlist.append(id['ID'])
print(IDlist)

url=r'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'

data_list = []

for id in IDlist:
    data = {'id':id}
    res_json = requests.post(url, headers=headers, data=data).json()
    print(res_json)
    data_list.append(res_json)
    sleep(1)

alldata=pd.DataFrame(data_list)

alldata.to_excel('化妆品生产许可证信息.xlsx')

print('下载完成!')
