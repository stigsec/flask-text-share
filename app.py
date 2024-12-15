from flask import Flask, render_template, request, send_from_directory
import random
import string
import os
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

path = 'files'
for filename in os.listdir(path):
    file = os.path.join(path, filename)
    
    try:
        if os.path.isfile(file) or os.path.islink(file):
            os.unlink(file)
    except Exception:
        print("Failed to delete the files on startup")

app = Flask(__name__)

scheduler = BackgroundScheduler()

def generate_random_name():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    text = request.form['text']
    upload_dir = "files"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    random_name = generate_random_name()
    filename = random_name + ".txt"
    path = os.path.join(upload_dir, filename)
    with open(path, 'w') as file:
        lines = (line.strip() for line in text.splitlines())
        file.write('\n'.join(lines))                              #Change deletion time here
    scheduler.add_job(delete_file, 'date', run_date=datetime.now() + timedelta(minutes=10), args=[path])
    file_url = f"/view/{filename}"
    return render_template('upload_done.html', file_url=file_url)

@app.route('/view/<path:file_to_view>')
def view(file_to_view):
    upload_dir = "files"
    return send_from_directory(upload_dir, file_to_view)

if __name__ == '__main__':
    scheduler.start()
    app.run(port=5003)
