class SalaryNotFound(Exception):
    """Exception Raised"""

    def __init__(self,salary,message='salary not in range'):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

salary = int(input("Enter Salary amount"))
if not 5000 < salary < 15000:
    raise SalaryNotFound(salary)

