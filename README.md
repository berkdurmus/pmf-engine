
# PMF Analysis Project

## Overview
This project is designed to analyze various metrics to assess a company's Product-Market Fit (PMF). It includes scripts for analyzing customer feedback, usage metrics, churn rate, and a main application script that orchestrates the entire PMF analysis process.

## Project Structure
- `data_collection/data_collector.py`: Contains functions to simulate the collection of mock data for customer feedback, usage metrics, and churn rate analysis.
- `analysis_modules/customer_feedback.py`: Module for analyzing customer feedback through sentiment analysis.
- `analysis_modules/usage_metrics.py`: Module for calculating usage metrics such as Daily Active Users (DAU), Monthly Active Users (MAU), and average session duration.
- `analysis_modules/churn_rate.py`: Module for calculating the churn rate based on user activity data.
- `main_application/main.py`: The main script that integrates all analysis modules and generates an overall PMF score.
- `requirements.txt`: Lists all Python dependencies necessary for the project.

## Installation
1. Clone or download the project to your local machine.
2. Install the required Python packages using the following command:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the `main_application/main.py` script to execute the analysis.
2. Modify the `data_collection/data_collector.py` to integrate with actual data sources.
3. Update analysis logic in the `analysis_modules/` based on specific business requirements and data structure.

## Customization
- The project is structured for basic PMF analysis and can be extended or modified for more complex scenarios.
- The data collection scripts are set up to generate mock data. Replace these with actual data fetching logic as per your data sources.

## Note
- This project is a template and requires customization and real data for practical use.
- Ensure compliance with data privacy laws and company policies when handling real user data.
