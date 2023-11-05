# This file is imported app.py
import os

import cv2
from flask import Markup, send_file

from app import cmnUtils

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
                Markup(
                    '<span class="oshite__not__convert__char alert-secondary">&nbsp;&nbsp;') + cmnUtils.two_bytes_char(
                    kana) + Markup('&nbsp;&nbsp;</span>'))
            converted_list.append(Markup('</span>'))
    if after_br:
        converted_list.append(Markup('</span>'))
    return converted_list


def download_image(kana_list):
    cwd = os.getcwd()
    converted_kana_list = []
    converted_kana_temp_list = []
    for kana in kana_list:
        if hex(ord(kana)) in UNICODE_KANA:
            img = cv2.imread(
                cwd + '/app/static/images/oshiteFont/' + hex(ord(kana)) + FILE_TYPE_PNG)
            converted_kana_temp_list.append(cv2.resize(img, dsize=(0, 0), fx=0.5, fy=0.5))
        elif kana == "\r":
            converted_kana_list.append(converted_kana_temp_list)
            converted_kana_temp_list = []
    if len(converted_kana_temp_list) != 0:
        converted_kana_list.append(converted_kana_temp_list)

    im_tile = cv2.vconcat([cv2.hconcat(im_h) for im_h in converted_kana_list])
    connected_file = cwd + '/temp/created_image/' + cmnUtils.get_now_date_time() + FILE_TYPE_PNG
    cv2.imwrite(connected_file, im_tile)

    return send_file(connected_file, as_attachment=True,
                     download_name=os.path.basename(connected_file),
                     mimetype='image/png')


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
