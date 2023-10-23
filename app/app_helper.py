# This file is imported app.py
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
        print(is_other_char(kana))

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
    for kana in kana_list:
        im_a = cv2.imread(cwd + '/output/oshite/a.png')

    filepath = os.getcwd() + "/temp/created_image/0x304a.png"
    filename = os.path.basename(filepath)
    # attachment_filename
    return send_file(filepath, as_attachment=True,
                     download_name=filename,
                     mimetype='image/png')


def converted_new_line(words):
    return re.sub(r'\r\n|\r|\n', '\r', words)


def two_bytes_char(words):
    return words.translate(words.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))


def can_downloadable(kana):
    has_other_char = True
    kana_list = list(kana)

    for kana in kana_list:
        if is_other_char(kana):
            has_other_char = False
            break

    return has_other_char


def is_other_char(char):
    return hex(ord(char)) not in UNICODE_KANA and char != "\r"
