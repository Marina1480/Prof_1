import application.db.people, application.salary


if __name__ == '__main__':
    application.salary.calculate_salary()

    application.db.people.get_employees()

from datetime import datetime, date, time
print(datetime.today())
