from flask import Flask, render_template, request, redirect, url_for
from distutils.util import strtobool
import ptvsd

import service as service
import cmnUtils as cmnUtils
import imgUtils as imgUtils

app = Flask(__name__)


@app.route('/')
def root():
    return redirect(url_for('home'))


# click convertBtn.
@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        input_kana = cmnUtils.convert_new_line(request.form['input_kana'])
        input_rube = cmnUtils.convertBool(request.form['input_rube'])
        is_downloadable = imgUtils.can_downloadable(input_kana)
        converted_input_list = service.converted_kana_to_oshite(input_kana, input_rube)

        # rendering for home.html.
        return render_template('home.html',
                               input_kana=input_kana,
                               input_rube=input_rube,
                               converted_input_list=converted_input_list,
                               fileType=imgUtils.FILE_TYPE_PNG,
                               can_downloadable=is_downloadable
                               )
    else:  # error redirect.
        return redirect(url_for('home'))


# click homeBtn from header.
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html',
                            input_rube=True)


@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        input_kana = cmnUtils.convert_new_line(request.json['input_kana'])
        input_rube = cmnUtils.convertBool(request.json['input_rube'])
        return service.download_image(input_kana, input_rube)
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
    ptvsd.enable_attach(address=('0.0.0.0', 5679))
    app.run(debug=False, host='0.0.0.0', port=8000)
