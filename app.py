from flask import Flask, render_template, request ,jsonify
import json

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    #print(request.data)
    if request.data == b'':
         return jsonify({"message":"text not found"})

    data = json.loads(request.data)
    info = dict()
    info['user_title'] = data.get("user_title",None)
    info['user_name'] = data.get("user_name",None)
    info['user_pwd'] = data.get("user_pwd",None)
    info['user_remote_addr'] = request.remote_addr
    
    print('')
    print('user_title='+data.get("user_title",None))
    print('user_name='+data.get("user_name",None))
    print('user_pwd='+data.get("user_pwd",None))
    print('request.remote_addr='+request.remote_addr)
    print('')
        
    if  info['user_title'] is None:
        return jsonify({"message":"text not found"})
    else:
        return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
