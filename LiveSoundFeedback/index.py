from flask import Flask, request, send_from_directory

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

app.route('/static/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

app.route('/static/js/lib/<path:path>')
def send_js(path):
    return send_from_directory('static/js/lib', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000)

