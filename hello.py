from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
  return  render_template('hello.html', name = user)

@app.route('/score/<int:score>')
def score(score):
  return render_template('score.html', marks = score)

@app.route('/result')
def method_name():
  dict = {'phy':50, 'che':60, 'maths':70}
  return render_template('result.html', result = dict)

@app.route('/admin')
def hello_admin():
  return 'hello admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
  return 'hello  %s' % guest

@app.route('/user/<name>')
def hello_user(name):
  if name == 'admin':
    return redirect(url_for('hello_admin'))
  else:
    return redirect(url_for('hello_guest', guest=name))

if __name__ == '__main__':
  app.run(debug = True)