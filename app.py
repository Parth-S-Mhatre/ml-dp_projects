from flask import Flask,render_template,request
from text_summarizer import summazier

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/summarize',methods=['GET','POST'])
def summarize():
    if request.method=='POST':
        rawtext=request.form['raw_text']
        summazier(rawtext)
        summary,original_text,original_length,summary_length=summazier(rawtext)
    return render_template('summary.html',summary=summary,original_text=original_text,original_length=original_length,summary_length=summary_length)





if __name__=="__main__":
    app.run(debug=True)