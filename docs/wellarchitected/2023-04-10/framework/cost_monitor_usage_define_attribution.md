---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/cost_monitor_usage_define_attribution.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST03-BP03 Identify cost attribution categories
<a name="cost_monitor_usage_define_attribution"></a>

|  |
| --- |
| This best practice was updated with new guidance on July 13th, 2023. |

Identify organization categories such as business units, departments, or projects that could be used to allocate cost within your organization to the internal consuming entities so that spend accountability can be enforced and consumption behaviors can be driven effectively.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 The process of categorizing costs is crucial in budgeting, accounting, financial reporting, decision making, benchmarking, and project management. By classifying and categorizing expenses, teams can gain a better understanding of the types of costs they will incur throughout their cloud journey, helping teams make informed decisions and manage budgets effectively.

Cloud spend accountability establishes a strong incentive for disciplined demand and cost management. The result is significantly greater cloud cost savings for organizations that allocate most of their cloud spend to consuming business units or teams.

Work with your finance team and other relevant stakeholders to understand the requirements of how costs must be allocated within your organization. Workload costs must be allocated throughout the entire lifecycle, including development, testing, production, and decommissioning. Understand how the costs incurred for learning, staff development, and idea creation are attributed in the organization. This can be helpful to correctly allocate accounts used for this purpose to training and development budgets, instead of generic IT cost budgets.

 After defining your cost attribution categories with your stakeholders in your organization, use [AWS Cost Categories](https://aws.amazon.com/aws-cost-management/aws-cost-categories/) to group your cost and usage information into meaningful categories in the AWS Cloud such as cost for specific project or AWS accounts for departments or business units. You can create custom categories and map your cost and usage information into these categories based on rules you define using various dimensions such as account, tag, service, charge type, and even other cost categories. Once cost categories are set up, you will be able to view your cost and usage information by these categories allowing your organization to make better strategic and purchasing decisions. These categories will be visible in AWS Cost Explorer, AWS Budgets, and AWS Cost and Usage Report as well.

 As an example, the following diagram shows you how can you group your costs and usage information in your organization such as having multiple teams (cost category) having multiple environments (rules) and each environment having multiple resources or assets (dimensions).

![Flowchart detailing the relationship between cost and usage within an organization.](https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/images/cost-usage-organization-chart.png)

## Implementation steps
<a name="implementation-steps"></a>
+  **Define your organization categories:** Meet with stakeholders to define categories that reflect your organization's structure and requirements. These will directly map to the structure of existing financial categories, such as business unit, budget, cost center, or department. Look at the outcomes the cloud delivers for your business, such as training or education, as these are also organization categories. Multiple categories can be assigned to a resource, and a resource can be in multiple different categories, so define as many categories as needed.
+  **Define your functional categories:** Meet with stakeholders to define categories that reflect the functions that you have within your business. This may be the workload or application names, and the type of environment, such as production, testing, or development. Multiple categories can be assigned to a resource, and a resource can be in multiple different categories, so define as many categories as needed so that you can [manage your costs](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html) within the categorized structure using AWS Cost Categories.
+  **Define AWS Cost Categories:** You can [create cost categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/create-cost-categories.html) to organize your cost and usage information. Use [AWS Cost Categories](https://aws.amazon.com/aws-cost-management/aws-cost-categories/) to map your AWS costs and usage into meaningful categories. With cost categories, you can organize your costs using a rule-based engine. The rules that you configure organize your costs into categories. Within these rules, you can filter with using multiple dimensions for each category such as specific AWS accounts, specific AWS services, or specific charge types. You can then use these categories across multiple products in the [AWS Billing and Cost Management](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html) [console](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/view-billing-dashboard.html). This includes AWS Cost Explorer, AWS Budgets, AWS Cost and Usage Report, and AWS Cost Anomaly Detection. You can create groupings of costs using cost categories as well. After you create the cost categories (allowing up to 24 hours after creating a cost category for your usage records to be updated with values), they appear in [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/), [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html), [AWS Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html), and [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/). For example, create cost categories for your business units (DevOps Team), and under each category create multiple rules (rules for each sub category) with multiple dimensions (AWS accounts, cost allocation tags, services or charge type) based on your defined groupings. In AWS Cost Explorer and AWS Budgets, a cost category appears as an additional billing dimension. You can use this to filter for the specific cost category value, or group by the cost category.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
+ [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)
+  [Analyzing your costs with AWS Budgets](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html)
+  [Analyzing your costs with Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-explorer-what-is.html)
+  [Managing AWS Cost and Usage Reports](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-reports-costusage-managing.html)
+ [AWS Cost Categories](aws-cost-management/aws-cost-categories/)
+ [Managing your costs with AWS Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html)
+ [Creating cost categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/create-cost-categories.html)
+ [Tagging cost categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tag-cost-categories.html)
+ [Splitting charges within cost categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/splitcharge-cost-categories.html)
+ [AWS Cost Categories Features ](https://aws.amazon.com/aws-cost-management/aws-cost-categories/features/)

 **Related examples:**
+ [Organize your cost and usage data with AWS Cost Categories](https://aws.amazon.com/blogs/aws-cloud-financial-management/organize-your-cost-and-usage-data-with-aws-cost-categories/)
+ [Managing your costs with AWS Cost Categories](https://aws.amazon.com/aws-cost-management/resources/managing-your-costs-with-aws-cost-categories/)
