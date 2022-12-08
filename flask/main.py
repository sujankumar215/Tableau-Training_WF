from flask import Flask,redirect,url_for,render_template
### WSGI Application
app = Flask(__name__)

@app.route('/') ### Decoreator
def welcome():   ## Decorator come with a function
    return render_template('index.html')

@app.route('/success/<int:score>') ### String  <score>
def success(score):   ## Decorator come with a function
    return "The Person has passed and the marks is  "+str(score)

@app.route('/fail/<int:score>') ### String  <score>
def fail(score):   ## Decorator come with a function
    return "The Person has failed and the marks is  "+str(score)


@app.route('/results/<int:marks>') ### String  <score>
def results(marks):   ## Decorator come with a function
    results=""
    if marks<50:
        results = 'fail'
    else:
        results = 'success'
    ###return "The Person has "+ results +" and the marks is  "+str(score)
    return redirect(url_for(results,score=marks))

if __name__=='__main__':
    app.run(debug=True)