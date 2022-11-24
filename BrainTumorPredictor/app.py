from flask import Flask, render_template, request
import joblib
import numpy as np
import cv2

def preprocess(path):
    img = np.array(cv2.imread(path,cv2.IMREAD_GRAYSCALE)) #reading images into grayscale
    img = cv2.resize(img,(200,200))
    X_flattened = np.reshape(img,-1)
    X_flattened = X_flattened/255
    return X_flattened
app = Flask(__name__)

app = Flask(__name__,template_folder='templates')
@app.route("/")
def home():
    return render_template("main.html")
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['fileAjax']
      with open('./upload.jpg','wb') as img:
        f.save(img)
      X_pred = preprocess('upload.jpg')
      model = joblib.load(open('./finalized_model.sav', 'rb'))
      y_pred = model.predict([X_pred])
      dict = {'0':'Good News!! No tumor is Detected. Stay Healthy, Stay Happy.',
      '1':'Tumor is Detected. Take care, Hope for the Best.'}
      output = dict[str(y_pred[0])]
      return render_template('main.html',output = output)
		
if __name__ == "__main__":
  app.run(debug=True,host ='0.0.0.0',port =8000)