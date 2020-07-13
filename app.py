from flask import Flask,render_template,redirect,request
import joblib


app=Flask(__name__)



model=joblib.load("harword_pays_model.pkl")

@app.route('/')#routing i.e when a client will enter this url the below function will performed
def hello():
	return render_template("index.html")  #write html code in this index.html file saved in templates folder
   


@app.route('/', methods=['POST'])
def marks():
	if request.method=='POST':
		hours=float(request.form['work'])
		marks=str(model.predict([[hours]])[0][0])
		marks=float(marks)
		marks=round(marks,2)
		marks=str(marks)
	return render_template('index.html',your_marks=marks)



if __name__=='__main__':
	app.run(debug=True)
