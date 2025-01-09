from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)


with open(r'C:/Users/siddh/OneDrive/Desktop/Git/AI-ML/Task 3/heart_attack_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        data = request.form
        
        # Get user input from the form
        age = int(data.get("age"))
        cardiac_arrest = 1 if data.get("cardiac_arrest") == 'Yes' else 0  
        sex = 1 if data.get("sex") == 'Male' else 0
        cholesterol = int(data.get("cholesterol"))
        smoker = 1 if data.get("smoker") == 'Smoker' else 0
        hypertension = 1 if data.get("hypertension") == 'Yes' else 0
        alcoholic = 1 if data.get("alcoholic") == 'Yes' else 0
        
        
        # Only pass the 6 features that your model expects
        user_input = np.array([[age, sex, cholesterol, smoker, hypertension, alcoholic]])
        
        # Make the prediction
        model_output = model.predict(user_input)
        
        # Check (whether it's heart attack risk or not)
        if model_output[0] == 1:
            prediction = "Risk of Heart Attack"
        else:
            prediction = "No Risk of Heart Attack"
        
        return render_template('index.html', prediction_text=prediction)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
