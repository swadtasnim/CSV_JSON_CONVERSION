import csv
import pandas as pd
import pandasql as ps
import json

dt= pd.read_csv('results-20190108-013124.csv', dtype=str)
df=pd.DataFrame(dt)

day_key=df["day"].unique()
print(day_key)
month_key=df["month"].unique()
print(month_key)
year_key=df["year"].unique()
print(year_key)




white_list=df["whitelisting_number"].unique()



print(white_list)

Whitelisting_number={}

for y in year_key:
    for m in month_key:
        for w in white_list:
            route={}
            year={}
            month={}
            day={}
            

            basic=df[df.whitelisting_number==w]

            basic_info={}
            basic_info["area"]=basic["area"][0]
            basic_info["distributor_code"]=basic["distributor_code"][0]
            basic_info["imei"]=basic["imei"][0]
            basic_info["name"]=basic["name"][0]
            basic_info["region"]=basic["region"][0]
            basic_info["territory"]=basic["territory"][0]


            route["basic_info"]=basic_info
            
            for d in day_key:


                        data=df[df.day==d]



                        merchandiser={}
                        wallet_no={}
                        merchandiser["attendance"]=0
                    
                        for i in data['wallet_no']:
                            
                            wallet_no[i]=False

                        merchandiser["outlets"]=wallet_no
                        merchandiser["selfieAttendance"]=""

                        

                        day[d]=merchandiser


            month[m]=day
            year[y]=month
            route["route"]=year
            whitelisting_number_key=w
            print(whitelisting_number_key)



            Whitelisting_number[whitelisting_number_key]=route


"""print(json.dumps(Whitelisting_number))"""

with open("data2.json","w") as outfile:
    json.dump(Whitelisting_number,outfile)



