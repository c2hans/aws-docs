---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_monitor_usage_define_attribution.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST03-BP02 Identify cost attribution categories
<a name="cost_monitor_usage_define_attribution"></a>

 Identify organization categories that could be used to allocate cost within your organization.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Work with your finance team and other relevant stakeholders to understand the requirements of how costs must be allocated within your organization. Workload costs must be allocated throughout the entire lifecycle, including development, testing, production, and decommissioning. Understand how the costs incurred for learning, staff development, and idea creation are attributed in the organization. This can be helpful to correctly allocate accounts used for this purpose to training and development budgets, instead of generic IT cost budgets.

**Implementation steps**
+  **Define your organization categories:** Meet with stakeholders to define categories that reflect your organization's structure and requirements. These will directly map to the structure of existing financial categories, such as business unit, budget, cost center, or department. Look at the outcomes the cloud delivers for your business, such as training or education, as these are also organization categories. Multiple categories can be assigned to a resource, and a resource can be in multiple different categories, so define as many categories as needed.
+  **Define your functional categories:** Meet with stakeholders to define categories that reflect the functions that you have within your business. This may be the workload or application names, and the type of environment, such as production, testing, or development. Multiple categories can be assigned to a resource, and a resource can be in multiple different categories, so define as many categories as needed.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
+  [Analyzing your costs with AWS Budgets](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html)
+  [Analyzing your costs with Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-explorer-what-is.html)
+  [Managing AWS Cost and Usage Reports](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-reports-costusage-managing.html)
