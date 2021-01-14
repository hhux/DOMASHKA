import os
import fnmatch

# Счетчики файлов
cnt_exe = 0
cnt_py = 0
cnt_dir = 0
cnt_all = 0

for base, dirs, files in os.walk('C:\Python37-32'):
    for directories in dirs:
        cnt_dir += 1
    for Files in files:
        cnt_all += 1

    for file in os.listdir('C:\Python37-32'):
        if fnmatch.fnmatch(file, '*.exe'):
            cnt_exe += 1

    for file in os.listdir('C:\Python37-32'):
        if fnmatch.fnmatch(file, '*.py'):
            cnt_py += 1

# Запись в файл. Не разобрался как красиво записать
with open('file_for_links.txt', 'w', encoding='utf-8') as f:
    f.write('Файлов с разрешением ".exe"=' + str(cnt_exe))

    f.write('\n')

    f.write('Файлов с разрешением ".py"=' + str(cnt_py))

    f.write('\n')

    f.write('Всего файлов=' + str(cnt_all))

    f.write('\n')

    f.write('Количество папок=' + str(cnt_dir))
