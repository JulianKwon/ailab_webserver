import os
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def display():
    return redirect("https://sites.google.com/view/ailab-hyu/home", code=302)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port, threaded=True)
