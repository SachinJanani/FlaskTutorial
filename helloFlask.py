from flask import Flask
app = Flask(__name__)

# Default root for web service
@app.route("/")
def greet():
  return "Hello Flask"
if __name__ == '__main__':
  app.run()
