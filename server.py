from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return "Hello, World! This is a lightweight web server."

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5053)
    
