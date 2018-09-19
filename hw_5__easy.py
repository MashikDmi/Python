# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

def create_folders(begin, end):
    for i in range(begin, end+1):
        dir_path = os.path.join(os.getcwd(), "dir_{}".format(i))
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print("Директория с именем dir_{} уже существует".format(i))
#create_folders(1, 9)

def create_folders_for_nomal(name):
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print("Папка с именем {} успешно создана".format(name))
    except FileExistsError:
        print("Папка с именем {} уже существует, папка не была создана".format(name))
#create_folders_for_nomal("test")

def delete_folders(begin, end):
    for i in range(begin, end+1):
        dir_path = os.path.join(os.getcwd(), "dir_{}".format(i))
        try:
            os.rmdir(dir_path)
        except FileNotFoundError:
            print("Директория с именем dir_{} не найдена".format(i))
        except OSError:
            print("Директория с именем dir_{} не пуста".format(i))

def delete_folders_for_normal(name):
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.rmdir(dir_path)
        print("Папка с именем {} успешно удалена".format(name))
    except FileNotFoundError:
        print("Папка с именем {} не найдена, папка не была удалена".format(name))
    except OSError:
        print("Папка с именем {} не пуста, папка не была удалена".format(name))
#delete_folders(1, 9)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def view():
    for name in os.listdir():
        #if os.path.isdir(name):
        print(name)
#view()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
#os.system("copy {} {}".format(__file__, r"{}\test.py".format(os.getcwd())))
def my_copy():
    filename, file_extension = os.path.splitext(__file__)
    shutil.copyfile(__file__, "{}_copy{}".format(filename, file_extension))
#my_copy()