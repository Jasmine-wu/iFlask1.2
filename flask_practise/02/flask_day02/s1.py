

from flask import Flask,session,render_template,Markup


app=Flask(__name__)
app.debug=True
app.secret_key='asdfsdfe34454dfdf'
app.config['SESSION_COOKIE_NAME']='xxxxxx'



def test():

    return Markup('<input type="text">')
#J9.X0YGQg.Uc9RkCClahhpqXkU7qITS0hrdT8
@app.route('/',methods=['GET'])
def index():
    session['key']='asdfasdf'
    session['user']='lqz'
    return 'hello'

@app.route('/order',methods=['GET'])
def order():
    print(session['key'])
    return 'order'
@app.route('/xxx',methods=['GET'])
def xxx():
    return render_template('index.html',aa='lqz',bb=18,cc=test,ll=[1,2,3],name='egon',sss='<input type="text">')

if __name__ == '__main__':
    print(app.config)
    app.run()