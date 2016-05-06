from flask import Flask, render_template, request, redirect
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

api = Api(app)
class Vizq1(Resource):
  def get(self):
    return "hello world"

api.add_resource(Vizq1,'/vizq1')


if __name__ == '__main__':
  app.run(port=33507)
