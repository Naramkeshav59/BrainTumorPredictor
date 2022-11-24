import joblib
import numpy as np
import cv2
def preprocess(path):
    img = np.array(cv2.imread(path,cv2.IMREAD_GRAYSCALE)) #reading images into grayscale
    img = cv2.resize(img,(200,200))
    X_flattened = np.reshape(img,-1)
    X_flattened = X_flattened/255
    return X_flattened
x = preprocess('./yes/y0.jpg')
loaded_model = joblib.load(open('./BrainTumorPredictor/finalized_model.sav', 'rb'))
y = loaded_model.predict([x])
print(y)
dict = {'0':'Good News!! No,tumor is Detected.',
      '1':'Tumor is Detected. Take care, Hope for the Good'}

print(dict[str(y[0])])