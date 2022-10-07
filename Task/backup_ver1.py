import os
import time
# Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['C:\\Users\isidorov\Desktop']

# Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'D:\\Backup'

# Файлы помещаются в zip-архив.
# Именем для архива служит текущая дата и время.
target = target_dir + os.sep +time.strftime('%Y%m%d%H%M%S') + '.zip'

# Используем команду ZIP для помещения файлов в zip-архив
zip_command = "7z a {0} {1}".format(target, ' '.join(source))
print(zip_command)
# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')