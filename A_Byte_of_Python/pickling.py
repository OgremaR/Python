import pickle

# имя файла, в котором мы сохраним объект
shoplistfile = 'shoplist.data'
# список покупак
shoplist = ['яблоки', 'манго', 'морковь']

# запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # Помещаем объект в файл
f.close()
del shoplist # уничтожаем переменную shoplist

# считываем с хранилища
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # загрузаем объект из списка
print(storedlist)