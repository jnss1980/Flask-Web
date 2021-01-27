from flask import Flask, render_template, request ,jsonify
import json
import Util.dbUtil as odb

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

        
    if  info['user_title'] is None:
        return jsonify({"message":"text not found"})
    else:
        return jsonify(info)


@app.route('/getUserProfileList',methods=['GET','POST'])
def getList():
    m = odb.dbUtil()
    m._checkDB()
    reslut = m._selectUserProfile([])
    return jsonify(reslut)
    
@app.route('/addUser',methods=['GET','POST'])
def addUser():
    if request.data == b'':
        return jsonify({"message":"text not found"})
        
    print(request.data)
    
    data = json.loads(request.data)
    info = dict()
    info['user_ID'] = data.get("user_ID",None)
    info['user_title'] = data.get("user_title",None)
    info['user_name'] = data.get("user_name",None)
    info['user_pwd'] = data.get("user_pwd",None)
    info['user_phone'] = data.get("user_phone",None)   
    info['user_remote_addr'] = request.remote_addr
    
    m = odb.dbUtil()
    m._checkDB()
    m._insertUserProfile(info)
      

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
