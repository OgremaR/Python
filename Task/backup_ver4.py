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
if len(comment) == 0: # проверяем, введен ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +\
        comment.replace(' ', '_') + '.zip'

# Создаём каталогб если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) # Создание каталога
print('Каталог успешно создан', today)

# 5. используем комманду "7z" для помещение файлов в архив
zip_command = "7z a {0} {1}".format(target, ' '.join(source))

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервноя копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')