import pandas as pd
import json
from pathlib import Path
json_files = ["C:/Users/86183/Documents/WeChat Files/wxid_ot8jppgzo67v22/FileStorage/File/2024-07/先锋.json",
              "C:/Users/86183/Documents/WeChat Files/wxid_ot8jppgzo67v22/FileStorage/File/2024-07/近卫男.json",
               "C:/Users/86183/Documents/WeChat Files/wxid_ot8jppgzo67v22/FileStorage/File/2024-07/近卫女.json",
               "C:/Users/86183/Documents/WeChat Files/wxid_ot8jppgzo67v22/FileStorage/File/2024-07/狙击.json",
               "C:/Users/86183/Documents/WeChat Files/wxid_ot8jppgzo67v22/FileStorage/File/2024-07/术师.json",
               "C:/Users/86183/Documents/WeChat Files/wxid_ot8jppgzo67v22/FileStorage/File/2024-07/医疗.json",
               "C:/Users/86183/Documents/WeChat Files/wxid_ot8jppgzo67v22/FileStorage/File/2024-07/重装.json",
               "C:/Users/86183/Documents/WeChat Files/wxid_ot8jppgzo67v22/FileStorage/File/2024-07/辅助.json",
               "C:/Users/86183/Documents/WeChat Files/wxid_ot8jppgzo67v22/FileStorage/File/2024-07/特种.json"]
all_data=[]
for file in json_files:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        all_data.extend(data)  # 将当前 JSON 文件的数据扩展到 all_data 列表中
df = pd.DataFrame(all_data)
data=df.rename(columns={
    'cname':'中文名',
    'ename':'英文名',
    'jname':'日文名',
    'code':'编号',
    'sub_occupation':'子职业',
    'influnce':'归属势力',
    'place_of_birth':'出生地',
    'race':'种族',
    'hp':'血量',
    'atk':'攻击',
    'defe':'物防',
    'res':'法防',
    're_deploy':'再部署时间',
    'cost':'费用',
    'block':'阻挡数',
    'interval':'攻速',
    'sex':'性别',
    'position':'定位',
    'obtain':'获取方式',
    'tag':'标签',
    'feature':'特性'
    })
data.to_excel('干员总览.xlsx', index=False)  # 如果不需要保存索引列，可以设置index参数为False