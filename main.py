from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temperature = request.form.get('temperature')
    if temperature:
        try:
            temperature = float(temperature)
            prediction = model.predict([[temperature]])
            output = round(prediction[0], 2)
            return render_template('index.html', prediction_text=f'Predicted Value: {output}')
        except ValueError:
            return render_template('index.html', error_text='Invalid input. Please enter a numeric value.')
    else:
        return render_template('index.html', error_text='Please provide a temperature value.')

if __name__ == '__main__':
    app.run(debug=True)
