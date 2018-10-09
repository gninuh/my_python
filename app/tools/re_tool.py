import re


def is_cellphone(str_):
    re_cellphone = re.compile(r'[1][^1269]\d{9}')
    res = re_cellphone.match(str_)
    if res:
        return True
    return False


def is_email(str_):
    re_email = re.compile(r'[^\._][\w\._-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+$')
    res = re_email.match(str_)
    if res:
        return True
    return False
