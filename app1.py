from flask import Flask, render_template, request
import pickle
import tensorflow as tf
from tensorflow import keras
from keras.models import model_from_json
#app = Flask('faku')
app = Flask(__name__)
# @app.route('/',methods=['GET','POST'])
# def home():
#   prediction = 0
#   if request.method == 'POST':
#     model = pickle.load(open("C:/Users/simra/Desktop/Group6/lstm.pkl",'rb'))
#     user_input = request.form['newstext']
#     prediction = model.predict(user_input)
#     print(prediction)
#   return render_template('predictorform.html',prediction=prediction)

# if __name__ == "__main__":
#      app.run(debug=True)

def get_model():
   
   from keras.models import model_from_json
   # load json and create model
   file = open("C:/Users/simra/Desktop/Group6/fake_json.json", 'r') 
   model_json = file.read()
   file.close()
   loaded_model = model_from_json(model_json)
   # load weights
   return loaded_model.load_weights("C:/Users/simra/Desktop/Group6/model.h5")

@app.route('/')
def show_predict_fake_form():
    return render_template('predictorform.html')
@app.route('/result', methods=['POST'])
def result():
    form = request.form
    if request.method == 'POST':
      #write your function that loads the model
      model = get_model()
      #model = pickle.load(open("C:/Users/simra/Desktop/Group6/lstm.pkl",'r')) #you can use pickle to load the trained model
      newstext = request.form['newstext']
      predicted_fakenews = model.predict(newstext)
      # if predicted_fakenews[0][0]<0.5:
      #     label = 'Real News'
      # else:
      #   label = 'Fake News'
      return render_template('resultsform.html', newstext=newstext, predicted_fakenews=predicted_fakenews)
    
if __name__ == "__main__":
   app.run(debug=True)