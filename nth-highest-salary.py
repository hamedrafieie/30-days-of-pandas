import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_salaries = employee['salary'].sort_values(ascending=False).unique()
    nth_highest_salary = sorted_salaries[N - 1] if N <= len(sorted_salaries) else None
    result_df = pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest_salary]})
    return result_df