from flask import Flask, render_template, request, redirect, url_for

import service as service
import cmnUtils as cmnUtils

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('home.html')


# click convertBtn.
@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        input_kana = request.form['input_kana']
        converted_input_list = service.converted_kana_to_oshite(cmnUtils.converted_new_line(input_kana))

        input_kana = service.converted_new_line(request.form['input_kana'])
        ## TODO:改行がエラー判定される
        is_downloadable = service.can_downloadable(input_kana)
        converted_input_list = service.converted_kana_to_oshite(input_kana)

        # rendering for home.html.
        return render_template('home.html',
                               input_kana=input_kana,
                               converted_input_list=converted_input_list,
                               fileType=service.FILE_TYPE_PNG,
                               can_downloadable=is_downloadable
                               )
    else:  # error redirect.
        return redirect(url_for('home'))


# click homeBtn from header.
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        input_kana = service.converted_new_line(request.json['input_kana'])
        # input_kana = request.form['input_kana']
        download_file = service.download_image(input_kana)
        return download_file
    else:  # error redirect.
        return redirect(url_for('home'))


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
