from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Make sure to use a strong secret key

# Sample user data (you can store this in a database in real apps)
users = {
    'jashanpreetkaur': {'name': 'Jashanpreet Kaur', 'email': 'jashanpreetkaurkhass@gmail.com', 'phone': '9872839927', 'location': 'Fatehgarh Sahib, Punjab'}
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username in users:
            session['username'] = username
            return redirect(url_for('profile'))
        else:
            return "Invalid username. Please try again."
    return render_template('login.html')

@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user_data = users[session['username']]
    return render_template('profile.html', user=user_data)

if __name__ == '__main__':
    app.run(debug=True)
