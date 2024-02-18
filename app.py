from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/login')
def login():
    return render_template('login_register.html')

@app.route('/contactus')
def contactus():
    return render_template('contact_us.html')

if __name__=='__main__':
    app.run(debug=True)