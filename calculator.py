import re
import operator

def safe_calculator(func):
    def wrapper(expression):
        try:
            # перевірка на допустимі символи (тільки цифри, оператори і дужки.)
            if not re.match(r'^[\d+\-*/(). ]+$', expression):
                raise ValueError("Недопустимі символи у виразі")
            
            # виклик оригінальної функції.
            return func(expression)
        except ZeroDivisionError:
            return "Помилка: ділення на нуль"
        except SyntaxError:
            return "Помилка: неправильний синтаксис"
        except Exception as e:
            return f"Помилка: {str(e)}"
    return wrapper

@safe_calculator
def calculate(expression):
    return eval(expression)

# приклад використання.
print(calculate("10 + 5 * 2"))  # 20
print(calculate("10 / 0"))      # Помилка: ділення на нуль
print(calculate("10 + "))       # Помилка: неправильний синтаксис
print(calculate("10 + abc"))    # Помилка: недопустимі символи у виразі

