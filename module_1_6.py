my_dict = {
    "Алексей": 1985,
    "Мария": 1992,
    "Сергей": 1978
}
print(my_dict)
print(my_dict.get("Мария"))
print(my_dict.get("Никита", "Ключ не найден"))
print(my_dict.get("Мария"))
print(my_dict.get("Никита", "Ключ не найден"))
my_dict["Дмитрий"] = 2000
my_dict["Екатерина"] = 1988
удалённое_значение = my_dict.pop("Сергей", "Ключ не найден")
print(удалённое_значение)
print(my_dict)
my_set = {1, 2, 2, 3.5, "Привет", "Привет"}
my_set.add(4)
my_set.add("Мир")
my_set.remove(3.5)
print(my_set)
