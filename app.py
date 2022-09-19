from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('theOffice.html')

@app.route('/bootstrap')
def bootstrap():
    return render_template('Sienfeld.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)