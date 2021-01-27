import os  
import sqlite3
from datetime import datetime

class dbUtil():

    _dbPath = "dbfolder" #存放db檔資料夾
    _dbFile =  "tmp.db"			

    def __init__(self):
         self._dbFile = os.path.join(self._dbPath,self._dbFile)
       
    def _checkDB(self):
        # 檢查 資料夾 dbfolder 不存在則建立
        if os.path.exists(self._dbPath) is False:          
            os.makedirs(self._dbPath)
            
        if os.path.exists(self._dbFile) is False:
            self._createDB()
            
    def _createDB(self):
        command = "CREATE TABLE UserProfile(\
            user_ID Text Not NULL,\
            user_title Text NULL,\
            user_name Text NULL,\
            user_pwd Text NULL,\
            user_phone TEXT NULL,\
            RecordTime Text NOT Null,\
            PRIMARY KEY (user_ID, RecordTime)\
        )"
        self._Execute(self._dbFile,command,[])   

    def _insertUserProfile(self,para):
        user_id = para['user_ID']
        user_title = para['user_title']
        user_name = para['user_name']
        user_pwd = para['user_pwd']
        user_phone = para['user_phone']
        now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        
        command = " INSERT INTO UserProfile VALUES(:user_ID,:user_title,:user_name,:user_pwd,:user_phone,:RecordTime)"
        parameter = {
            'user_ID': user_id,
            'user_title': user_title,
            'user_name': user_name,
            'user_pwd': user_pwd,
            'user_phone': user_phone,
            'RecordTime': now
        }
        self._Execute(self._dbFile,command,parameter)
    
    def _deleteUserProfile(self,para):
        result = {
            'status': False,
            'message':'',
            'data':[]
        }   
        self._checkDB()
        sqlPara = {}
        command = " Delete UserProfile "
        
        if 'user_ID' not in para:
            return False, "參數錯誤，未輸入參數id"
            
        if para['user_ID'] is None:
             return False, "參數錯誤，參數id無值"
             
        if para['user_ID'] is not None:
          command += " Where user_ID=:user_ID "
          sqlPara['user_ID']=para['user_ID']  
        
          
        data = self._Execute(self._dbFile, command, sqlPara)
        result['status'] = True
        result['message'] = '刪除成功'
        result['data'] = data
        return result        
    
    def _selectUserProfile(self,para):
        result = {
            'status': False,
            'message':'',
            'data':[]
        }   
            
        self._checkDB()
            
        # select 指令
        sqlPara = {}
        command = " Select * From UserProfile  Where 1=1"
        
        #加入查詢條件
        if 'user_ID' in para:
            if para['user_ID'] is not None:
                command += " And user_ID=:user_ID "
                sqlPara['user_ID']=para['user_ID']        
                
        if 'user_title' in para:
            if para['user_title'] is not None:
                command += " And user_title=:user_title "
                sqlPara['user_title']=para['user_title']
                
        if 'user_name' in para:
            if para['user_name'] is not None:
                command += " And user_name=:user_name "
                sqlPara['user_name']=para['user_name']

        if 'user_pwd' in para:        
            if para['user_pwd'] is not None:
                command += " And user_pwd=:user_pwd "
                sqlPara['user_pwd']=para['user_pwd']

        if 'user_phone' in para:                 
            if para['user_phone'] is not None:
                command += " And user_phone=:user_phone "
                sqlPara['user_phone']=para['user_phone']        
        
        data = self._Execute(self._dbFile, command, sqlPara)
        result['status'] = True
        result['data'] = data
        return result        
        
    # 執行SQL Lite指令
    def _Execute(self, dbFile, sqlcommand, sqlparamter):
        print(sqlcommand)
        with sqlite3.connect(dbFile) as conn:
            cur = conn.cursor()
            cur.execute(sqlcommand, sqlparamter)
            conn.commit()
            # 把結果轉為List<tuple>
            data = []
            for row in cur:
                data.append(row)
            return data