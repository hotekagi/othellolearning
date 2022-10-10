from flask import Flask, render_template, request, redirect
from logic import Board

app = Flask(__name__)
data = Board()

@app.route('/', methods=['GET'])
def get():
    return render_template('index.html', turn=data.turn, board_data=data.stones)

@app.route('/post', methods=['POST'])
def post():
    if request.form.get('position0') != None and request.form.get('position1') != None:
        req0 = request.form.get('position0')
        req1 = request.form.get('position1')
        if data.is_empty(int(req0), int(req1)):
            data.put_stone(int(req0), int(req1))
            data.change_turn()
    return redirect("/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8880, debug=True)
