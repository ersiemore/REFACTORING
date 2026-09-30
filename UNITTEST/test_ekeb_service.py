import unittest
from ekeb_service import print_cost, exam_result, Student, GrantStudent, ExcellentStudent


# ---------- Задание 1. Стоимость печати ----------
class TestPrintCost(unittest.TestCase):

    def test_zero_pages(self):
        self.assertEqual(print_cost(0), 0)

    def test_one_page(self):
        self.assertEqual(print_cost(1), 30)

    def test_nine_pages_no_discount(self):
        # 9 * 30 = 270
        self.assertEqual(print_cost(9), 270)

    def test_ten_pages_discount(self):
        # 10 * 30 * 0.9 = 270
        self.assertAlmostEqual(print_cost(10), 270)

    def test_eleven_pages_discount(self):
        # 11 * 30 * 0.9 = 297
        self.assertAlmostEqual(print_cost(11), 297)

    def test_negative_pages(self):
        with self.assertRaises(ValueError):
            print_cost(-1)


# ---------- Задание 2. Результат экзамена ----------
class TestExamResult(unittest.TestCase):

    def test_score_minus_one(self):
        with self.assertRaises(ValueError):
            exam_result(-1)

    def test_score_zero(self):
        self.assertEqual(exam_result(0), "Незачёт")

    def test_score_49(self):
        self.assertEqual(exam_result(49), "Незачёт")

    def test_score_50_boundary(self):
        self.assertEqual(exam_result(50), "Зачёт")

    def test_score_51(self):
        self.assertEqual(exam_result(51), "Зачёт")

    def test_score_100(self):
        self.assertEqual(exam_result(100), "Зачёт")

    def test_score_101(self):
        with self.assertRaises(ValueError):
            exam_result(101)


# ---------- Задание 3. Класс Student ----------
class TestStudent(unittest.TestCase):

    def setUp(self):
        # новый объект перед каждым тестом
        self.student = Student("Алия", 50)

    def test_name(self):
        self.assertEqual(self.student.name, "Алия")

    def test_start_score(self):
        self.assertEqual(self.student.score, 50)

    def test_has_passed_on_boundary_50(self):
        self.assertTrue(self.student.has_passed())

    def test_has_not_passed_49(self):
        student = Student("Ерлан", 49)
        self.assertFalse(student.has_passed())

    def test_has_passed_returns_bool(self):
        self.assertIsInstance(self.student.has_passed(), bool)

    def test_add_ten_points(self):
        result = self.student.add_points(10)
        self.assertEqual(result, 60)

    def test_add_points_changes_score(self):
        self.student.add_points(10)
        self.assertEqual(self.student.score, 60)

    def test_max_score_100(self):
        # 50 + 60 = 110, но должно быть 100
        result = self.student.add_points(60)
        self.assertEqual(result, 100)

    def test_add_negative_points(self):
        with self.assertRaises(ValueError):
            self.student.add_points(-5)


# ---------- Задание 4. Наследование ----------
class TestGrantStudent(unittest.TestCase):

    def setUp(self):
        self.student = GrantStudent("Данияр", 69)

    def test_is_instance_of_student(self):
        self.assertIsInstance(self.student, Student)

    def test_grant_status_69(self):
        self.assertEqual(GrantStudent("Данияр", 69).grant_status(), "Грант не сохранён")

    def test_grant_status_70_boundary(self):
        self.assertEqual(GrantStudent("Данияр", 70).grant_status(), "Грант сохранён")

    def test_grant_status_71(self):
        self.assertEqual(GrantStudent("Данияр", 71).grant_status(), "Грант сохранён")

    def test_inherited_add_points(self):
        # метод add_points берётся у Student
        self.assertEqual(self.student.add_points(1), 70)

    def test_grant_after_adding_points(self):
        # 69 -> грант не сохранён, после +1 балла должен сохраниться
        self.assertEqual(self.student.grant_status(), "Грант не сохранён")
        self.student.add_points(1)
        self.assertEqual(self.student.grant_status(), "Грант сохранён")

    def test_inherited_has_passed(self):
        self.assertTrue(self.student.has_passed())


# ---------- Дополнительное задание. ExcellentStudent ----------
class TestExcellentStudent(unittest.TestCase):

    def test_is_instance_of_student(self):
        self.assertIsInstance(ExcellentStudent("Аружан", 80), Student)

    def test_scholarship_74(self):
        self.assertEqual(ExcellentStudent("Аружан", 74).scholarship(), 0)

    def test_scholarship_75(self):
        self.assertEqual(ExcellentStudent("Аружан", 75).scholarship(), 15000)

    def test_scholarship_89(self):
        self.assertEqual(ExcellentStudent("Аружан", 89).scholarship(), 15000)

    def test_scholarship_90(self):
        self.assertEqual(ExcellentStudent("Аружан", 90).scholarship(), 30000)

    def test_scholarship_100(self):
        self.assertEqual(ExcellentStudent("Аружан", 100).scholarship(), 30000)


if __name__ == "__main__":
    unittest.main()
