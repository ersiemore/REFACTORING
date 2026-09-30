# Автоматические тесты функций и классов (unittest)

Практическая работа, группа 307.

Цель: написать модульные тесты с помощью `unittest`, найти дефекты в коде, исправить их и подтвердить исправление повторным запуском.

## Файлы

- `ekeb_service.py` - исправленный код (функции `print_cost`, `exam_result`, классы `Student`, `GrantStudent`, `ExcellentStudent`)
- `test_ekeb_service.py` - тесты (35 штук)
- `README.md` - результаты запусков, таблица, описание дефекта, вывод, ответы на вопросы

## Как запустить

```
python -m unittest test_ekeb_service.py
python -m unittest discover
python -m unittest -v
```

## Как я делал работу

1. Создал `ekeb_service.py` с кодом из задания.
2. Написал `test_ekeb_service.py` до исправления программы. Ожидаемые значения взял из требований, а не из ответов программы.
3. Запустил тесты и записал ошибки.
4. Исправил код в `ekeb_service.py` (места исправлений помечены комментариями `# исправлено`).
5. Запустил весь набор тестов ещё раз.

Класс `ExcellentStudent` (дополнительное задание) новый, поэтому он уже был в файле при первом запуске, чтобы тесты могли импортироваться.

## Какие тесты написаны

| Задание | Класс тестов | Проверяемые значения |
|---|---|---|
| 1. Стоимость печати | `TestPrintCost` | 0, 1, 9, 10, 11 страниц и -1 (`assertRaises`) |
| 2. Результат экзамена | `TestExamResult` | -1, 0, 49, 50, 51, 100, 101 |
| 3. Класс Student | `TestStudent` | имя, начальный балл, граница 50, тип `bool`, +10 баллов, максимум 100, отрицательные баллы. Объект создаётся в `setUp()` |
| 4. Наследование | `TestGrantStudent` | `isinstance`, статус при 69, 70, 71, унаследованный `add_points()`, грант после добавления баллов |
| Дополнительно | `TestExcellentStudent` | стипендия при 74, 75, 89, 90, 100 |

Ожидаемые значения, рассчитанные вручную: 10 страниц = 10 × 30 × 0,9 = 270; 11 страниц = 11 × 30 × 0,9 = 297; 9 страниц = 270 (без скидки).

## Результат первого запуска (до исправления)

```
TestExamResult.test_score_100 ... ok
TestExamResult.test_score_101 ... ok
TestExamResult.test_score_49 ... ok
TestExamResult.test_score_50_boundary ... FAIL
TestExamResult.test_score_51 ... ok
TestExamResult.test_score_minus_one ... ok
TestExamResult.test_score_zero ... ok
TestExcellentStudent.test_is_instance_of_student ... ok
TestExcellentStudent.test_scholarship_100 ... ok
TestExcellentStudent.test_scholarship_74 ... ok
TestExcellentStudent.test_scholarship_75 ... ok
TestExcellentStudent.test_scholarship_89 ... ok
TestExcellentStudent.test_scholarship_90 ... ok
TestGrantStudent.test_grant_after_adding_points ... ERROR
TestGrantStudent.test_grant_status_69 ... ERROR
TestGrantStudent.test_grant_status_70_boundary ... ERROR
TestGrantStudent.test_grant_status_71 ... ERROR
TestGrantStudent.test_inherited_add_points ... ok
TestGrantStudent.test_inherited_has_passed ... ok
TestGrantStudent.test_is_instance_of_student ... ok
TestPrintCost.test_eleven_pages_discount ... ok
TestPrintCost.test_negative_pages ... FAIL
TestPrintCost.test_nine_pages_no_discount ... ok
TestPrintCost.test_one_page ... ok
TestPrintCost.test_ten_pages_discount ... FAIL
TestPrintCost.test_zero_pages ... ok
TestStudent.test_add_negative_points ... FAIL
TestStudent.test_add_points_changes_score ... ok
TestStudent.test_add_ten_points ... ok
TestStudent.test_has_not_passed_49 ... ok
TestStudent.test_has_passed_on_boundary_50 ... FAIL
TestStudent.test_has_passed_returns_bool ... ok
TestStudent.test_max_score_100 ... FAIL
TestStudent.test_name ... ok
TestStudent.test_start_score ... ok

----------------------------------------------------------------------
Ran 35 tests in 0.005s

FAILED (failures=6, errors=4)
```

