from flask import Flask,request,render_template
import requests
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    inp=request.form.get('inp')
    key=request.form.get('key')
    message=None
    if request.method == 'POST':
        url=f'https://gen.pollinations.ai/text/you-are-a-advanced-prompt-enhancer-dont-give-any-useless-output-except-the-refined-prompt-write-in-one-para-not-more-here-is-the-prompt-:-{inp}?model=mistral&key={key}'
        res=requests.get(url)
        message=res.text
    return render_template('index.html',message=message)
if __name__ =='__main__':
    app.run(debug=True)
