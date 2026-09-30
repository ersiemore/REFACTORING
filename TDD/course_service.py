"""Service for registering students on EKEB courses.

Implemented according to the practical task on TDD and code coverage.
"""


class Course:
    """Base course with capacity and student enrollment management."""

    def __init__(self, name: str, capacity: int) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название курса не может быть пустым")
        if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Количество мест должно быть положительным целым числом")

        self.name = name
        self.capacity = capacity
        self.enrolled = 0

    def available_places(self) -> int:
        """Return the number of free places on the course."""
        return self.capacity - self.enrolled

    def enroll(self) -> int:
        """Register one student and return the number of free places remaining."""
        if self.is_full:
            raise ValueError("Нет свободных мест на курсе")

        self.enrolled += 1
        return self.available_places()

    def cancel_enrollment(self) -> None:
        """Cancel one enrollment."""
        if self.enrolled == 0:
            raise ValueError("Нет зарегистрированных студентов для отмены")

        self.enrolled -= 1

    @property
    def is_full(self) -> bool:
        """Return True when the course has reached its capacity."""
        return self.enrolled == self.capacity


class IntensiveCourse(Course):
    """Course with a weekly workload requirement."""

    def __init__(self, name: str, capacity: int, hours_per_week: int) -> None:
        super().__init__(name, capacity)

        if isinstance(hours_per_week, bool) or not isinstance(hours_per_week, int):
            raise ValueError("Количество часов в неделю должно быть целым числом от 6 до 20")
        if not 6 <= hours_per_week <= 20:
            raise ValueError("Количество часов в неделю должно быть от 6 до 20")

        self.hours_per_week = hours_per_week

    def workload_level(self) -> str:
        """Return the workload level based on weekly hours."""
        if self.hours_per_week <= 10:
            return "средняя"
        return "высокая"
