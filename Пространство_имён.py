#Функция для подсчёта количества вызовов остальных функций
def count_calls():
    global calls
    calls += 1

#Функция для вывода изменённой строки и её длины
def string_info(string):
    count_calls()
    tup = (len(string), string.upper(), string.lower())
    return tup

#Функция для поиска строки в списке
def is_contains(string, list_to_search):
    count_calls()
    bol = string.lower() in map(str.lower, list_to_search)
    return bol

calls = 0

print(string_info('ArchiTecTURe'))
print(string_info('ThE WiTnEsS'))
print(is_contains('lite', ['recycling', 'cyclic']))
print(is_contains('RWBY', ['RUby', 'Rwbyk', 'Rwby']))
print(calls)