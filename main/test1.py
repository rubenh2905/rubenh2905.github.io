import base64

test = b''' 
def hello():
    print('hello world!')

hello()
'''
test = test.decode()
test = bytes(test, 'utf-8')
my_enc = base64.b64encode(test)
print(my_enc.decode("utf-8"))
