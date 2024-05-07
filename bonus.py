import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary']
    employees.loc[employees['name'].str.startswith('M'),'bonus'] = 0
    employees.loc[employees['employee_id'] % 2 == 0, 'bonus'] = 0
    columns_to_keep = ['employee_id','bonus']
    employees = employees[columns_to_keep]
    result = employees.sort_values('employee_id')
    return result