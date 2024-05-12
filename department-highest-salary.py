import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(employee, department, left_on='departmentId', right_on='id')
    max_salary_by_department = merged_df.groupby('name_y')['salary'].max()
    result = merged_df[merged_df.apply(lambda row: row['salary'] == max_salary_by_department[row['name_y']], axis=1)].reset_index(drop=True)
    result = result[['name_y', 'name_x', 'salary']]
    result.columns=['Department', 'Employee', 'Salary']   
    return result