#### Обзор
Эта программа предоставляет интерфейс командной строки для выполнения трассировки маршрута до указанного доменного имени или IP-адреса. Она определяет каждый промежуточный узел на маршруте и отображает IP-адрес вместе с соответствующим номером автономной системы (AS).

#### Особенности
- При необходимости конвертирует доменное имя в IP-адрес.
- Выполняет трассировку маршрута для отслеживания пути пакетов до сетевого хоста.
- Получает номер автономной системы (AS) для каждого IP-адреса, встречающегося на маршруте.
- Выводит результаты в аккуратно оформленной таблице.

#### Зависимости
Для работы утилиты убедитесь, что у вас установлены следующие библиотеки Python:
- subprocess
- re
- socket
- requests
- sys
- prettytable

Установить необходимые зависимости можно с помощью pip:
pip install prettytable requests


#### Использование
Для использования этой утилиты:
1. Убедитесь, что Python установлен на вашей системе.
2. Сохраните скрипт в файл, например, traceroute.py.
3. Выполните скрипт с помощью Python из командной строки:
   
   python traceroute.py
   
4. По запросу введите доменное имя или IP-адрес.

#### Функции
- resolve_hostname(hostname): Преобразует предоставленное доменное имя в IP-адрес.
- traceroute(destination): Выполняет трассировку маршрута до указанного пункта назначения.
- get_as_number(ip): Получает номер AS для данного IP-адреса с использованием API сайта iptoasn.com.
- parse_traceroute(output): Разбирает вывод функции трассировки для извлечения IP-адресов.
- main(): Главная функция, которая управляет процессом трассировки и выводит результаты.

#### Пример
Когда вы запустите скрипт, введите доменное имя, например google.com, или IP-адрес.

Вывод будет отображаться в виде таблицы, показывающей каждый промежуточный узел, соответствующий IP-адрес и номер AS.

#### Устранение неполадок
- Этот скрипт использует кодировку и команды, специфичные для Windows (tracert). Если вы используете систему, отличную от Windows, измените команду трассировки согласно вашей системе (например, traceroute для систем Unix-like).
- Проверьте ваше интернет-соединение, если скрипт не может получить номера AS с API сайта iptoasn.com.

#### Примеры использования и вывода

Ввод: youtube.com                                                                                                                  
Вывод:                                                                                                                          
```
Трассировка маршрута к mad07s20-in-f14.1e100.net [216.58.211.238] 
с максимальным числом прыжков 30:

1     2 ms     2 ms     1 ms  192.168.0.1
2     1 ms     1 ms     4 ms  85.12.216.65
3    82 ms    14 ms    11 ms  10.10.8.93
4     1 ms     1 ms     1 ms  10.66.252.10
5     5 ms     2 ms     2 ms  217.24.176.200
6     2 ms     8 ms     2 ms  ebg06rb.transtelecom.net [188.43.34.234]
7    30 ms    21 ms    22 ms  mskn15-Lo1.transtelecom.net [217.150.55.234]
8    25 ms    34 ms    25 ms  Google-gw.transtelecom.net [188.43.10.141]
9    25 ms    24 ms    25 ms  108.170.250.99
10    44 ms    43 ms    43 ms  142.251.238.82
11    42 ms     *       42 ms  142.251.238.64
12    42 ms    43 ms    43 ms  192.178.105.59
13    42 ms    43 ms    49 ms  142.251.235.111
14    42 ms    42 ms     *     mad07s20-in-f14.1e100.net [216.58.211.238]
15    43 ms    45 ms    42 ms  mad07s20-in-f14.1e100.net [216.58.211.238]

Трассировка завершена.
Ошибка: Невозможно получить AS для IP 216.58.211.238.
Ошибка: Невозможно получить AS для IP 192.168.0.1.
Ошибка: Невозможно получить AS для IP 85.12.216.65.
Ошибка: Невозможно получить AS для IP 10.10.8.93.
Ошибка: Невозможно получить AS для IP 10.66.252.10.
Ошибка: Невозможно получить AS для IP 217.24.176.200.
Ошибка: Невозможно получить AS для IP 188.43.34.234.
Ошибка: Невозможно получить AS для IP 217.150.55.234.
Ошибка: Невозможно получить AS для IP 188.43.10.141.
Ошибка: Невозможно получить AS для IP 108.170.250.99.
Ошибка: Невозможно получить AS для IP 142.251.238.82.
Ошибка: Невозможно получить AS для IP 142.251.238.64.
Ошибка: Невозможно получить AS для IP 192.178.105.59.
Ошибка: Невозможно получить AS для IP 142.251.235.111.
Ошибка: Невозможно получить AS для IP 216.58.211.238.
Ошибка: Невозможно получить AS для IP 216.58.211.238.
+----+-----------------+-------------+
| №  |        IP       |      AS     |
+----+-----------------+-------------+
| 1  |  216.58.211.238 | Unavailable |
| 2  |   192.168.0.1   | Unavailable |
| 3  |   85.12.216.65  | Unavailable |
| 4  |    10.10.8.93   | Unavailable |
| 5  |   10.66.252.10  | Unavailable |
| 6  |  217.24.176.200 | Unavailable |
| 7  |  188.43.34.234  | Unavailable |
| 8  |  217.150.55.234 | Unavailable |
| 9  |  188.43.10.141  | Unavailable |
| 10 |  108.170.250.99 | Unavailable |
| 11 |  142.251.238.82 | Unavailable |
| 12 |  142.251.238.64 | Unavailable |
| 13 |  192.178.105.59 | Unavailable |
| 14 | 142.251.235.111 | Unavailable |
| 15 |  216.58.211.238 | Unavailable |
| 16 |  216.58.211.238 | Unavailable |
+----+-----------------+-------------+
```
                                                                                                                                                                              
