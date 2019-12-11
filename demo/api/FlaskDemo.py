from flask import Flask, request, json
import pymysql

app = Flask(__name__)

@app.route('/helloWorld')
def hello_world():
    conn = pymysql.connect(host='10.255.242.136', port=3306, user='kefu_ai_user', passwd='kefu_ai_dev', db='kefu_ai')
    # 创建游标
    cursor = conn.cursor()
    # 执行SQL，并返受影响行数
    effect_row = cursor.execute("SELECT * FROM question_classify_train order by id desc limit 10")
    print(effect_row)
    row_2 = cursor.fetchall()
    # 关闭游标
    cursor.close()
    conn.close()
    return str(row_2)


@app.route('/helloWorldJson', methods=['POST'])
def hello_world_json():
    if request.method == 'POST':
        data = request.get_data()
        print(data)
        json_data = json.loads(data.decode("utf-8"))
        print(json_data)
        return data


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=False)
