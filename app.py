from flask import *  
import numpy as np
import pickle
app = Flask(__name__)  
model = pickle.load(open('classify.pkl', 'rb'))
model_reg = pickle.load(open('regression.pkl', 'rb'))
@app.route('/')  
def home ():  
    return render_template("home.html")  
 
@app.route('/classify')  
def classify():  
    return render_template("classify.html");  
 
@app.route('/validate', methods = ["POST"])  
def validate():  
    float_features = [int(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features) 

    if prediction == 1:
        pred = "You have like pizza."
    elif prediction == 0:
        pred = "You don't like pizza."
    output = pred

    return render_template('classify.html', prediction_text='{}'.format(output))

@app.route('/reg')  
def reg():  
    return render_template("reg.html");  
 
@app.route('/validates', methods = ["POST"])  
def validates():  
    int_features =[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    print(final_features)
    prediction=model_reg.predict(final_features)
    output=np.round(prediction[0],2)
    
    
    return render_template('reg.html', prediction_text='Fuel Rate is Rs {}'.format(output))  
if __name__ =="__main__":
    app.run(threaded=True, port=5000) 