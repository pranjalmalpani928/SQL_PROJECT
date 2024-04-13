from flask import Flask, request, jsonify
import mysql.connector as cnn

app = Flask(__name__)

@app.route('/data',methods=['GET','POST'])
def test():
    try:
        if (request.method=='POST'):
            mydb=cnn.connect(host='localhost',user='root',passwd='2173@Pramal')
            cursor=mydb.cursor()
            cursor.execute('use testdb')
            cursor.execute('select * from testdb.test_table')
            rows=cursor.fetchall()
            result = []
            for row in rows:
                result.append(dict(zip(cursor.column_names, row)))

            return jsonify(result)
        else:
            return 'please make a post request'
    except Exception as e:
        return e
    
if __name__=='__main__':
    app.run(debug=True)