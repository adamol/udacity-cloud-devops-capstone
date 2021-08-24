from flask import Flask
from flask import Response
import cowsay

app = Flask(__name__)

@app.route("/")
def hello_world():
    response = Response(cowsay.get_output_string('cow', 'Hello World'))

    # print(1 / 0)

    response.headers['Content-Type'] = 'text/plain'

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
