

from flask import Flask,request,jsonify,make_response,session


app=Flask(__name__)
app.debug=True
# 这是配置session的规则
# app.session_interface=类()
app.secret_key='asdfsadfeeee'
@app.route('/',methods=['GET','POST'])
def index():
    session['name']='lqz'
    return 'hello'


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    session.pop('name')
    return '删除了'
@app.route('/order', methods=['GET', 'POST'])
def order():
    print(session['name'])
    return 'order'
if __name__ == '__main__':
    print(app.config)
    app.run()
    # 请求来了，走谁
    app.__call__()