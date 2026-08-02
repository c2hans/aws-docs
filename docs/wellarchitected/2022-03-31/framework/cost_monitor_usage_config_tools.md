---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_monitor_usage_config_tools.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST03-BP04 Configure billing and cost management tools
<a name="cost_monitor_usage_config_tools"></a>

 Configure AWS Cost Explorer and AWS Budgets inline with your organization policies.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

To modify usage and adjust costs, each person in your organization must have access to their cost and usage information. It is recommended that all workloads and teams have the following tooling configured when they use the cloud:
+ **Reports:** Summarize of all cost and usage information
+ **Notifications:** Provide notifications when cost or usage is outside of defined limits.
+ **Current State: **Configure a dashboard showing current levels of cost and usage. The dashboard should be available in a highly visible place within the work environment (similar to an operations dashboard).
+ **Trending: **Provide the capability to show the variability in cost and usage over the required period of time, with the required granularity.
+ **Forecasts: **Provide the capability to show estimated future costs.
+ **Tracking: **Show the current cost and usage against configured goals or targets.
+ **Analysis: **Provide the capability for team members to perform custom and deep analysis down to the hourly granularity, with all possible dimensions.

You can use AWS native tooling, such as [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/), [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/), and [Amazon Athena](https://docs.aws.amazon.com/athena/?id=docs_gateway) with [Quick](https://docs.aws.amazon.com/quicksight/?id=docs_gateway) to provide this capability. You can also use third-party tooling — however, you must ensure that the costs of this tooling provide value to your organization.

**Implementation steps**
+ ** Create a Cost Optimization group: **Configure your account and create a group that has access to the required Cost and Usage reports. This group must include representatives from all teams that own or manage an application. This certifies that every team has access to their cost and usage information.
+ ** Configure AWS Budgets:** Configure AWS Budgets on all accounts for your workload. Set a budget for the overall account spend, and a budget for the workload by using tags.
+ ** Configure AWS Cost Explorer: **Configure AWS Cost Explorer for your workload and accounts. Create a dashboard for the workload that tracks overall spend, and key usage metrics for the workload.
+ ** Configure advanced tooling: **Optionally, you can create custom tooling for your organization that provides additional detail and granularity. You can implement advanced analysis capability using [Amazon Athena](https://docs.aws.amazon.com/athena/?id=docs_gateway), and dashboards using [Quick](https://docs.aws.amazon.com/quicksight/?id=docs_gateway).

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
+  [Analyzing your costs with AWS Budgets](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html)
+  [Analyzing your costs with Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-explorer-what-is.html)
+  [Managing AWS Cost and Usage Reports](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-reports-costusage-managing.html)

 **Related examples:**
+  [Well-Architected Labs - AWS Account Setup](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_1_AWS_Account_Setup/README.html/)
+  [Well-Architected Labs: Billing Visualization](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_5_Cost_Visualization/README.html)
+  [Well-Architected Labs: Cost and Governance Usage](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_2_Cost_and_Usage_Governance/README.html)
+  [Well-Architected Labs: Cost and Usage Analysis](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/200_4_Cost_and_Usage_Analysis/README.html)
+  [Well-Architected Labs: Cost and Usage Visualization](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/200_5_Cost_Visualization/README.html)
