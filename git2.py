import json
array = json.dumps({"name":"Galen","learning objective":"load json files for data analysis"})
a = json.loads(array)
a["name"]
