# coding : utf-8
#Author : Parallel
#Create On  
def readJSON(filename=""):
    import json
    if filename != "":
        lists = filename.split(".")
        if lists[len(lists) - 1].lower() == "json":
            with open(filename,mode='r',encoding="utf-8") as file:
                return json.loads(file.read())
