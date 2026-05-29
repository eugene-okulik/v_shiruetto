# result1 = 'result of operation: 42'
# result2 = 'result of operation: 54'
# result3 = 'result of operation: 209'
# result4 = 'result: 2'
#
# def add_me(fuck):
#     fuck = fuck.split()
#     return int(fuck[-1]) + 10
# print(add_me(result1), add_me(result2), add_me(result3), add_me(result4))

# def progression(limit=100):
#     n = 2
#     num = 1
#     count = 1
#     while count < limit:
#         yield num
#         num += n
#         count += 1
#
# for number in progression(11):
#     print(number)
def progression(limit=100):
    n = 1
    num = 1
    count = 1
    while count < limit:
        yield num
        num += n
        count += 1

count = 1
for number in progression(1000001):
    if count == 1000000:
        print(number)
        break
    count += 1