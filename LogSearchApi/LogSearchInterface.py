import pymysql
from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

class LogSearch(object):
    def __init__(self):
        self.db = pymysql.connect("localhost","wyn","123456","ebay_log", autocommit=True)

    def ParseRawData(self, rows):
        pass

    def SearchByCorrId(self, corrId):
        cursor = self.db.cursor()
        sql = "SELECT * FROM log_item where corr_id = {0}".format(corrId)
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        return results
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



