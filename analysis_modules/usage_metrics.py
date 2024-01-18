import pandas as pd

def analyze_usage(data):
    """
    Analyze usage metrics such as DAU, MAU, and average session duration.

    :param data: DataFrame with 'user_id', 'session_start', 'session_end' columns
    :return: A dictionary with DAU, MAU, and average session duration
    """
    # Convert session start/end times to datetime
    data['session_start'] = pd.to_datetime(data['session_start'])
    data['session_end'] = pd.to_datetime(data['session_end'])

    # Calculate session duration
    data['session_duration'] = (data['session_end'] - data['session_start']).dt.total_seconds()

    # Daily Active Users (DAU)
    dau = data['session_start'].dt.date.nunique()

    # Monthly Active Users (MAU)
    mau = data['session_start'].dt.to_period('M').nunique()

    # Average Session Duration
    avg_session_duration = data['session_duration'].mean()

    return {
        'DAU': dau,
        'MAU': mau,
        'Average Session Duration': avg_session_duration
    }

# Example usage
# data = pd.DataFrame({'user_id': [...], 'session_start': [...], 'session_end': [...]})
# usage_metrics = analyze_usage(data)
# print("Usage Metrics:", usage_metrics)
