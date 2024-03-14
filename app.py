from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        test_string = request.form['test_string']
        regex = request.form['regex']
        matches = re.findall(regex, test_string)
        return render_template('results.html', matches=matches)
    return render_template('index.html')

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        return 'The email address is valid.'
    else:
        return 'The email address is invalid.'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

