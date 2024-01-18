import pandas as pd
from datetime import datetime, timedelta

def analyze_churn(data, period='30D'):
    """
    Calculate churn rate for a given period.

    :param data: DataFrame with columns 'user_id', 'signup_date', 'last_activity_date'
    :param period: Time period for calculating churn (default is '30D' for 30 days)
    :return: Churn rate as a float
    """
    # Ensure dates are in datetime format
    data['signup_date'] = pd.to_datetime(data['signup_date'])
    data['last_activity_date'] = pd.to_datetime(data['last_activity_date'])

    # Define the end date for the period to analyze
    end_date = datetime.now()
    start_date = end_date - pd.to_timedelta(period)

    # Filter users who signed up before the start date
    active_users = data[data['signup_date'] < start_date]

    # Determine users who have churned
    churned_users = active_users[active_users['last_activity_date'] < start_date]

    # Calculate churn rate
    churn_rate = len(churned_users) / len(active_users) if len(active_users) > 0 else 0
    return churn_rate

# Example usage
# data = pd.DataFrame({'user_id': [...], 'signup_date': [...], 'last_activity_date': [...]})
# churn_rate = analyze_churn(data)
# print("Churn Rate:", churn_rate)
