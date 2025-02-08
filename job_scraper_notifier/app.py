from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

PREFERENCES_FILE = "preferences.json"

# Load user preferences from a file
def load_preferences():
    if os.path.exists(PREFERENCES_FILE):
        with open(PREFERENCES_FILE, "r") as file:
            return json.load(file)
    return None

# Save user preferences to a file
def save_preferences(preferences):
    with open(PREFERENCES_FILE, "w") as file:
        json.dump(preferences, file, indent=4)

@app.route('/', methods=['GET', 'POST'])
def index():
    preferences = load_preferences()
    
    if preferences:
        return "Preferences already submitted. You will receive daily job updates."
    
    if request.method == 'POST':
        preferences = {
            "email": request.form.get("email"),
            "job_title": request.form.get("job_title"),
            "location": request.form.get("location"),
            "company": request.form.get("company")
        }
        save_preferences(preferences)
        return "Preferences saved successfully! You will receive daily job updates."
    
    return render_template('preferences.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
