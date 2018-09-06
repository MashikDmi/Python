# hard 1
string = "y = -12x + 11111140.2121"
x = 2.5
string_list = string.split("x")
a = float(string_list[0][string_list[0].find("=")+1:].strip())
b = float(string_list[1][2:].strip())
print(a*x + b)

# hard 2
data = input("Введите дату в формате dd.mm.yyyy:")
data_list = data.split(".")
days_in_month = {"01":"31", "02":"30", "03":"31", "04":"30", "05":"31", "06":"30",
                 "07":"31", "08":"31", "09":"30", "10":"31", "11":"30", "12":"31"}
if len(data_list[0]) == 2 and len(data_list[1]) == 2 and len(data_list[2]) == 4:
    if int(data_list[1]) >= 1 and int(data_list[1]) <= 12:
        if int(data_list[2]) >= 1 and int(data_list[2]) <= 9999:
            if int(data_list[0]) >= 1 and int(data_list[0]) <= 31:
                flag = False
                for month in days_in_month:
                    if data_list[1] == month and data_list[0] <= days_in_month[month]:
                        print("Дата введена корректно")
                        flag = True
                if flag == False:
                    print("Количество дней не соответствует указанному месяцу")
            else:
                print("В веденной дате некорректно указан день")
        else:
            print("В веденной дате некорректно указан год")
    else:
        print("В веденной дате некорректно указан месяц")
else:
    print("Формат веденной даты не соответсвует шаблону dd.mm.yyyy")

# hard 3
number = 11
floor = 1
flat = 1
floor_result = 0
while number > 0:
    for floor_i in range(floor):
        floor_result = floor_result + 1
        for flat_i in range(flat):
            number = number - 1
            if number == 0:
                print("Этаж: {}, порядковый номер слева на этаже: {}".format(floor_result, flat_i + 1))
                break
    floor = floor + 1
    flat = flat + 1
