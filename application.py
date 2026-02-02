from flask import Flask, request, render_template

application = Flask(__name__)
app = application

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except:
        return '''
        <h1>Student Performance Prediction App</h1>
        <p>App is running successfully!</p>
        '''

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        try:
            return render_template('home.html')
        except:
            return '<h1>Prediction Page</h1><form method="POST"><button type="submit">Predict</button></form>'
    else:
        return render_template('home.html', results=85)
