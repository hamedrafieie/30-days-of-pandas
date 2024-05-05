import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    filtered_countries = world[(world['population'] > 25000000) & (world['area'] > 300000)]
    filtered_countries = filtered_countries[['name', 'population', 'area']]
    return filtered_countries
