# Cohort-analysis-for-assessing-customer-retention-in-E-commerce-industry
This project aimed to understand customer purchasing behavior and retention trends for an e-commerce business using cohort analysis. Key steps included data preparation, cohort assignment, cohort index calculation, data aggregation, and visualization of trends to derive actionable insights.
Data Preparation: Loaded transactional data, converted date columns to datetime format, and ensured data was clean for analysis.
Cohort Assignment: Customers were grouped into cohorts based on their first purchase month and year using a custom get_cohort_date() function.
Cohort Index Calculation: Computed the number of months between a customer’s first purchase and subsequent purchases using the create_cohort_index() function to measure retention.
Data Aggregation and Visualization: Analyzed key metrics like sales and retention rates by cohort and visualized trends using line charts and heatmaps to identify patterns in customer behavior.
Insights and Recommendations: Derived insights on high-value customer segments, periods of low retention, and provided recommendations to enhance customer engagement, reduce churn, and improve marketing strategies.
The project utilized Python, Pandas, NumPy, Matplotlib, and Seaborn to perform the analysis and visualization, providing valuable insights for data-driven decision-making to boost customer loyalty and business growth.
