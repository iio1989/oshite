from distutils.util import strtobool
import re
import datetime

def convertBool(str: str)-> bool:
    if str == 'false':
        return False
    else:
        return bool(strtobool(str))

def convert_new_line(words):
    return re.sub(r'\r\n|\r|\n', '\r', words)


def two_bytes_char(words):
    return words.translate(words.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))


# return example: 2023-11-06-01:35:09
def get_now_date_time():
    return datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
