from flask import Flask, render_template, request, jsonify
from models import Database

app = Flask(__name__)
db = Database()

@app.route('/')
def board():
    columns = db.get_columns()
    return render_template('board.html', columns=columns)


if __name__ == '__main__':
    app.run(debug=True)