Ввод: google.com                                                                                                                    
Вывод:                                                                                                                           
```
Трассировка маршрута к mad07s20-in-f14.1e100.net [216.58.211.238]``
с максимальным числом прыжков 30:```
1     1 ms     1 ms     5 ms  192.168.0.1
2     1 ms     1 ms     1 ms  85.12.216.65
3     8 ms     4 ms     2 ms  10.10.8.93
4     4 ms     1 ms     1 ms  10.66.252.10
5     2 ms     2 ms     3 ms  217.24.176.200
6     3 ms     *      222 ms  ebg06rb.transtelecom.net [188.43.34.234]
7     *       22 ms     *     mskn15-Lo1.transtelecom.net [217.150.55.234]
8    46 ms    25 ms    47 ms  Google-gw.transtelecom.net [188.43.10.141]
9    24 ms    27 ms    29 ms  108.170.250.99
10    49 ms    47 ms    51 ms  142.251.238.82
11    42 ms   116 ms    42 ms  142.251.238.64
12    43 ms    44 ms    43 ms  192.178.105.59
13    42 ms     *       44 ms  142.251.235.111
14    66 ms    45 ms    42 ms  mad07s20-in-f14.1e100.net [216.58.211.238]

Трассировка завершена.
Ошибка: Невозможно получить AS для IP 216.58.211.238.
Ошибка: Невозможно получить AS для IP 192.168.0.1.
Ошибка: Невозможно получить AS для IP 85.12.216.65.
Ошибка: Невозможно получить AS для IP 10.10.8.93.
Ошибка: Невозможно получить AS для IP 10.66.252.10.
Ошибка: Невозможно получить AS для IP 217.24.176.200.
Ошибка: Невозможно получить AS для IP 188.43.34.234.
Ошибка: Невозможно получить AS для IP 217.150.55.234.
Ошибка: Невозможно получить AS для IP 188.43.10.141.
Ошибка: Невозможно получить AS для IP 108.170.250.99.
Ошибка: Невозможно получить AS для IP 142.251.238.82.
Ошибка: Невозможно получить AS для IP 142.251.238.64.
Ошибка: Невозможно получить AS для IP 192.178.105.59.
Ошибка: Невозможно получить AS для IP 142.251.235.111.
Ошибка: Невозможно получить AS для IP 216.58.211.238.
+----+-----------------+-------------+
| №  |        IP       |      AS     |
+----+-----------------+-------------+
| 1  |  216.58.211.238 | Unavailable |
| 2  |   192.168.0.1   | Unavailable |
| 3  |   85.12.216.65  | Unavailable |
| 4  |    10.10.8.93   | Unavailable |
| 5  |   10.66.252.10  | Unavailable |
| 6  |  217.24.176.200 | Unavailable |
| 7  |  188.43.34.234  | Unavailable |
| 8  |  217.150.55.234 | Unavailable |
| 9  |  188.43.10.141  | Unavailable |
| 10 |  108.170.250.99 | Unavailable |
| 11 |  142.251.238.82 | Unavailable |
| 12 |  142.251.238.64 | Unavailable |
| 13 |  192.178.105.59 | Unavailable |
| 14 | 142.251.235.111 | Unavailable |
| 15 |  216.58.211.238 | Unavailable |
+----+-----------------+-------------+
```