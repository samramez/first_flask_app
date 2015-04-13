from flask import Flask

# Making instance of the class
app = Flask(__name__)

# If a path from the browser with /hello get executed, this function would  run
@app.route('/')
@app.route('/hello')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':

    # True means we don't have to restart the server every time I modify the code
    app.debug = True

    # Running a local server on our system
    # 0.0.0.0 means all public ip addresses can access my server
    app.run(host='0.0.0.0', port = 5000)