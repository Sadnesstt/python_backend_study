from flask import Flask, jsonify, request, render_template
app = Flask(__name__, static_url_path='/static')
session_count = 0


@app.route('/login')
def login():
    email_address = request.args.get('email_address')
    passwd = request.args.get('passwd')
    print(email_address, passwd)

    if email_address == "dave@gmail.com" and passwd == "111":
        return_data = {'auth':'success'}
    else:
        return_data = {'auth':'failed'}
    return jsonify(return_data)


@app.route('/html_test')
def hello_html():
    # html file은 templates 폴더에 위치해야 함
    return render_template('login_rawtest.html')
