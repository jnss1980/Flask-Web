from flask import Flask
from flask_script import Manager
from Util.dbUtil import dbUtil

app = Flask(__name__)

manager = Manager(app)

def hello():
    dbUtil.__checkDB()

if __name__ == '__main__':
    manager.run()