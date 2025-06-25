person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country, sep=', ')

result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'
result_4 = 'результат работы программы: 10'  # пример для любого числа
new_result_1 = int(result_1[result_1.index('42'):]) + 10
new_result_2 = int(result_2[result_2.index('514'):]) + 10
new_result_3 = int(result_3[result_3.index('9'):]) + 10
new_result_4 = int(result_4.split(': ')[1]) + 10
print(new_result_1)
print(new_result_2)
print(new_result_3)
print(new_result_4)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students = ', '.join(students)
subjects = ', '.join(subjects)
print('Students', students, 'study these subjects:', subjects)