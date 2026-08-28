---
source_url: https://docs.aws.amazon.com/MAP/latest/userguide/getting-started.html
---

# Getting started with AWS Migration Acceleration Program 2.0
<a name="getting-started"></a>

As you move your existing on-premises workloads to AWS, the migrated workloads are identified through a tagging mechanism. Tagging is required because it is used to report the migrated workloads’ spend and generate appropriate incentives. MAP cannot provide these incentives if you do not activate Cost Allocation Tags or tag the migrated resources.

The MAP migration tracking mechanism uses native AWS functionality that you configure in the following steps:

1. Tagging migrated workloads.

1. Selecting the appropriate MAP 2.0 tag value for your `map-migrated` key. To learn how to select the right tag value, see [Tagging key combinations](setting-up.md).

**Note**
The Migration Acceleration Program requires that you tag resources with the `map-migrated` tag. This tag is automatically activated for you as a cost allocation tag. Tags that are automatically activated don't count towards your cost allocation tag quota. For more information, see [Quotas and restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html).
Ensure that Cost Explorer is enabled. To learn how to enable Cost Explorer, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html).

**Topics**
+ [Prerequisites](getting-started-prerequisites.md)
+ [MPE ID length](mpe-length.md)
+ [Tagging Resources](getting-started-step2.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Acceleration Program. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query MAP` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