Итог: 35 тестов, 25 успешных, 6 упали (F), 4 с ошибкой (E).

Что показали упавшие тесты:

| Тест | Причина |
|---|---|
| `test_ten_pages_discount` | в коде `pages > 10`, а скидка должна быть от 10 включительно (получили 300, ждали 270) |
| `test_negative_pages` | функция вернула 0 вместо `ValueError` |
| `test_score_50_boundary` | в `exam_result` стоит `score > 50` вместо `>=` |
| `test_has_passed_on_boundary_50` | в `has_passed` стоит `>` вместо `>=` |
| `test_max_score_100` | `add_points` не ограничивает балл числом 100 |
| `test_add_negative_points` | `add_points` не выбрасывает `ValueError` |
| 4 теста `TestGrantStudent` (E) | у `GrantStudent` нет метода `grant_status()`, потому что вместо него стоит `pass` (`AttributeError`) |

## Что исправлено

- `print_cost`: `pages >= 10` и `ValueError` при отрицательном значении
- `exam_result`: `score >= 50`
- `Student.has_passed`: `self.score >= 50`
- `Student.add_points`: `ValueError` для отрицательных баллов и максимум 100
- `GrantStudent`: вместо `pass` добавлен метод `grant_status()` (грант сохраняется при 70 баллах и выше)

## Результат после исправления

```
Ran 35 tests in 0.002s

OK
```

Все 35 тестов проходят.

## Задание 5. Регрессионная проверка

| Показатель | Первый запуск | После исправления |
|---|---|---|
| Количество тестов | 35 | 35 |
| Успешные тесты | 25 | 35 |
| Ошибки F | 6 | 0 |
| Ошибки E | 4 | 0 |
| Итог OK или FAILED | FAILED (failures=6, errors=4) | OK |

## Описание одного дефекта

| Поле | Ответ студента |
|---|---|
| Название дефекта | Скидка не применяется при заказе ровно 10 страниц |
| Входные данные | `print_cost(10)` |
| Ожидаемый результат | 270 (10 × 30 × 0,9) |
| Фактический результат | 300 |
| Причина ошибки | в условии стоит `pages > 10` вместо `pages >= 10`, поэтому граница 10 не входит в скидку |
| Подтверждение исправления | после замены на `>=` тест `test_ten_pages_discount` проходит, и весь набор из 35 тестов выдаёт OK |

## Дополнительное задание

Класс `ExcellentStudent(Student)` с методом `scholarship()`: 30000 при 90-100 баллах, 15000 при 75-89, иначе 0. Проверены значения 74 (0), 75 (15000), 89 (15000), 90 (30000) и 100 (30000). Все тесты проходят.

## Вывод

При первом запуске из 35 тестов упало 10: 6 тестов с F и 4 с E. Ошибки были связаны с границами (`>` вместо `>=` в трёх местах), отсутствием проверок (`ValueError` и максимум 100) и потерянным методом `grant_status()` в `GrantStudent` из-за `pass`. После исправления кода все 35 тестов проходят, то есть исправление подтверждено повторным запуском всего набора, а не одного теста. Автоматические тесты удобнее ручной проверки, потому что все сценарии повторяются одной командой.

## Вопросы для защиты

1. **Почему имя метода начинается с `test_`?**
   `unittest` находит и запускает автоматически только методы, названия которых начинаются с `test_`. Метод с другим именем (например `check_result`) не будет запущен.
2. **Чем `assertEqual` отличается от `print()`?**
   `assertEqual` сам сравнивает результат с ожидаемым и сообщает, пройден тест или нет. `print()` только показывает значение, а проверять его должен человек.
3. **Зачем `setUp` создаёт объект перед каждым тестом?**
   Чтобы каждый тест получал новый объект и не зависел от изменений (например, от `add_points`) в других тестах. Результат не зависит от порядка запуска.
4. **Как проверить ожидаемое исключение?**
   Через `with self.assertRaises(ValueError):` и вызов функции внутри блока. Тест пройдёт, только если возникнет именно `ValueError`.
5. **Какие значения проверяют условие `score >= 50`?**
   Значение до границы (49), сама граница (50) и значение после неё (51).
6. **Почему после исправления запускают весь набор?**
   Исправление одной ошибки могло сломать другую часть программы, а полный запуск проверяет и найденную ошибку, и все остальные сценарии (регрессионная проверка).
