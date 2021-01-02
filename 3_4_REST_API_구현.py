from flask import Flask, jsonify
app = Flask(__name__)

# routing 해주기
@app.route('/json_test')
def hello_json():
    data = {'name':'우대리', 'family':'Woo'} # 사전 데이터 정의
    return jsonify(data) # return할때 jsonify 호출하기

@app.route('/server_info')
def server_json():
    data = {'server_name':'127.0.0.1', 'server_port':'8080'}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port = '8080')
