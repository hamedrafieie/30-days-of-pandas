import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    def is_valid_email(email):
        if not email.endswith('@leetcode.com'):
            return False

        prefix = email[:-len('@leetcode.com')]

        if not prefix:
            return False

        first_char = prefix[0]
        if not first_char.isalpha():
            return False

        valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.-")
        return all(char in valid_chars for char in prefix)

    # Use the function to filter the DataFrame
    valid_users = users[users['mail'].apply(is_valid_email)]
    return valid_users