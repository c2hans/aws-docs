---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-directory-service-for-microsoft-ad-well-architected-analysis/cost-optimization-pillar.html
---

# Cost optimization pillar
<a name="cost-optimization-pillar"></a>

The cost optimization pillar focuses on avoiding unnecessary costs. The following recommendations can help you meet the** **cost optimization design principles and architectural best practices for AWS Managed Microsoft AD.

**Key focus areas**
+ Understanding spending over time and controlling fund allocation
+ Selecting resources of the right type and quantity
+ Scaling to meet business needs without overspending

## Implement cloud financial management
<a name="implement-cloud-financial-management"></a>
+ Forecast AWS Managed Microsoft AD costs by using [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html).
+ Plan and set expectations around AWS Managed Microsoft AD costs by using [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).
+ Keep up to date with new service releases that can be used to optimize AWS Managed Microsoft AD costs.
+ Consider combining billing for AWS Managed Microsoft AD through a unified tagging strategy.

## Adopt a consumption cost model
<a name="adopt-a-consumption-cost-model"></a>
+ Evaluate your AWS Managed Microsoft AD edition. Choose the edition that meets your needs for the lowest price.

## Pay only for what you use
<a name="pay-only-for-what-you-use"></a>
+ Automate AWS Managed Microsoft AD scaling based on utilization metrics to reduce the number of domain controllers when utilization is low. For more information, see [How to automate AWS Managed Microsoft AD scaling based on utilization metrics](https://aws.amazon.com/blogs/security/how-to-automate-aws-managed-microsoft-ad-scaling-based-on-utilization-metrics/) on the AWS Blog.
+ Set the retention period for Amazon CloudWatch log groups that store AWS Managed Microsoft AD logs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
