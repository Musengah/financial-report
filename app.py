from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask app!"

@app.route('/reports', methods=['GET', 'POST'])
def reports():
    pass

@app.route('/reports/<int:report_id>', methods=['GET', 'PUT', 'DELETE'])
def report_detail(report_id):
    pass

@app.route('/users', methods=['GET', 'POST'])
def users():
    pass

@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_detail(user_id):
    pass

@app.route('/login', methods=['POST'])
def login():
    pass

@app.route('/logout', methods=['POST'])
def logout():
    pass

if __name__ == '__main__':
    app.run(debug=True)
