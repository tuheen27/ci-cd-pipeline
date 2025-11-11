from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask app running via Jenkins CI/CD!"
@app.route('/status')
def status():
    return "Application is running smoothly!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
