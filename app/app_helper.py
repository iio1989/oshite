# This file is imported app.py
import datetime
import os
import re
import cv2

from flask import Markup, send_file

# oshite image names.
UNICODE_KANA = ["0x3042", "0x3044", "0x3046", "0x3048", "0x304a", "0x304b", "0x304d", "0x304f", "0x3051", "0x3053",
                "0x3055", "0x3057", "0x3059",
                "0x305b", "0x305d", "0x305f", "0x3061", "0x3064", "0x3066", "0x3068", "0x306a", "0x306b", "0x306c",
                "0x306d", "0x306e", "0x306f", "0x3072",
                "0x3075", "0x3078", "0x307b", "0x307e", "0x307f", "0x3080", "0x3081", "0x3082", "0x3089", "0x308a",
                "0x308b", "0x308c", "0x308d", "0x3084", "0x3086", "0x3088", "0x308f", "0x3092", "0x3093"]

# oshite image file extension.
FILE_TYPE_PNG = ".png"


# Convert Kana to List of OshiteImage.
def converted_kana_to_oshite(kana):
    kana_list = list(kana)
    converted_list = [Markup('<span class="oshite__not__convert__row">')]

    if len(kana) == 0:
        converted_list.append(Markup('&nbsp;&nbsp;') + "ひらがなが入力されていません。")

    url = "/static/images/oshiteFont/"
    after_br = False

    for kana in kana_list:
        if hex(ord(kana)) in UNICODE_KANA:
            converted_list.append(url + hex(ord(kana)) + FILE_TYPE_PNG)
        elif kana == "\r":
            after_br = True
            converted_list.append(Markup('</span>'))
            converted_list.append(Markup('<span class="oshite__not__convert__row">'))
        else:
            converted_list.append(Markup('<span class="oshite__not__convert">'))
            converted_list.append(Markup('<span class="oshite__not__convert__char__padding">'))
            converted_list.append(Markup('</span>'))
            converted_list.append(
                Markup('<span class="oshite__not__convert__char alert-secondary">&nbsp;&nbsp;') + two_bytes_char(
                    kana) + Markup('&nbsp;&nbsp;</span>'))
            converted_list.append(Markup('</span>'))
    if after_br:
        converted_list.append(Markup('</span>'))
    return converted_list


def download_image(kana_list):
    cwd = os.getcwd()
    converted_kana_list = []
    converted_kanas = []
    for kana in kana_list:
        if hex(ord(kana)) in UNICODE_KANA:
            img = cv2.imread(
                cwd + '/app/static/images/oshiteFont/' + hex(ord(kana)) + FILE_TYPE_PNG)
            converted_kanas.append(cv2.resize(img, dsize=(0, 0), fx=0.5, fy=0.5))
        elif kana == "\r":
            converted_kana_list.append(converted_kanas)
            converted_kanas = []
    if len(converted_kanas) != 0:
        converted_kana_list.append(converted_kanas)

    im_tile = concat_tile(converted_kana_list)

    dfile = cwd + '/temp/created_image/' + get_now_date_time() + '.png'

    cv2.imwrite(dfile, im_tile)

    filepath = dfile

    # filepath = os.getcwd() + "/temp/created_image/0x304a.png"
    filename = os.path.basename(filepath)
    # attachment_filename
    return send_file(filepath, as_attachment=True,
                     download_name=filename,
                     mimetype='image/png')


def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])


# 2019-02-04 21:04:15.412854##
def get_now_date_time():
    dt_now = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    return dt_now


def converted_new_line(words):
    return re.sub(r'\r\n|\r|\n', '\r', words)


def two_bytes_char(words):
    return words.translate(words.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))


def can_downloadable(kana):
    if kana == "":
        return False

    has_other_char = True
    kana_list = list(kana)

    for kana in kana_list:
        if not is_oshite_char(kana):
            has_other_char = False
            break

    return has_other_char


def is_oshite_char(char):
    return hex(ord(char)) in UNICODE_KANA or char == "\r"
