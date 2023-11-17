import os
import re
import datetime

CWD = os.getcwd()

RUN_BASE = os.getenv('run_base', 'DEV')


def convert_new_line(words):
    return re.sub(r'\r\n|\r|\n', '\r', words)


def two_bytes_char(words):
    return words.translate(words.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))


# return example: 2023-11-06-01:35:09
def get_now_date_time():
    return datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')


def img_base_dir():
    base_path = CWD
    if RUN_BASE == "DEV":
        base_path = base_path + '/app/static/images'
    else:
        base_path = base_path + '/static/images'
    return base_path
