---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/forecast-demand-freight-capacity/best-practices.html
---

# Best practices for an ML model that forecasts freight demand
<a name="best-practices"></a>

By following these best practices, you can enhance the accuracy, reliability, and interpretability of your machine learning model for forecasting freight demand, ultimately leading to better decision-making and operational efficiency:
+ **Data quality and preprocessing** – Make sure that the data used for training the model is of high quality and free from errors, missing values, and inconsistencies. Data preprocessing steps, such as handling missing values, outlier detection, and feature engineering, play a crucial role in improving the model's accuracy.
+ **Sufficient historical data** – Having sufficient historical data is essential for capturing patterns, trends, and seasonality. However, it's also important to consider the relevance and timeliness of the historical data. If there have been significant changes in the market, business operations, or external factors, older data may not be representative of the current scenario. In this situation, give higher weightage to the more recent data.
+ **Feature selection and engineering** – Identifying relevant features and engineering new features from existing data can significantly improve the model's performance. Collaborate closely with domain experts to use their knowledge and insights when selecting appropriate features. Additionally, consider performing feature importance analysis to identify the most influential features and potentially remove redundant or irrelevant features.
+ **Ensemble models** – Instead of relying on a single model, consider using ensemble techniques that combine the predictions of multiple models. Ensemble models can outperform individual models and provide more robust and accurate forecasts.
+ **Model evaluation and validation** – Regularly evaluate and validate the model's performance by using appropriate metrics, such as mean squared error (MSE), mean absolute percentage error (MAPE), or any other domain-specific metrics. Use cross-validation or holdout validation to assess the model's generalization capabilities.
+ **Continuous monitoring and retraining** – Freight demand patterns can change over time due to various factors, such as economic conditions, market dynamics, or changes in business operations. Continuously monitor the model's performance and retrain it periodically with the latest data to improve its accuracy and relevance.
+ **Explainable AI** – Demand forecasting models should be interpretable and explainable, especially in cases where stakeholders need to understand the reasoning behind the forecasts. Techniques such as feature importance analysis, partial dependence plots, Shapley Additive explanations (SHAP) can help explain the model's decisions.
+ **Incorporate domain knowledge** – Collaborate closely with domain experts and business stakeholders to incorporate their knowledge and insights into the modeling process. Their domain expertise can help identify potential biases, interpret results, and make informed decisions based on the forecasts.
+ **Scenario analysis and what-if simulations** – Incorporate the ability to perform scenario analysis and what-if simulations into the forecasting solution. This allows stakeholders to explore the effect of different business decisions or external factors on the demand forecast, enabling more informed decision-making.
+ **Automated and scalable pipeline** – Build an automated and scalable pipeline for data ingestion, preprocessing, model training, and deployment. This consistently and efficiently executes the forecasting process, especially when dealing with multiple products or regions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
