import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    filtered = views[(views['author_id'] == views['viewer_id'])]
    result = filtered['author_id'].unique()

    # Create a DataFrame with the result
    result_df = pd.DataFrame({'id': result})

    # Sort by id in ascending order
    result_df.sort_values(by='id', inplace=True)
    return result_df