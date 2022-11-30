#!/usr/bin/python3
"""Gets info about employee from an API"""


def get_employee_todo():
        """Gets info from JSON Placeholder API, generates fake data for
        Employee Name, Employee To Do, Employee Completed To Do
        Based on input of an Employee ID as an integer"""
        employee_id = sys.argv[1]
        num_completed = 0
        source = "https://jsonplaceholder.typicode.com/"

        employee_name = (requests.get(f'{source}users/{employee_id}')).json()

        # testing above code so far

        # print(f'Employee Name Result: {employee_name}')
        # print(f'Employee_to_to Result: {employee_to_do}')

        completed_list = []

        for task in employee_to_do:
            if task.get("completed") is True:
                num_completed += 1
                completed_list.append(task.get("title"))

        # print(num_completed)
        # print(len(employee_to_do))

        name = employee_name.get("name")
        print(f'Employee {name} is done with'
              f'tasks({num_completed}/{len(employee_to_do)}):')
        for task in completed_list:
            print(f'\t {task}')

if __name__ == "__main__":
    get_employee_todo()