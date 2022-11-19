# This file is imported app.py
import re

from flask import Markup

# oshite image names.
UNICODE_KANA = ["0x3042", "0x3044", "0x3046", "0x3048", "0x304a", "0x304b", "0x304d", "0x304f", "0x3051", "0x3053",
                "0x3055", "0x3057", "0x3059",
                "0x305b", "0x305d", "0x305f", "0x3061", "0x3064", "0x3066", "0x3068", "0x306a", "0x306b", "0x306c",
                "0x306d", "0x306e", "0x306f", "0x3072",
                "0x3075", "0x3078", "0x307b", "0x307e", "0x307f", "0x3080", "0x3081", "0x3082", "0x3089", "0x308a",
                "0x308b", "0x308c", "0x308d", "0x3084", "0x3086", "0x3088", "0x308f", "0x3092", "0x3093"]

# oshite image file extension.
FILE_TYPE_PNG = ".png"


# Convet Kana to List of OshiteImage.
def getConvetedStr_kanaToOshite(kana):
    kanaList = list(kana)
    converted_list = []
    converted_list.append(Markup('<span class="oshite__not__covered__row">'))

    url = "/static/images/oshiteFont/"
    after_br = False

    for kana in kanaList:

        if hex(ord(kana)) in UNICODE_KANA:
            converted_list.append(url + hex(ord(kana)) + FILE_TYPE_PNG)
        elif kana == "\r":
            after_br = True
            converted_list.append(Markup('</span>'))
            converted_list.append(Markup('<span class="oshite__not__covered__row">'))
        else:
            converted_list.append(Markup('<span class="oshite__not__covered">'))
            converted_list.append(Markup('<span class="oshite__not__covered__char__padding">'))
            converted_list.append(Markup('</span>'))
            converted_list.append(
                Markup('<span class="oshite__not__covered__char alert-secondary">&nbsp;&nbsp;') + getTwoBytesChar(
                    kana) + Markup('&nbsp;&nbsp;</span>'))
            converted_list.append(Markup('</span>'))
    if len(converted_list) == 0:
        converted_list.append("文字が入力されていません。")
    if after_br:
        converted_list.append(Markup('</span>'))
    return converted_list


def getConvetedStr_kanaToOshite_old_design(kana):
    kanaList = list(kana)
    converted_list = []
    url = "/static/old_design/images/oshiteFont/"

    for kana in kanaList:
        if hex(ord(kana)) in UNICODE_KANA:
            converted_list.append(url + hex(ord(kana)) + FILE_TYPE_PNG)
        elif kana == "\r":
            converted_list.append(Markup('<br>'))
        else:
            converted_list.append(kana)
    if len(converted_list) == 0:
        converted_list.append("文字が入力されていません。")
    return converted_list


def getConvetedNewline(str):
    return re.sub(r'\r\n|\r|\n', '\r', str)


def getTwoBytesChar(str):
    return str.translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))
