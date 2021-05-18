
from flask import  Flask,session,make_response
import redis
from flask_session import RedisSessionInterface,FileSystemSessionInterface

app =Flask(__name__ ,static_url_path='/static' ,static_folder='static' ,template_folder='templates')

# 第一种用法
# conn=redis.Redis(host='127.0.0.1',port=6379)
# app.session_interface=RedisSessionInterface(conn,'lqz',permanent=False)
# 第二种用法
# from redis import Redis
# from flask.ext.session import Session
# app.config['SESSION_TYPE'] = 'redis'
#
# app.config['SESSION_KEY_PREFIX'] = 'lqz'
#
# app.config['SESSION_REDIS'] = Redis(host='127.0.0.1',port='6379')
# # 本质跟上面一样
# # 类似的用法在flask中很常见 函数(app)
# Session(app)




@app.route('/')
def index():
    # session对象是RedisSession
    # session['name']='xxxxxx'
    res=make_response('hello')
    res.set_cookie('name','lqz',max_age=100)
    return res

@app.route('/order')
def order():

    return 'order'

if __name__ == '__main__':
    app.run()