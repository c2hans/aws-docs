---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_cloud_financial_management_budget_forecast.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST01-BP03 Establish cloud budgets and forecasts
<a name="cost_cloud_financial_management_budget_forecast"></a>

Adjust existing organizational budgeting and forecasting processes to be compatible with the highly variable nature of cloud costs and usage. Processes must be dynamic using trend-based or business driver-based algorithms, or a combination of both.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Customers use the cloud for efficiency, speed and agility, which creates a highly variable amount of cost and usage. Costs can decrease with increases in workload efficiency, or as new workloads and features are deployed. It is possible to see the cost increase when the workload efficiency increases, or as new workloads and features are deployed. Or, workloads will scale to serve more of your customers, which increases cloud usage and costs. Resources are now more readily accessible than ever before. With the elasticity of the cloud also brings an elasticity of costs and forecasts. Existing organizational budgeting processes must be modified to incorporate this variability.

Adjust existing budgeting and forecasting processes to become more dynamic using either a trend-based algorithm (using historical costs as inputs), or using business-driver-based algorithms (for example, new product launches or regional expansion), or a combination of both trend and business drivers.

Use [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) to set custom budgets at a granular level by specifying the time period, recurrence, or amount (fixed or variable), and adding filters such as service, AWS Region, and tags. To stay informed on the performance of your existing budgets you can create and schedule [AWS Budgets Reports](https://docs.aws.amazon.com/cost-management/latest/userguide/reporting-cost-budget.html) to be emailed to you and your stakeholders on a regular cadence. You can also create [AWS Budgets Alerts](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-best-practices.html) based on actual costs, which is reactive in nature, or on forecasted costs, which provides time to implement mitigations against potential cost overruns. You will be alerted when your cost or usage exceeds, or if they are forecasted to exceed, your budgeted amount.

AWS gives you the flexibility to build dynamic forecasting and budgeting processes so you can stay informed on whether costs adhere to, or exceed, budgetary limits.

Use [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-forecast.html) to forecast costs in a defined future time range based on your past spend. AWS Cost Explorer’s forecasting engine segments your historical data based on charge types (for example, Reserved Instances) and uses a combination of machine learning and rule-based models to predict spend across all charge types individually. Use [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-forecast.html) to forecast daily (up to three months) or monthly (up to 12 months) cloud costs based on machine learning algorithms applied to your historical costs (trend-based).

Once you’ve determined your trend-based forecast using Cost Explorer, use the [AWS Pricing Calculator](https://calculator.aws/#/) to estimate your AWS use case and future costs based on the expected usage (traffic, requests-per-second, required Amazon Elastic Compute Cloud (Amazon EC2) instance, and so forth). You can also use it to help you plan how you spend, find cost saving opportunities, and make informed decisions when using AWS.

Use [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) to prevent or reduce cost surprises and enhance control without slowing innovation. AWS Cost Anomaly Detection leverages advanced machine learning technologies to identify anomalous spend and root causes, so you can quickly take action. [With three simple steps](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/), you can create your own contextualized monitor and receive alerts when any anomalous spend is detected. Let builders build, and let AWS Cost Anomaly Detection monitor your spend and reduce the risk of billing surprises.

As mentioned in the [Well-Architected Cost Optimization Pillar’s Finance and Technology Partnership](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/finance-and-technology-partnership.html) section, it is important to have partnership and cadences between IT, Finance and other stakeholders to ensure that they are all using the same tooling or processes for consistency. In cases where budgets may need to change, increasing cadence touch points can help react to those changes more quickly.

**Implementation steps**
+  **Update existing budget and forecasting processes: **Implement trend-based, business driver-based, or a combination of both in your budgeting and forecasting processes.
+ **Configure alerts and notifications:** Use AWS Budgets Alerts and Cost Anomaly Detection.
+ **Perform regular reviews with key stakeholders:** For example, stakeholders in IT, Finance, Platform, and other areas of the business, to align with changes in business direction and usage.

## Resources
<a name="resources"></a>

 **Related documents:**
+ [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-forecast.html)
+ [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/)
+ [AWS Pricing Calculator](https://calculator.aws/#/)
+ [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/)
+ [AWS License Manager](https://aws.amazon.com/license-manager/)

 **Related examples:**
+  [Launch: Usage-Based Forecasting now Available in AWS Cost Explorer](https://aws.amazon.com/blogs/aws-cloud-financial-management/launch-usage-based-forecasting-now-available-in-aws-cost-explorer/)
+  [AWS Well-Architected Labs - Cost and Usage Governance](https://wellarchitectedlabs.com/cost/100_labs/100_2_cost_and_usage_governance/)
