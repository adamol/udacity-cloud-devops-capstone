from flask import Flask
import cowsay

app = Flask(__name__)

@app.route("/")
def hello_world():
    output = cowsay.get_output_string('cow', 'Hello World')

    output = output.replace('\n', '<br>')

    return output

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
