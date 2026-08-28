---
source_url: https://docs.aws.amazon.com/cost-management/latest/userguide/ce-granular-data.html
---

# Granular data
<a name="ce-granular-data"></a>

Cost Explorer provides hourly and resource-level granularity through three features:
+ Resource-level data at daily granularity
+ Cost and usage data for all AWS services at hourly granularity (without resource-level data)
+ EC2-Instances (Elastic Compute Cloud) resource-level data at hourly granularity

Enable one or all of these features based on how you plan on using granular data for your in-depth cost and usage analysis.

To enable granular data in Cost Explorer, see [Configuring multi-year and granular data](ce-configuring-data.md).

**Note**
Granular data visibility is only available for billing views that show chargeable data. When you use Billing Conductor as an account in a standard billing group or billing transfer billing group, you can't view granular data in Cost Explorer.

**Topics**
+ [Resource-level data at daily granularity](ce-resource-daily.md)
+ [Cost and usage data for all AWS services at hourly granularity (without resource-level data)](ce-services-hourly.md)
+ [EC2-Instances (Elastic Compute Cloud) resource-level data at hourly granularity](ce-ec2-hourly.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
