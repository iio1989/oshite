# This file is imported app.py
import os
import shutil

import cv2
from flask import Markup, send_file

import cmnUtils
import imgUtils

cwd = os.getcwd()


# Convert Kana to List of OshiteImage.
def converted_kana_to_oshite(kana):
    kana_list = list(kana)
    converted_list = [Markup('<span class="oshite__not__convert__row">')]

    if len(kana) == 0:
        converted_list.append(Markup('&nbsp;&nbsp;') + "ひらがなが入力されていません。")

    url = "/static/images/oshiteFont/"
    after_br = False

    for kana in kana_list:
        if hex(ord(kana)) in imgUtils.UNICODE_KANA:
            converted_list.append(url + hex(ord(kana)) + imgUtils.FILE_TYPE_PNG)
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
    # 基本をして文字変換画像作成
    converted_kana_list = imgUtils.base_img_connect(kana_list)

    # フォルダ削除
    if os.path.isdir(cwd + '/temp/created_image/'):
        shutil.rmtree(cwd + '/temp/created_image/')

    # フォルダ作成
    os.mkdir(cwd + '/temp/created_image/')

    # imgファイル作成
    connected_file = cwd + '/temp/created_image/' + cmnUtils.get_now_date_time() + imgUtils.FILE_TYPE_PNG

    # 空白画像補助追加
    converted_kana_list = imgUtils.add_white_img(converted_kana_list)

    # 最終画像作成
    imgUtils.img_h_concat(converted_kana_list, connected_file)

    return send_file(connected_file, as_attachment=True,
                     download_name=os.path.basename(connected_file),
                     mimetype='image/png')
