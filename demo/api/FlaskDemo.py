from flask import Flask, request, json

app = Flask(__name__)


@app.route('/helloWorld')
def hello_world():
    return 'Hello World!'


@app.route('/helloWorldJson', methods=['POST'])
def hello_world_json():
    if request.method == 'POST':
        data = request.get_data()
        print(data)
        json_data = json.loads(data.decode("utf-8"))
        print(json_data);
        return data;


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=False);
