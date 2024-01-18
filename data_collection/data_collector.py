import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_mock_feedback_data(num_entries=100):
    """
    Generate mock data for customer feedback.
    :param num_entries: Number of feedback entries to generate
    :return: DataFrame with customer feedback data
    """
    feedback_examples = ['I love this product!', 'Not what I expected.', 'Absolutely fantastic!', 'Could be better.', 'I am not satisfied.']
    data = {'feedback': np.random.choice(feedback_examples, num_entries)}
    return pd.DataFrame(data)

def generate_mock_usage_data(num_users=50, num_days=30):
    """
    Generate mock data for usage metrics.
    :param num_users: Number of unique users
    :param num_days: Number of days to simulate
    :return: DataFrame with usage data
    """
    start_dates = [datetime.now() - timedelta(days=x) for x in range(num_days)]
    user_ids = np.arange(1, num_users + 1)
    session_starts = np.random.choice(start_dates, num_users)
    session_ends = [start + timedelta(minutes=np.random.randint(15, 120)) for start in session_starts]

    data = {'user_id': np.random.choice(user_ids, num_users), 'session_start': session_starts, 'session_end': session_ends}
    return pd.DataFrame(data)

def generate_mock_churn_data(num_users=100, start_date=datetime(2021, 1, 1)):
    """
    Generate mock data for churn analysis.
    :param num_users: Number of users
    :param start_date: Start date for the user base
    :return: DataFrame with churn data
    """
    signup_dates = [start_date + timedelta(days=np.random.randint(0, 365)) for _ in range(num_users)]
    last_activity_dates = [date + timedelta(days=np.random.randint(0, 365)) for date in signup_dates]

    data = {'user_id': np.arange(1, num_users + 1), 'signup_date': signup_dates, 'last_activity_date': last_activity_dates}
    return pd.DataFrame(data)

# Example usage
# feedback_data = generate_mock_feedback_data()
# usage_data = generate_mock_usage_data()
# churn_data = generate_mock_churn_data()
