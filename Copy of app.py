import joblib
import numpy as np
from flask import Flask, render_template, request

# Initialize Flask
app = Flask(__name__)

# Loading the trained model
model = joblib.load('best_churn_model.pkl')

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the input values
        
        # 'state' represents the geographic state of the customer (e.g., 'California', 'Texas')
        # It should be selected from a predefined list or dropdown in the form.
        state = request.form['state']  # Example: 'California'
        
        # 'account_length' is the length of the customer's account in months
        # It should be a positive integer (e.g., 12, 24, 36).
        account_length = int(request.form['account_length'])  # Example: 24
        
        # 'area_code' is the area code of the customer’s phone number.
        # It should be an integer (e.g., 415, 510, 408).
        area_code = int(request.form['area_code'])  # Example: 415
        
        # 'international_plan' is whether the customer has an international calling plan.
        # This should be selected as 'Yes' or 'No'.
        # We will encode this as 1 for 'Yes' and 0 for 'No'.
        phone_number = request.form['phone_number']

        international_plan = request.form['international_plan']  # Example: 'Yes'
        
        # 'voice_mail_plan' is whether the customer has a voicemail plan.
        # This should be selected as 'Yes' or 'No'.
        # We will encode this as 1 for 'Yes' and 0 for 'No'.
        voice_mail_plan = request.form['voice_mail_plan']  # Example: 'Yes'
        
        # 'number_vmail_messages' is the number of voicemail messages the customer has.
        # This should be a non-negative integer (e.g., 5, 10, 0).
        number_vmail_messages = int(request.form['number_vmail_messages'])  # Example: 10
        
        # 'total_day_minutes' is the total number of minutes the customer spends on daytime calls.
        # This should be a floating-point number (e.g., 200.5, 150.0).
        total_day_minutes = float(request.form['total_day_minutes'])  # Example: 200.5
        
        # 'total_day_calls' is the total number of daytime calls made by the customer.
        # This should be an integer (e.g., 50, 30).
        total_day_calls = int(request.form['total_day_calls'])  # Example: 50
        
        # 'total_day_charge' is the total charge the customer has for daytime calls.
        # This should be a floating-point number (e.g., 20.5, 15.0).
        total_day_charge = float(request.form['total_day_charge'])  # Example: 20.5
        
        # 'total_eve_minutes' is the total number of minutes the customer spends on evening calls.
        # This should be a floating-point number (e.g., 150.5, 120.0).
        total_eve_minutes = float(request.form['total_eve_minutes'])  # Example: 150.5
        
        # 'total_eve_calls' is the total number of evening calls made by the customer.
        # This should be an integer (e.g., 40, 25).
        total_eve_calls = int(request.form['total_eve_calls'])  # Example: 40
        
        # 'total_eve_charge' is the total charge the customer has for evening calls.
        # This should be a floating-point number (e.g., 15.0, 12.5).
        total_eve_charge = float(request.form['total_eve_charge'])  # Example: 15.0
        
        # 'total_night_minutes' is the total number of minutes the customer spends on nighttime calls.
        # This should be a floating-point number (e.g., 100.5, 90.0).
        total_night_minutes = float(request.form['total_night_minutes'])  # Example: 100.5
        
        # 'total_night_calls' is the total number of nighttime calls made by the customer.
        # This should be an integer (e.g., 30, 20).
        total_night_calls = int(request.form['total_night_calls'])  # Example: 30
        
        # 'total_night_charge' is the total charge the customer has for nighttime calls.
        # This should be a floating-point number (e.g., 10.0, 8.5).
        total_night_charge = float(request.form['total_night_charge'])  # Example: 10.0
        
        # 'total_intl_minutes' is the total number of minutes the customer spends on international calls.
        # This should be a floating-point number (e.g., 20.5, 50.0).
        total_intl_minutes = float(request.form['total_intl_minutes'])  # Example: 20.5
        
        # 'total_intl_calls' is the total number of international calls made by the customer.
        # This should be an integer (e.g., 5, 10).
        total_intl_calls = int(request.form['total_intl_calls'])  # Example: 5
        
        # 'total_intl_charge' is the total charge the customer has for international calls.
        # This should be a floating-point number (e.g., 5.0, 8.0).
        total_intl_charge = float(request.form['total_intl_charge'])  # Example: 5.0
        
        # 'customer_service_calls' is the number of calls the customer has made to customer service.
        # This should be an integer (e.g., 2, 0).
        customer_service_calls = int(request.form['customer_service_calls'])  # Example: 2
        
        # Convert categorical features to numerical (if needed)
        # Example encoding for categorical features:
        international_plan = 1 if international_plan == 'Yes' else 0
        voice_mail_plan = 1 if voice_mail_plan == 'Yes' else 0

        state_dict = {'State1': 0, 'State2': 1, 'State3': 2} 
        state_encoded = state_dict.get(state, -1)  
        
        # Prepare the feature array
        input_data = np.array([[state_encoded, account_length, area_code,phone_number, international_plan, 
                                voice_mail_plan, number_vmail_messages, total_day_minutes, 
                                total_day_calls, total_day_charge, total_eve_minutes, total_eve_calls, 
                                total_eve_charge, total_night_minutes, total_night_calls, total_night_charge, 
                                total_intl_minutes, total_intl_calls, total_intl_charge, customer_service_calls]])

        #prediction from the model
        prediction = model.predict(input_data)

        if prediction == 1:
            result = "This customer is likely to churn."
        else:
            result = "This customer is likely to stay."
        
        return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
