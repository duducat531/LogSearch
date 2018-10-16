from flask import Flask
from flask import request
from flask import jsonify

from DBInstance.DBInstance import DBInstance

app = Flask(__name__)

class LogSearch(object):
    def __init__(self):
        self.dbIns = DBInstance()

    def ParseRawData(self, rows):
        # TODO
        return rows

    def SearchByCorrId(self, corrId):
        sql = "SELECT * FROM log_item where corr_id = {0} order by timestamp".format(corrId)
        results = self.dbIns.Execute(sql)
        return self.ParseRawData(results)
        # for row in results:
        #     print(row)

@app.route('/SearchByCorrId')
def SearchByCorrId():
    corr_id = request.args.get('corr_id', default='1', type=str)
    return jsonify(logSearch.SearchByCorrId(corr_id))

@app.route('/')
def Hello():
    return 'Hello'

if __name__ == '__main__':
    logSearch = LogSearch()
    app.run()



