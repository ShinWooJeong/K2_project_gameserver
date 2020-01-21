#-*- coding:utf-8 -*-
import json
from collections import OrderedDict

with open('./Data/dungeons.json', encoding="utf-8") as data_file:    
    data = json.load(data_file, object_pairs_hook=OrderedDict)
    print(data[0]["awards"][0])
