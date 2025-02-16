import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == "__main__":
    urrent_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Вызов функции для получения списка сотрудников
    employees = get_employees()
    
    # Для каждого сотрудника вызываем функцию расчета з/п
    for employee in employees:
        print(f"Рассчитываем зарплату для сотрудника: {employee}")
        calculate_salary(employee)