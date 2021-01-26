import os  
import sqlite3

class dbUtil():

    _dbPath = "dbfolder" #存放db檔資料夾
    _dbFile =  None			

    def __init__(self):
        self._dbFile = 'tmp.db'
       
    def __checkDB(self):
        # 檢查 資料夾 dbfolder 不存在則建立
        if os.path.exists(self._dbPath) is False:            
            print(self._dbPath+"Not Exists")            
            os.makedirs(self._dbPath)
            print(self._dbPath+"mak is!")
        _dbFile = os.path.join(self._dbPath,self._dbFile)
        if os.path.exists(self._dbFile) is False:
            self._createDB()
            
    def _createDB(self):
        command = "CREATE TABLE UserProfile(\
            user_title Text NULL,\
            user_name Text NULL,\
            user_pwd Text NULL\
        )"
        self._Execute(self,_dbFile,command,[])
        
    # 執行SQL Lite指令
    def _Execute(self, dbFile, sqlcommand, sqlparamter):
        with sqlite3.connect(dbFile) as conn:
            cur = conn.cursor()
            cur.execute(sqlcommand, sqlparamter)
            conn.commit()
            # 把結果轉為List<tuple>
            data = []
            for row in cur:
                data.append(row)
            return data
            
            