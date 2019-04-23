import os
import sso_embed as looker
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    iframe_url=looker.test()
    return render_template('home.html',iframe_url=iframe_url)
if __name__ == '__main__':
    app.run(debug=True)
