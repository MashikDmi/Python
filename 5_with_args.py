# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def cp():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    filename, file_extension = os.path.splitext(file_name)
    try:
        shutil.copyfile(file_name, "{}_copy{}".format(filename, file_extension))
        print("Файл {} скопирован".format(file_name))
    except FileNotFoundError:
        print("Файл с именем {} не найден, копирование невозможно".format(file_name))

def rm():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        os.remove(file_name)
        print("Файл {} удален".format(file_name))
    except FileNotFoundError:
        print("Файл с именем {} не найден, удаление невозможно".format(file_name))
    except PermissionError:
        print("Вторым параметром указана папка, необходимо указать файл")

def cd():
    if not file_name:
        print("Необходимо указать имя директории вторым параметром (полный путь)")
        return
    try:
        os.chdir(file_name)
        print("Выполнен переход в директорию: {}".format(file_name))
    except FileNotFoundError:
        print("Не удается найти указанную директорию: {}".format(file_name))

def ls():
    print(os.getcwd())

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "ls": ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None
try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")