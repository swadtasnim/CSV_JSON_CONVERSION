import csv
import pandas as pd
import pandasql as ps
import json
from pandas.io.json import json_normalize

dayin=input("day?")
"""
def get_leaves(item, key=None):
    if isinstance(item, dict):
        leaves = []
        for i in item.keys():
            
            leaves.extend(get_leaves(item[i], i))
        return leaves
    elif isinstance(item, list):
        leaves = []
        for i in item:
            leaves.extend(get_leaves(i, key))
        return leaves
    else:
        return [(key, item)]


def flattenjson( b, delim ):
    val = {}
    for i in b.keys():
        if isinstance( b[i], dict ):
            get = flattenjson( b[i], delim )
            for j in get.keys():
                val[ i + delim + j ] = get[j]
        else:
            val[i] = b[i]

    return val

"""

with open('campaign_supervisor.json') as data_file:    
    dt = json.load(data_file) 


lst_whtlst=[]
for k in dt.keys():
    print(k)
    lst_whtlst.append(k)

"""print(dt["+8801880084966"]["route"]["2019"]["01"]["1"]["outlets"])
 
 """
holiday=[4,11,18,25]

col=["imei","name","year","month","day","territory","area","distributor_code","whitelisting_number","region","wallet_no"]

ddd=[]
for wh in lst_whtlst:
    wh=str(wh)
    for i in range(int(dayin)-1,int(dayin)):
    
        p=i+1
        if p in holiday:
           continue
        day="0"+str(p)
        print("day "+ day+ "\n")
        basic= dt[wh]["basic_info"]
        print(basic)
        outlets=dt[wh]["route"]["2019"]["01"][day]["outlets"]
    
        for k in outlets.keys():
            print(k+" "+ str(outlets[k]))
            lst=[]

            lst.extend([basic["imei"],basic["name"],"2019","01",day,basic["territory"],basic["area"],basic["distributor_code"],wh,basic["region"],k])

            ddd.append(lst)    


        print("\n")  
ddd=pd.DataFrame(ddd,columns=col)



print(ddd)

ddd.to_csv('output.csv')








