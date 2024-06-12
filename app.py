from flask import Flask, request, jsonify, render_template
from robot import assistant

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/commande', methods=['POST'])
def commande():
    command = request.form['command']
    response = assistant(command)
    return jsonify({'response': response})

@app.route('/robot')
def nouvelle_page():
    return render_template('robot.html')

if __name__ == '__main__':
    app.run(debug=True)
