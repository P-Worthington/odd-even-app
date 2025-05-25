import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def check_number():
    # Your odd/even logic here
    return "Hello from odd-even app!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

@app.route('/')
def check_number():
    num = request.args.get('number', type=int)
    if num is None:
        return "Please provide a number in the URL like ?number=4"
    if num % 2 == 0:
        return f"{num} is even."
    else:
        return f"{num} is odd."

if __name__ == '__main__':
    app.run(debug=True)