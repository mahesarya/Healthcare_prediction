from flask import Flask,request,render_template
import model

app=Flask(__name__)

@app.route('/') 
def home():

    return render_template('index.html')

@app.route('/predict' ,methods=['GET','POST'])
def predict():
    input_features=[x for x in request.form.values()]
    gender=input_features[0]
    age=int(input_features[1])
    hypertension=int(input_features[2])
    disease=int(input_features[3])
    married=input_features[4]
    work=str(input_features[5])
    area=input_features[6]
    glucose=float(input_features[7])
    bmi=float(input_features[8])
    smoke=input_features[9]
    # l=[gender,age,hypertension,disease,married,work,area,glucose,bmi,smoke]

    predicted_value=model.prediction(gender,age,hypertension,disease,married,work,area,glucose,bmi,smoke)

    if predicted_value==0:
        predicted_value="Good News! Patient has no Stroke"
    elif predicted_value==1:
        predicted_value="Oops! Patient going with Stroke"



    return render_template('index.html',predicted_text=predicted_value)
if __name__=='__main__':
    app.run(debug=True)