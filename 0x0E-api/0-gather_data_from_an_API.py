# 0-gather_data_from_an_API

if __name__ == "__main__":
    import sys
    import requests

    def get_employee_todo():
        """Gets info from JSON Placeholder API, generates fake data for
        Employee Name, Employee To Do, Employee Completed To Do
        Based on input of an Employee ID as an integer"""
        employee_id = sys.arg[1]
        completed = 0
        source = "https://jsonplaceholder.typicode.com/"

        employee_name = (requests.get(f'{source}users/{employee_id}')).json()
        employee_to_do = (requests.get(f'{source}'
                                       f'todos?userID={employee_id}')).json()

        # testing above code so far

        print(f'Employee Name Result: {employee_name}')
        print(f'Employee_to_to Result: {employee_to_do}')
