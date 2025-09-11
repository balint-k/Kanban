from flask import Flask, render_template, request, redirect, url_for
from models import Database

app = Flask(__name__)
db = Database()

@app.route('/')
def board():
    columns = db.get_data()
    return render_template('board.html', columns=columns)

@app.route('/add_column', methods=['POST'])
def add_column():
    name = request.form['name']
    db.add_column(name)
    return redirect(url_for('board'))

@app.route('/delete_column', methods=['POST'])
def delete_column():
    column_id = request.form['column_id']
    db.delete_column(column_id)
    return redirect(url_for('board'))

if __name__ == '__main__':
    app.run(debug=True)
