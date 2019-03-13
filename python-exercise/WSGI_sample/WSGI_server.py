

#导入wsgire模块
from wsgiref.simple_server import make_server
# 从hello.py导入application函数
from hello import application

httpd = make_server("",8000,application)
print("Serving HTTP on port 8000...")
# 开始监听http请求
httpd.serve_forever()
