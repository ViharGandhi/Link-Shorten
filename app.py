import hashlib
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

url_mappings = {}

def generate_short_url(long_url):
    hash_object = hashlib.md5(long_url.encode())
    return hash_object.hexdigest()[:6]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['long_url']
    short_url = generate_short_url(long_url)
    url_mappings[short_url] = long_url
    return render_template('shortened.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    if short_url in url_mappings:
        return redirect(url_mappings[short_url])
    else:
        return "URL not found."

if __name__ == '__main__':
    app.run(debug=True)
