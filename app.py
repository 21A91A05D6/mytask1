from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get details
    name = "Asha Shiny Gudey"
    username = os.getenv('USER', 'unknown')
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput("top -b -n 1")

    # Format output
    return f"""
    <h1>{name}</h1>
    <p>Username: {username}</p>
    <p>Server Time (IST): {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
