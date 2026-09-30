# Сервис колледжа EKEB (исправленная версия)


def print_cost(pages):
    # исправлено: отрицательное количество - ошибка, а не 0
    if pages < 0:
        raise ValueError("Количество страниц не может быть отрицательным")
    total = pages * 30
    # исправлено: скидка от 10 страниц включительно
    if pages >= 10:
        total = total * 0.9
    return total


def exam_result(score):
    if score < 0 or score > 100:
        raise ValueError("Недопустимый балл")
    # исправлено: >= вместо >
    if score >= 50:
        return "Зачёт"
    return "Незачёт"


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def has_passed(self):
        # исправлено: >= вместо >
        return self.score >= 50

    def add_points(self, points):
        # исправлено: нельзя добавлять отрицательные баллы
        if points < 0:
            raise ValueError("Баллы не могут быть отрицательными")
        # исправлено: максимум 100
        self.score = self.score + points
        if self.score > 100:
            self.score = 100
        return self.score


class GrantStudent(Student):
    # исправлено: вместо pass добавлен метод grant_status
    def grant_status(self):
        if self.score >= 70:
            return "Грант сохранён"
        return "Грант не сохранён"


# дополнительное задание
class ExcellentStudent(Student):
    def scholarship(self):
        if self.score >= 90:
            return 30000
        elif self.score >= 75:
            return 15000
        return 0
