from flask import Flask, request
import subprocess

app = Flask(__name__)

command_list = [
    {
        "cmd_type": "System info",
        "cmd": ["uname", "-a"]
    },
    {
        "cmd_type": "DF",
        "cmd": ["df"]
    },
    {
        "cmd_type": "Git version",
        "cmd": ["git", "-v"]
    },
    {
        "cmd_type": "Docker version",
        "cmd": ["docker", "-v"]
    },
    {
        "cmd_type": "Which python",
        "cmd": ["which", "python"]
    },
    {
        "cmd_type": "Git version",
        "cmd": ["which", "python3"]
    }
]

system_list = [
    {
        "cmd_type": "System info",
        "cmd": ["uname", "-a"]
    },
    {
        "cmd_type": "Current user",
        "cmd": ["whoami"]
    },
    {
        "cmd_type": "Current shell",
        "cmd": ["echo", '$SHELL']
    },
    {
        "cmd_type": "Current user",
        "cmd": ["whoami"]
    },
    {
        "cmd_type": "Current user",
        "cmd": ["whoami"]
    },
]

@app.route('/check_versions', methods=['GET'])
def check_versions():
    cmd_array = command_list

    for index, item in enumerate(command_list):
        output = subprocess.check_output(command_list[index]["cmd"])
        # print(cmd_array[item])
        cmd_array[index]["output"] = str(output)

    return cmd_array


@app.route('/system_info', methods=['GET'])
def system_info():
    cmd_array = system_list

    for index, item in enumerate(system_list):
        output = subprocess.check_output(system_list[index]["cmd"])
        # print(cmd_array[item])
        cmd_array[index]["output"] = str(output)

    return cmd_array

@app.route('/run_command', methods=['GET'])
def run_command():
    # output = "123"
    # output = subprocess.check_output(["pwd"], capture_output=True)
    output = subprocess.check_output(["pwd"])
    # command = request.form['command']
    # output = subprocess.check_output(command, shell=True, text=True)
    # print(output)
    return output

if __name__ == '__main__':
    app.run(debug=True)