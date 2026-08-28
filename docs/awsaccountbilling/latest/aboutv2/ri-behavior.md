---
source_url: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-behavior.html
---

# Reserved Instances
<a name="ri-behavior"></a>

For billing purposes, the consolidated billing feature of AWS Organizations treats all the accounts in the organization as one account. This means that all accounts in the organization can receive the hourly cost benefit of Reserved Instances that are purchased by any other account.

You can turn off Reserved Instance discount sharing on the **Preferences** page on the Billing and Cost Management console. For more information, see [Reserved Instances and Savings Plans discount sharing](ri-turn-off.md).

**Note**
When you use billing transfer, Reserved Instances and Savings Plans apply only to the AWS Organizations where they're purchased, regardless of which account pays the bill. You can't purchase or share Reserved Instances and Savings Plans across multiple AWS Organizations.

**Topics**
+ [Billing examples for specific services](consolidatedbilling-other.md)
+ [Reserved Instances and Savings Plans discount sharing](ri-turn-off.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awsaccountbilling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
