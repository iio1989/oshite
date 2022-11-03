from flask import Flask, render_template, request, redirect, url_for, Markup
import app_helper as apHelp

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('home.html')

# click convetBtn. get HttpParam.
@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        input_kana = request.form['input_kana']
        converted_input_list = apHelp.getConvetedStr_kanaToOshite(input_kana)
        # rendering for home.html.
        return render_template('home.html',
                               input_kana=input_kana,
                               converted_input_list=converted_input_list,
                               fileType= apHelp.FILE_TYPE)
    else: # error redirect.
        return redirect(url_for('home'))

# click homeBtn from header.
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

# click aboutBtn from header.
@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

# click historyBtn from header.
@app.route('/history', methods=['GET', 'POST'])
def history():
    return render_template('history.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)