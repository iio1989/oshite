from flask import Flask, render_template, request, redirect, url_for
import app_helper as ap_help

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('home.html')


# click convetBtn. get HttpParam.
@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        input_kana = request.form['input_kana']
        converted_input_list = ap_help.getConvetedStr_kanaToOshite(input_kana)
        # rendering for home.html.
        return render_template('home.html',
                               input_kana=input_kana,
                               converted_input_list=converted_input_list,
                               fileType=ap_help.FILE_TYPE)
    else:  # error redirect.
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

# old design -------------------------------------------------------------------

# click convetBtn. get HttpParam.
@app.route('/old_design/post', methods=['GET', 'POST'])
def old_design_post():
    if request.method == 'POST':
        input_kana = request.form['input_kana']
        converted_input_list = ap_help.getConvetedStr_kanaToOshite(input_kana)
        # rendering for home.html.
        return render_template('old_design/home.html',
                               input_kana=input_kana,
                               converted_input_list=converted_input_list,
                               fileType=ap_help.FILE_TYPE)
    else:  # error redirect.
        return redirect(url_for('old_design/home'))


# click homeBtn from header.
@app.route('/old_design/home', methods=['GET', 'POST'])
def old_design_home():
    return render_template('old_design/home.html')


# click aboutBtn from header.
@app.route('/old_design/about', methods=['GET', 'POST'])
def old_design_about():
    return render_template('old_design/about.html')


# click historyBtn from header.
@app.route('/old_design/history', methods=['GET', 'POST'])
def old_design_history():
    return render_template('old_design/history.html')


# old design -------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
