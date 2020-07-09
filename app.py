from flask import Flask, render_template,request



app = Flask(__name__)

@app.route('/')
def default():
    return render_template('home.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/stack.html')
def stack():
    return render_template('team.html')

@app.route('/test.html',methods=['POST'])
def push():


    if request.method == 'POST':
        data = request.form['']

      
    
 
       rev , conf =(s.sentiment(data))
        p_conf = conf * 100
               
        
    return render_template('test.html', prediction_text = "the review :: " + data + " :: is a " + rev + " review!, with " + str(p_conf) + " percent confidence")

 

if __name__ == '__main__':
    app.run(debug=True)


    