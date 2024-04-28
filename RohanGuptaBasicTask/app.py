# Importing Necessary Modules
from flask import Flask, render_template, request
import hashlib
app = Flask(__name__)

# Create a Main route here
@app.route('/')
def input():
    return render_template('Temp.html')

# Create other routes here. 
# host/passing will be the website link
# Mock database (replace with actual database interaction)
users = {}  # Change this to a real database connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/passing', methods=['GET', 'POST'])
def display():
    if request.method == 'POST':
        result = request.form
        if result['username'] in users:
            return render_template("result_data.html", result=result)

        # Save user data (replace with secure storage)
        # Hash password (implement a secure hashing algorithm)
        hashed_password = hash_password(result['password'])
        users[result['username']] = {
            'email': result['email'],
            'password': hashed_password
        }
    return render_template("result_data.html", result=result)


# main route to start with
if __name__ == '__main__':
    app.run(debug=True)