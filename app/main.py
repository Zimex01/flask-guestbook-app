from flask import Flask, request, render_template, redirect, url_for
import re

app = Flask(_name_)

# In-memory storage for guestbook entries
guestbook = []

# Basic input sanitization
def sanitize_input(text):
    if not text:
        return ""
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    return text[:50]  

@app.route('/')
def index():
    return render_template('index.html', entries=guestbook)

@app.route('/add', methods=['POST'])
def add_entry():
    name = sanitize_input(request.form.get('name'))
    message = sanitize_input(request.form.get('message'))
    if name and message:
        guestbook.append({'name': name, 'message': message})
    return redirect(url_for('index'))

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)