#Модуль OS

#Вивести дані про комп'ютер

import os
print(os.environ)
print(os.environ['COMPUTERNAME'])

#Доступ до змінної оточення

print(os.getenv('COMPUTERNAME'))

#Можливі помилки
#print(os.environ['COMPUTERNAME2'])
#print(os.getenv('COMPUTERNAME2'))