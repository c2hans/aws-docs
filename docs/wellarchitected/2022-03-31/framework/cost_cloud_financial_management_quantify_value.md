---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_cloud_financial_management_quantify_value.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST01-BP09 Quantify business value from cost optimization
<a name="cost_cloud_financial_management_quantify_value"></a>

 Quantifying business value from cost optimization allows you to understand the entire set of benefits to your organization. Because cost optimization is a necessary investment, quantifying business value allows you to explain the return on investment to stakeholders. Quantifying business value can help you gain more buy-in from stakeholders on future cost optimization investments, and provides a framework to measure the outcomes for your organization’s cost optimization activities.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

In addition to reporting savings from cost optimization, it is recommended that you quantify the additional value delivered. Cost optimization benefits are typically quantified in terms of lower costs per business outcome. For example, you can quantify On-Demand Amazon Elastic Compute Cloud(Amazon EC2) cost savings when you purchase Savings Plans, which reduce cost and maintain workload output levels. You can quantify cost reductions in AWS spending when idle Amazon EC2 instances are terminated, or unattached Amazon Elastic Block Store (Amazon EBS) volumes are deleted.

The benefits from cost optimization, however, go above and beyond cost reduction or avoidance. Consider capturing additional data to measure efficiency improvements and business value.

**Implementation steps**
+ **Executing cost optimization best practices: **For example, resource lifecycle management reduces infrastructure and operational costs and creates time and unexpected budget for experimentation. This increases organization agility and uncovers new opportunities for revenue generation.
+ **Implementing automation: **For example, Auto Scaling, which ensures elasticity at minimal effort, and increases staff productivity by eliminating manual capacity planning work. For more details on operational resiliency, refer to the [Well-Architected Reliability Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).
+ **Forecasting future AWS costs: **Forecasting enables finance stakeholders to set expectations with other internal and external organization stakeholders, and helps improve your organization’s financial predictability. AWS Cost Explorer can be used to perform forecasting for your cost and usage.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Blog](https://aws.amazon.com/blogs/)
+  [AWS Cost Management](https://aws.amazon.com/blogs/aws-cost-management/)
+  [AWS News Blog](https://aws.amazon.com/blogs/aws/)
+  [Well-Architected Reliability Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
