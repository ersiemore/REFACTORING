# Практическая работа: тестовые случаи и регрессионная проверка
# Группа 307
# Таблицы, описание дефекта и вывод лежат в README.md
# Ожидаемые результаты посчитаны вручную по требованиям до запуска


# ----- дополнительное задание -----
def check_result(actual, expected):
    if actual == expected:
        print("Пройдена")
        return True
    else:
        print("Не пройдена")
        return False


# то же самое, но возвращает текст (для таблиц)
def status(actual, expected):
    if actual == expected:
        return "Пройдена"
    return "Не пройдена"


# ----- Задание 1. Результат зачёта -----
def result_before(score):
    if score >= 50:
        answer = "Зачёт"
    else:
        answer = "Незачёт"
    return answer


def result_after(score):
    # ошибка: > вместо >=, 50 баллов не проходит
    if score > 50:
        return "Зачёт"
    return "Незачёт"


def result_fixed(score):
    # исправлено: вернул >=
    if score >= 50:
        return "Зачёт"
    return "Незачёт"


# ----- Задание 2. Стоимость печати -----
def print_cost_before(pages):
    total = pages * 30
    if pages >= 10:
        total = total * 0.9
    return total


def print_cost_after(pages):
    # ошибка: вычитается 0.1 тенге вместо скидки 10%
    if pages >= 10:
        return pages * 30 - 0.1
    return pages * 30


def print_cost_fixed(pages):
    # исправлено: умножаю на 0.9
    if pages >= 10:
        return pages * 30 * 0.9
    return pages * 30


# ----- Задание 3. Число есть, результата нет -----
def purchase_before(price, quantity):
    return price * quantity


def purchase_after(price, quantity):
    # ошибка: есть print, но нет return
    print(price * quantity)


def purchase_fixed(price, quantity):
    # исправлено: добавил return
    return price * quantity


# ----- Задание 4. Штраф за просрочку -----
def fine_before(days):
    if days < 0:
        return "Ошибка"
    elif days <= 3:
        return 0
    else:
        return (days - 3) * 100


def fine_after(days):
    # ошибка 1: нет проверки days < 0
    # ошибка 2: days * 100 вместо (days - 3) * 100
    if days <= 3:
        return 0
    return days * 100


def fine_fixed(days):
    # исправлено обе ошибки
    if days < 0:
        return "Ошибка"
    if days <= 3:
        return 0
    return (days - 3) * 100


# ----- Задание 5. Классы и наследование -----
class StudentBefore:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_result(self):
        if self.score >= 50:
            return "Зачёт"
        return "Незачёт"


class GrantStudentBefore(StudentBefore):
    def get_result(self):
        if self.score >= 70:
            return "Грант сохранён"
        return "Грант не сохранён"


class StudentAfter:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_result(self):
        # ошибка 1: > вместо >=
        if self.score > 50:
            return "Зачёт"
        return "Незачёт"


class GrantStudentAfter(StudentAfter):
    # ошибка 2: из-за pass метод берётся у Student
    pass


# исправленные классы
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_result(self):
        if self.score >= 50:
            return "Зачёт"
        return "Незачёт"


class GrantStudent(Student):
    # вернул переопределение метода
    def get_result(self):
        if self.score >= 70:
            return "Грант сохранён"
        return "Грант не сохранён"


# ----- Тестовые данные (вход, ожидаемый результат) -----
tests1 = [(0, "Незачёт"), (49, "Незачёт"), (50, "Зачёт"), (51, "Зачёт"), (100, "Зачёт")]

# 10 стр: 10*30*0.9 = 270, 11 стр: 11*30*0.9 = 297, 20 стр: 20*30*0.9 = 540
# 20 - моя дополнительная проверка со скидкой
tests2 = [(0, 0), (1, 30), (9, 270), (10, 270), (11, 297), (20, 540)]

# 4 дня: (4-3)*100 = 100, 5 дней: 200, 10 дней: 700
tests4 = [(-1, "Ошибка"), (0, 0), (3, 0), (4, 100), (5, 200), (10, 700)]


def run_tests(title, tests, f_before, f_after, f_fixed):
    print()
    print(title)
    print("№ | Вход | Ожидаемый | До рефакторинга | После рефакторинга | Статус | После исправления | Повторный статус")
    number = 1
    for value, expected in tests:
        before = f_before(value)
        after = f_after(value)
        fixed = f_fixed(value)
        print(number, "|", value, "|", expected, "|", before, "|", after, "|",
              status(after, expected), "|", fixed, "|", status(fixed, expected))
        number += 1


run_tests("Задание 1. Результат зачёта", tests1, result_before, result_after, result_fixed)
run_tests("Задание 2. Стоимость печати", tests2, print_cost_before, print_cost_after, print_cost_fixed)


# задание 3
print()
print("Задание 3. Число есть, результата нет")
# до запуска думаю: на экране будет 1400, а new_result будет None
old_result = purchase_before(700, 2)
new_result = purchase_after(700, 2)
print("Старая версия вернула:", old_result)
print("Новая версия вернула:", new_result)

# после исправления
balance = 5000 - purchase_fixed(700, 2)
print("Остаток:", balance)

print("1 | 700, 2 | 1400 |", new_result, "|", status(new_result, 1400), "|",
      purchase_fixed(700, 2), "|", status(purchase_fixed(700, 2), 1400))
print("2 | 5000 - покупка | 3600 | TypeError (5000 - None) | Не пройдена |",
      balance, "|", status(balance, 3600))

run_tests("Задание 4. Штраф за просрочку", tests4, fine_before, fine_after, fine_fixed)


# задание 5
print()
print("Задание 5. Классы и наследование")
print("№ | Вход | Ожидаемый | До рефакторинга | После рефакторинга | Статус | После исправления | Повторный статус")

students = [(49, "Незачёт"), (50, "Зачёт"), (51, "Зачёт")]
grants = [(69, "Грант не сохранён"), (70, "Грант сохранён"), (71, "Грант сохранён")]

number = 1
for score, expected in students:
    before = StudentBefore("Аскар", score).get_result()
    after = StudentAfter("Аскар", score).get_result()
    fixed = Student("Аскар", score).get_result()
    print(number, "| Student", score, "|", expected, "|", before, "|", after, "|",
          status(after, expected), "|", fixed, "|", status(fixed, expected))
    number += 1

for score, expected in grants:
    before = GrantStudentBefore("Аскар", score).get_result()
    after = GrantStudentAfter("Аскар", score).get_result()
    fixed = GrantStudent("Аскар", score).get_result()
    print(number, "| GrantStudent", score, "|", expected, "|", before, "|", after, "|",
          status(after, expected), "|", fixed, "|", status(fixed, expected))
    number += 1

# проверка конструктора
s = Student("Айгуль", 88)
g = GrantStudent("Данияр", 72)
print()
print("Student:", s.name, s.score)
print("GrantStudent:", g.name, g.score)
print("Конструктор работает:", s.name == "Айгуль" and s.score == 88 and g.name == "Данияр" and g.score == 72)


# проверка check_result
print()
print("Проверка check_result:")
check_result(result_fixed(50), "Зачёт")
check_result(result_after(50), "Зачёт")
