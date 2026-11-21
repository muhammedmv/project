from flask import Flask,request,render_template
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client.test  
collection =db['data']

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')



@app.route('/submit',methods= ['POST'])
def submit():
  form_data = dict(request.form)
  print(form_data)
  collection.insert_one(form_data)
  return 'data tranfer successfull'

if __name__ == '__main__':
  app.run(debug=True)