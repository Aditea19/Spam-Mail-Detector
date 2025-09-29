from flask import Flask, request, render_template
import joblib

# Load the trained pipeline
model = joblib.load('spam_pipeline.joblib')

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # get message from the form
    message = request.form['message']
    # use the model to predict
    prediction = model.predict([message])[0]

    if prediction == 1:
        result = "✅ This looks like a Ham (Safe) Email"
    else:
        result = "🚨 This looks like a Spam Email!"

    return render_template('index.html', prediction_text=result, user_input=message)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  # Render provides the port
    app.run(host="0.0.0.0", port=port, debug=True)
