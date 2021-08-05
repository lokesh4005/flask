from flask import Flask, request, render_template
loki=Flask(__name__)


@loki.route('/')
def hello():
    return render_template("login.html")
database={'chandra': 'pubg', 'dhanush':'dp28', 'koushik':'ranker' }
@loki.route('/form_login',methods=['POST','GET'])
def login():
    name=request.form['username']
    pwd=request.form['password']
    if name not in database:
        return render_template('login.html', info='Invalid User')
    else:
        if database[name]!=pwd:
            return render_template('login.html', info='Invalid Password')
        else:
            return render_template('home.html', name=name)



if __name__=='__main__':
    loki.run(debug=True)