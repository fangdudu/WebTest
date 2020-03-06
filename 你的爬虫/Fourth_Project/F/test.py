import json

jsondata = '''
{
"MemberList":[
{
"UserName":"小帅b",
"sex":"男"
},
{
"UserName":"小帅b的1号女朋友",
"sex":"女"
},
{
"UserName":"小帅b的2号女朋友",
"sex":"女"
}
]
}
'''

myfriend = json.loads(jsondata)  # json 数据转换PYTHON字典
print(myfriend.get('MemberList'))
