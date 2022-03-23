import redis
r=redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('name', 'runoob')  # 设置 name 对应的值
print(r['gospeltimes'])
print(r.get('gospeltimes'))  # 取出键 name 对应的值
print(type(r.get('name')))