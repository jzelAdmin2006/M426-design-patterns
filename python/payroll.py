from payroll.employee import Employee
from payroll.third_party.banking import pay_out

if __name__ == "__main__":
    john_doe = Employee("John", "Doe", 120000)
    jayne_done = Employee("Jane", "Done", 125000)
    print(john_doe.get_full_name())
    print(jayne_done.get_full_name())

    john_doe.add_note("AccountDetails", "ABC-123")
    john_doe.add_note("Position", "Lead Engineer")
    jayne_done.add_note("AccountDetails", "XYZ-789")
    jayne_done.add_note("Position", "Head of HR")

    # FIXME: provide adapter for Employee
    pay_out(john_doe, john_doe.get_salary() / 12.0)
    pay_out(jayne_done, jayne_done.get_salary() / 12.0)
