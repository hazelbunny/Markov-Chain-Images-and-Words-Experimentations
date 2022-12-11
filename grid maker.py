import json
file = open("dataset.json")

_output=[]
for x in range(1,500):
    _output_1 = []
    for y in range(1,500):
        _output_1.append([])
    _output.append(_output_1)

jsout=json.dumps(_output)

json.dump(jsout,file)
