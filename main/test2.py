import base64

test = '< result of test1.py >'.encode()
exec(base64.b64decode(test))
