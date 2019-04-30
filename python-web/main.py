from flask import Flask, render_template, request, redirect


app = Flask(__name__)

messages = [{'email': 'xero@local.domain', 'message': 'The quick brown fox'}]

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contat_page():
    return render_template('contact.html')

@app.route('/message')
def message():
    email = request.args.get('email')
    message = request.args.get('message')
    messages.append({'email': email, 'message': message})
    return render_template('message_processed.html')

@app.route('/messages')
def message_list():
    return render_template('message_list.html', messages=messages)

app.run(debug=True, host='0.0.0.0')