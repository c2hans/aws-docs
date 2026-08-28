---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-resource-inventory.html
---

# Resource inventory for Accelerate
<a name="acc-resource-inventory"></a>

All the resources that AMS Accelerate deploys to your AWS account or accounts are listed in the [`resource_inventory.zip`](samples/resource_inventory.zip) file (Excel spreadsheet).

**Note**
 In the *Resource Name* column, the prefix *CFN:* indicates a CloudFormation logical ID instead of a resource name. These are shown for unnamed resources, for example, for S3 bucket policies.

AMS deploys a set of services as described in the [Service description](acc-sd.md). The cost of deploying them is low when deployed to an empty account, but the cost increases as utilization grows. For example, logs are created and config rules are invoked as resources change.

When multiple changes are made to the config rules, multiple config compliance invocation can be triggered, leading to higher costs. The same possibility applies for Amazon CloudWatch used for monitoring instances—the more granular your monitoring, the higher the cost of the service. AWS Backup is another example. If you have multiple backups stored, or if you have higher retention periods, you are using more storage and the cost is higher.

These numbers are hard to predict. During your monthly business review with your cloud service delivery manager (CSDM), keep track of the changes and work to identify areas of opportunity for cost reduction.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
