import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    rearranged_products = products.melt(id_vars='product_id',var_name='store', value_name='price').dropna()
    return rearranged_products