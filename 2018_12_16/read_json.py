import json

# with open("./111.json", 'r', encoding='UTF-8') as f:

with open('./wanzheng.json', 'r', encoding='UTF-8') as f:
    temp = json.loads(f.read())
    #print(temp)
    #print(temp['RECORDS'])
    print(len(temp['RECORDS']))
    print(temp['RECORDS'][1]['Id'])

print('hello world!')


