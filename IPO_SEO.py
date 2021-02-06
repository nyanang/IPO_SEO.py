#1st step: Collecting Business Group Data

import requests, xmltodict, json
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib import parse
import json
import openpyxl


file = open("./BG_01_11.json", "a")

start = 2001
end = 2011

KEY = //

for year in range(start, end):
    url = ("http://apis.data.go.kr/1130000/affiCompList/affiliationCompList?serviceKey={}&presentnYear="+str(year)+"&numOfRows=5000&pageNo=1&_type=json xml, json").format(KEY)

    content = requests.get(url).content
    dict = xmltodict.parse(content)
    jsonString = json.dumps(dict['affiCompList'], ensure_ascii=False)
    jsonObj = json.loads(jsonString)


    for item in jsonObj['affiComp']:
        print(item)
    item = json.dumps(jsonObj['affiComp'])
    # if year is end - 1:
    #     0
    # else:
    #     if year is start :
    #         item = item[1:item.len - 1] + ","
    #     elif year is end - 1 :
    #         item = item[1:item.len]
    file.write(item)
file.close()


def save(df, filename):
    writer  = pd.ExcelWriter(filename)
    df.to_excel(writer,"sheet")
    writer.save()

df = pd.read_json("./BG_01_11.json") ##문제 발생!!
#print(df.count())
save(df, "BG_01_11.xlsx")


