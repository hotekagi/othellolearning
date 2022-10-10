from flask import Flask, render_template
from logic import Board

app = Flask(__name__)

@app.route('/')
def index():
    data = Board()
    return render_template('index.html', board_data=data.stones)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8880, debug=True)
