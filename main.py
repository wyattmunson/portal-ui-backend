from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/run_command', methods=['POST'])
def run_command():
    command = request.form['command']
    output = subprocess.check_output(command, shell=True, text=True)
    return output

if __name__ == '__main__':
    app.run(debug=True)