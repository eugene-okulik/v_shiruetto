result1 = 'result of operation: 42'
result2 = 'result of operation: 54'
result3 = 'result of operation: 209'
result4 = 'result: 2'
def add_me(text):
    text = text.split()
    return int(text[-1]) + 10
print(add_me(result1), add_me(result2), add_me(result3), add_me(result4))