import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['C:\\Users\isidorov\Desktop']

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'D:\\Backup'

# 3. Файлы помещаются в zip-архив.
# 4. Текущее дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0: # проверяем введен ли комментарий
    target = today + os.sep + now + '.7z'
else:
    target = today + os.sep + now + '_' +\
         comment.replace(' ', '_') + '.7z'
# создаем каталог, если его ещё нет.
if not os.path.exists(today):
    os.mkdir(today) # создание каталога
print('Каталог успешно создан', today)
# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "7zFM.exe a {0} {1}".format(target, ' '.join(source))

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')