from flask import Flask
app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
   return 'hello %s! ' %name

if __name__ == '__main__':
  app.run()