my_dict = {
    'tuple': (1, 'text', False, 1.25, 'string'),
    'list': [1, 3, True, 1.25, 'string'],
    'dict': {'one': 1, 'two': 3, 'three': False, 'four': 1.25, 'five': 'string'},
    'set': {1, 4, False, 1.25, 'string'}}

print(my_dict['tuple'][-1])
my_dict['list'].append(42)
my_dict['list'].pop(2)
my_dict['dict'].pop('one')
my_dict['dict']['i am a tuple'] = 'right'
my_dict['set'].add('Calgary')
my_dict['set'].remove(1.25)
print(my_dict)
