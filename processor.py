import pandas as pd

def process_cutoff_data(df):

    # Ensure correct datatype
    df['year'] = df['year'].astype(int)

    # Get last 3 years
    latest_years = sorted(df['year'].unique(), reverse=True)[:3]
    df = df[df['year'].isin(latest_years)]

    # Group data
    grouped = df.groupby(
        ['college_name', 'branch', 'category']
    )

    result = {}

    for category in df['category'].unique():
        category_df = df[df['category'] == category]

        pivot = category_df.pivot_table(
            index=['college_name', 'branch'],
            columns='year',
            values='cutoff_rank'
        ).reset_index()

        result[category] = pivot

    return result
