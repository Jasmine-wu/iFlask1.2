


from flask import Flask,request,render_template,redirect
from flask import views

app=Flask(__name__)


# class IndexView(views.View):
#     methods = ['GET']
#     # decorators = [auth, ]
#     def dispatch_request(self):
#         print('Index')
#         return 'Index!'

def auth(func):
    def inner(*args, **kwargs):
        print('before')
        result = func(*args, **kwargs)
        print('after')
        return result

    return inner
class IndexView(views.MethodView):
    methods = ['GET']  # 指定运行的请求方法
    # 登录认证装饰器加在哪？
    decorators = [auth, ]  #加多个就是从上往下的效果
    def get(self):
        print('xxxxx')
        return "我是get请求"
    def post(self):
       return '我是post请求'

# 路由如何注册？
# IndexView.as_view('index'),必须传name
app.add_url_rule('/index',view_func=IndexView.as_view('index'))

if __name__ == '__main__':
    app.run()
