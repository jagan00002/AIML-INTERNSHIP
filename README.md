Customer Churn Prediction Web Application
Overview
This project is a Customer Churn Prediction web application developed as part of an AI/ML internship. It utilizes machine learning to predict whether a customer is likely to leave a service based on various factors such as account length, call duration, and international plan usage.

The web application is built using Flask for the backend and serves a web-based user interface for predictions.

Features
Machine Learning Model: Uses a pre-trained model (best_churn_model.pkl) to predict customer churn.
Web-Based Interface: Developed using Flask and HTML/CSS.
Form-Based Input: Users enter customer details such as call duration and area code.
Real-Time Prediction: The system predicts whether a customer will churn or stay.
User-Friendly UI: Clean and responsive design for easy data entry.
Technologies Used
Python
Flask (for web framework)
Joblib (for model loading)
NumPy (for data processing)
HTML/CSS (for frontend UI)
Bootstrap (for responsive design)
Installation & Setup
Prerequisites:
Install Python (3.7+)
Install required libraries:
bash
Copy
Edit
pip install flask joblib numpy
Ensure best_churn_model.pkl is available in the project directory.
Running the Application:
Clone the repository:
bash
Copy
Edit
git clone https://github.com/jagan00002/aiml-internship.gi
cd aiml-internship
Run the Flask app:
bash
Copy
Edit
python app.py
Access the web application in your browser at:
cpp
Copy
Edit
http://127.0.0.1:5000/
File Structure
lua
Copy
Edit
|-- app.py            # Flask Backend
|-- templates/
|   |-- index.html    # Frontend HTML Form
|-- static/
|   |-- style.css     # Styling (if applicable)
|-- best_churn_model.pkl  # Trained ML Model
|-- README.md         # Documentation
Usage
Open the web app in a browser.
Enter customer details in the form.
Click "Predict Churn" to get a result.
The application will predict whether the customer is likely to leave.
Future Enhancements
Deploy the app using Heroku or AWS.
Improve the UI with better CSS/JS.
Enhance the model with more training data.
Add API support for mobile applications.
Contributors
Jagannath, Dinesh, Shripad,  Pavankumar
License
This project is licensed under the MIT License.

