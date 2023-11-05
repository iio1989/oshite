import re
import datetime

import cv2


def convert_new_line(words):
    return re.sub(r'\r\n|\r|\n', '\r', words)


def two_bytes_char(words):
    return words.translate(words.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))


# return example: 2023-11-06-01:35:09
def get_now_date_time():
    return datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')


def concat_tile(im_2d):
    return cv2.vconcat([cv2.hconcat(im_h) for im_h in im_2d])
