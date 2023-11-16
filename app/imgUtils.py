import os

import cv2

cwd = os.getcwd()

# oshite image file extension.
FILE_TYPE_PNG = ".png"

# oshite image names.
UNICODE_KANA = ["0x3042", "0x3044", "0x3046", "0x3048", "0x304a", "0x304b", "0x304d", "0x304f", "0x3051", "0x3053",
                "0x3055", "0x3057", "0x3059",
                "0x305b", "0x305d", "0x305f", "0x3061", "0x3064", "0x3066", "0x3068", "0x306a", "0x306b", "0x306c",
                "0x306d", "0x306e", "0x306f", "0x3072",
                "0x3075", "0x3078", "0x307b", "0x307e", "0x307f", "0x3080", "0x3081", "0x3082", "0x3089", "0x308a",
                "0x308b", "0x308c", "0x308d", "0x3084", "0x3086", "0x3088", "0x308f", "0x3092", "0x3093"]


# convert input kana to woshite img
def base_img_connect(kana_list):
    converted_kana_list = []
    temp_list = []
    for kana in kana_list:
        if hex(ord(kana)) in UNICODE_KANA:
            img = cv2.imread(
                cwd + '/static/images/oshiteFont/' + hex(ord(kana)) + FILE_TYPE_PNG)
            temp_list.append(cv2.resize(img, dsize=(0, 0), fx=0.5, fy=0.5))
        elif kana == "\r":
            converted_kana_list.append(temp_list)
            temp_list = []

    if len(temp_list) != 0:
        converted_kana_list.append(temp_list)
    return converted_kana_list


# create png and img connect
def img_h_concat(converted_kana_list, connected_file):
    image_tile = cv2.vconcat([cv2.hconcat(im_h) for im_h in converted_kana_list])
    cv2.imwrite(connected_file, image_tile)


# add white img
def add_white_img(converted_kana_list):
    word_lens = []
    for im_h in converted_kana_list:
        word_lens.append(len(im_h))
    word_len_max = max(word_lens)
    for im_h in converted_kana_list:
        if len(im_h) < word_len_max:
            add_count = word_len_max - len(im_h)
            img = cv2.imread(cwd + '/static/images/adjustImg/white01.png')
            num = 0
            while num < add_count:
                im_h.append(cv2.resize(img, dsize=(48, 30)))
                num = num + 1
    return converted_kana_list


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
