import unittest

from course_service import Course, IntensiveCourse


class TestCourse(unittest.TestCase):
    # Stage 1: Course creation
    def test_course_stores_name_and_capacity(self):
        course = Course("Python", 20)
        self.assertEqual(course.name, "Python")
        self.assertEqual(course.capacity, 20)

    def test_new_course_has_zero_enrolled(self):
        course = Course("Python", 20)
        self.assertEqual(course.enrolled, 0)

    def test_empty_name_raises_value_error(self):
        with self.assertRaises(ValueError):
            Course("", 20)

    def test_whitespace_name_raises_value_error(self):
        with self.assertRaises(ValueError):
            Course("   ", 20)

    def test_zero_capacity_raises_value_error(self):
        with self.assertRaises(ValueError):
            Course("Python", 0)

    def test_negative_capacity_raises_value_error(self):
        with self.assertRaises(ValueError):
            Course("Python", -1)

    def test_non_integer_capacity_raises_value_error(self):
        with self.assertRaises(ValueError):
            Course("Python", 2.5)

    # Stage 2: available_places
    def test_available_places_on_new_course(self):
        course = Course("Python", 3)
        self.assertEqual(course.available_places(), 3)

    # Stage 3: enroll
    def test_enroll_increases_enrolled_and_returns_remaining_places(self):
        course = Course("Python", 3)
        remaining = course.enroll()
        self.assertEqual(course.enrolled, 1)
        self.assertEqual(remaining, 2)

    def test_multiple_enrollments_are_counted(self):
        course = Course("Python", 3)
        self.assertEqual(course.enroll(), 2)
        self.assertEqual(course.enroll(), 1)
        self.assertEqual(course.enroll(), 0)
        self.assertEqual(course.enrolled, 3)

    def test_enroll_on_last_free_place_fills_course(self):
        course = Course("Python", 1)
        self.assertEqual(course.enroll(), 0)
        self.assertTrue(course.is_full)

    def test_enroll_beyond_capacity_raises_value_error(self):
        course = Course("Python", 1)
        course.enroll()
        with self.assertRaisesRegex(ValueError, "Нет свободных мест"):
            course.enroll()

    # Stage 4: cancel_enrollment
    def test_cancel_after_enrollment_decreases_enrolled(self):
        course = Course("Python", 2)
        course.enroll()
        course.cancel_enrollment()
        self.assertEqual(course.enrolled, 0)
        self.assertEqual(course.available_places(), 2)

    def test_cancel_when_no_students_are_registered_raises_value_error(self):
        course = Course("Python", 2)
        with self.assertRaisesRegex(ValueError, "Нет зарегистрированных студентов"):
            course.cancel_enrollment()

    def test_cancel_restores_free_place(self):
        course = Course("Python", 2)
        course.enroll()
        course.enroll()
        self.assertTrue(course.is_full)
        course.cancel_enrollment()
        self.assertEqual(course.available_places(), 1)
        self.assertFalse(course.is_full)

    # Stage 5: is_full
    def test_is_full_is_false_for_empty_course(self):
        course = Course("Python", 2)
        self.assertFalse(course.is_full)

    def test_is_full_is_false_for_partially_filled_course(self):
        course = Course("Python", 2)
        course.enroll()
        self.assertFalse(course.is_full)

    def test_is_full_is_true_for_full_course(self):
        course = Course("Python", 2)
        course.enroll()
        course.enroll()
        self.assertTrue(course.is_full)


class TestIntensiveCourse(unittest.TestCase):
    # Stage 6: IntensiveCourse
    def test_intensive_course_is_instance_of_course(self):
        course = IntensiveCourse("Backend", 10, 8)
        self.assertIsInstance(course, Course)

    def test_hours_6_have_medium_workload(self):
        course = IntensiveCourse("Backend", 10, 6)
        self.assertEqual(course.workload_level(), "средняя")

    def test_hours_10_have_medium_workload(self):
        course = IntensiveCourse("Backend", 10, 10)
        self.assertEqual(course.workload_level(), "средняя")

    def test_hours_11_have_high_workload(self):
        course = IntensiveCourse("Backend", 10, 11)
        self.assertEqual(course.workload_level(), "высокая")

    def test_hours_20_have_high_workload(self):
        course = IntensiveCourse("Backend", 10, 20)
        self.assertEqual(course.workload_level(), "высокая")

    def test_hours_5_raise_value_error(self):
        with self.assertRaises(ValueError):
            IntensiveCourse("Backend", 10, 5)

    def test_hours_21_raise_value_error(self):
        with self.assertRaises(ValueError):
            IntensiveCourse("Backend", 10, 21)

    def test_non_integer_hours_raise_value_error(self):
        with self.assertRaises(ValueError):
            IntensiveCourse("Backend", 10, 7.5)

    def test_inherited_enroll_available_places_and_is_full_work(self):
        course = IntensiveCourse("Backend", 1, 12)
        self.assertEqual(course.available_places(), 1)
        self.assertEqual(course.enroll(), 0)
        self.assertTrue(course.is_full)
        with self.assertRaises(ValueError):
            course.enroll()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
