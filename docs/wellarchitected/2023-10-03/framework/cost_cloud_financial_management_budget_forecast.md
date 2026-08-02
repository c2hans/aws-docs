---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/cost_cloud_financial_management_budget_forecast.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST01-BP03 Establish cloud budgets and forecasts
<a name="cost_cloud_financial_management_budget_forecast"></a>

 Adjust existing organizational budgeting and forecasting processes to be compatible with the highly variable nature of cloud costs and usage. Processes must be dynamic, using trend-based or business driver-based algorithms or a combination of both.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Customers use the cloud for efficiency, speed, and agility, which creates a highly variable amount of cost and usage. Costs can decrease (or sometimes increase) with increases in workload efficiency or as new workloads and features are deployed. Workloads can scale to serve more of your customers, which increases cloud usage and costs. Resources are now more readily accessible than ever before. The elasticity of the cloud also brings an elasticity of costs and forecasts. Existing organizational budgeting processes must be modified to incorporate this variability.

 The budget is usually prepared for a single year and remains fixed, requiring strict adherence from everyone involved. In contrast, forecasting is more flexible, allowing for readjustments throughout the year and providing dynamic projections over a period of one, two, or three years. Both budgeting and forecasting play a crucial role in establishing financial expectations among various technology and business stakeholders. Accurate forecasting and implementation also bring accountability for stakeholders who are directly responsible for provisioning cost in the first place, and it can also raise their overall cost awareness.

 Adjust existing budgeting and forecasting processes to become more dynamic using either a trend-based algorithm (using historical costs as inputs) or driver-based algorithms (for example, new product launches, Regional expansion, or new environments for workloads), which is ideal for a dynamic and variable spending environment, or a combination of both trend and business drivers.

 You can use [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-forecast.html) for trend-based forecasting in a defined future time range based on your past spend. AWS Cost Explorer's forecasting engine segments your historical data based on charge types (for example, Reserved Instances) and uses a combination of machine learning and rule-based models to predict spend across all charge types individually.

 Identify the business drivers which may impact your usage cost and forecast for each of them separately to ensure expected usage is calculated in advance. Some of the drivers are linked to IT and product teams within the organization. Other business drivers, such as marketing events, promotions, mergers, and acquisitions, are known by your sales, marketing, and business leaders, and it's important to collaborate and account for all those demand drivers as well. You need to work with them closely to understand the impact on new internal drivers.

 Once you've determined your trend-based forecast using Cost Explorer or any other tools, use the [AWS Pricing Calculator](https://calculator.aws/#/) to estimate your AWS use case and future costs based on the expected usage (traffic, requests-per-second, or required Amazon EC2 instance). You can also use it to help you plan how you spend, find cost saving opportunities, and make informed decisions when using AWS. It is important to track the accuracy of that forecast as budgets should be set based on these forecast calculations and estimations.

 Use [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) to set custom budgets at a granular level by specifying the time period, recurrence, or amount (fixed or variable), and adding filters such as service, AWS Region, and tags. To stay informed on the performance of your existing budgets, you can create and schedule [AWS Budgets Reports](https://docs.aws.amazon.com/cost-management/latest/userguide/reporting-cost-budget.html) to be emailed to you and your stakeholders on a regular cadence. You can also create [AWS Budgets Alerts](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-best-practices.html) based on actual costs, which is reactive in nature, or on forecasted costs, which provides time to implement mitigations against potential cost overruns. You can be alerted when your cost or usage exceeds, or if they are forecasted to exceed, your budgeted amount.

 Use [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) to prevent or reduce cost surprises and enhance control without slowing innovation. AWS Cost Anomaly Detection leverages machine learning to identify anomalous spend and root causes, so you can quickly take action. [With three simple steps](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/), you can create your own contextualized monitor and receive alerts when any anomalous spend is detected.

 As mentioned in the Well-Architected cost optimization pillar's [Finance and Technology Partnership section](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/finance-and-technology-partnership.html), it is important to have partnership and cadences between IT, finance, and other stakeholders to verify that they are all using the same tools or processes for consistency. In cases where budgets may need to change, increasing cadence touch points can help react to those changes more quickly.

### Implementation steps
<a name="implementation-steps"></a>
+  **Analyze trend-based forecasting:** Use preferred trend-based forecasting tools such as AWS Cost Explorer and Amazon Forecast. Analyze your usage cost on the different dimensions like service, account, tags and cost categories. If advanced forecasting is required, import your AWS Cost and Usage Report data into Amazon Forecast (which applies linear regression as a form of machine learning to forecast).
+  **Analyze driver-based forecasting:** Identify the impact of business drivers on your cloud usage and forecast for each of them separately to calculate expected usage cost in advance. Work closely with business unit owners and stakeholders to understand the impact on new drivers and calculate expected cost changes to define accurate budgets.
+  **Update existing forecasting and budget processes:** Define your forecasting budgeting processes based on adopted forecasting methods such as trend-based, business driver-based, or a combination of both forecasting methods. Budgets should be calculated and realistic, based on these forecasting processes.
+  **Configure alerts and notifications:** Use AWS Budgets Alerts and AWS Cost Anomaly Detection to get alerts and notifications.
+  **Perform regular reviews with key stakeholders: **For example, stakeholders in IT, finance, platform teams, and other areas of the business, should align with changes in business direction and usage.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/?sc_channel=cfm-blog&sc_campaign=using-the-right-tools-for-your-cloud-cost-forecasting&sc_medium=plan-and-evaluate&sc_content=cfm-blog&sc_detail=link&sc_outcome=aw&sc_publisher=cfm-awareness&trk=using-the-right-tools-for-your-cloud-cost-forecasting_cfm-blog_link)
+  [AWS Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html)
+  [Quick Forecasting](https://docs.aws.amazon.com/quicksight/latest/user/forecasts-and-whatifs.html)
+  [Amazon Forecast](https://aws.amazon.com/forecast/)
+  [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/)
+  [AWS News Blog](https://aws.amazon.com/blogs/aws/)

 **Related videos:**
+  [How can I use AWS Budgets to track my spending and usage](https://www.youtube.com/watch?v=Ris23gKc7s0)
+  [AWS Cost Optimization Series: AWS Budgets](https://www.youtube.com/watch?v=5vYEVQzoMeM)

 **Related examples:**
+  [Understand and build driver-based forecasting](https://aws.amazon.com/blogs/aws-cloud-financial-management/understand-and-build-driver-based-forecasting/)
+  [How to establish and drive a forecasting culture](https://aws.amazon.com/blogs/aws-cloud-financial-management/how-to-establish-and-drive-a-forecasting-culture/)
+  [How to improve your cloud cost forecasting](https://aws.amazon.com/blogs/aws-cloud-financial-management/forecasting-blog-series-1-3-ways-to-more-effectively-forecast-cloud-spend/)
+  [Using the right tools for your cloud cost forecasting](https://aws.amazon.com/blogs/aws-cloud-financial-management/using-the-right-tools-for-your-cloud-cost-forecasting/)
