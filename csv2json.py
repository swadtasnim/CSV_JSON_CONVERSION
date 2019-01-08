import csv
import pandas as pd
import pandasql as ps
import json

dt= pd.read_csv('results-20190108-013124.csv')
df=pd.DataFrame(dt)

route={}
year={}
month={}
day={}
Whitelisting_number={}
qq="""SELECT * FROM df  WHERE whitelisting_number = """+ "8801880084966"
bs=ps.sqldf(qq,globals())
basic_info={}
basic_info["area"]=str(bs["area"][0])
basic_info["distributor_code"]=str(bs["distributor_code"][0])
basic_info["imei"]=str(bs["imei"][0])
basic_info["name"]=str(bs["name"][0])
basic_info["region"]=str(bs["region"][0])
basic_info["territory"]=str(bs["territory"][0])


route["basic_info"]=basic_info
holiday=[4,11,18,25]
for p in range(28):
            k=p+1
            if k==4:
                continue
            q= """SELECT * FROM df WHERE  day="""+str(k)

            print(ps.sqldf(q, globals()))

            data=ps.sqldf(q, globals())

            
            """for i in data['wallet_no']:
                
                print( "\""+str(i)+"\"" + " : false,")




            year_key=input("Input year?")

            month_key=input("Input month?")

            day_key=input("Input day?")
            whitelisting_number_key=input("Input Whitelisting_number?")

            area=input("area")
            distrbutor_code=input("code")
            imei=input("imei")
            name=input("name")
            region=input("region")
            territory=input("territory")

            Whitelisting_number={}
            basic_info={}
            basic_info["area"]=data["area"][0]
            basic_info["distributor_code"]=data["distributor_code"][0]
            basic_info["imei"]=data["imei"][0]
            basic_info["name"]=data["name"][0]
            basic_info["region"]=data["region"][0]
            basic_info["territory"]=data["territory"][0]

            Whitelisting_number["basic_info"]=basic_info
            """

            merchandiser={}
            wallet_no={}
            merchandiser["attendance"]=0
          
            for i in data['wallet_no']:
                
                wallet_no[i]=False

            merchandiser["outlets"]=wallet_no
            merchandiser["selfieAttendance"]=""

            day_key=str(k)

            day[day_key]=merchandiser

month_key="01"
year_key="2019"
month[month_key]=day
year[year_key]=month
route["route"]=year
whitelisting_number_key="+8801880084966"



Whitelisting_number[whitelisting_number_key]=route


"""print(json.dumps(Whitelisting_number))"""

with open("data2.json","w") as outfile:
    json.dump(Whitelisting_number,outfile)



