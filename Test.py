from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>My Website</title>
        </head>
        <body>
            <h1>Welcome to My First Python Website</h1>
            <p>Hello Manikandan!</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)