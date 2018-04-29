from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def greetings():
    return 'Greetings, LinuxFest'
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')