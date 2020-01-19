from flask import render_template, redirect, url_for, session
from app import app

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def index():
	return render_template('index.html')

if __name__ == "__main__":
	pass