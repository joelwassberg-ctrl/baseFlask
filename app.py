from flask import Flask, render_template
"""
Template inheritance can be used when multiple templates share a common structure 
such as headers, footers, and navigation menus.
"""
app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')