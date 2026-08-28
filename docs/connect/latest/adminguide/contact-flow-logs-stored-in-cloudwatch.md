---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/contact-flow-logs-stored-in-cloudwatch.html
---

# Flow logs stored in an Amazon CloudWatch log group
<a name="contact-flow-logs-stored-in-cloudwatch"></a>

Flow logs are stored in an Amazon CloudWatch log group, in the same AWS Region as your Connect Customer instance. This log group is created automatically when [Enable flow logging](contact-flow-logs.md#enable-contact-flow-logs) is turned on for your instance.

For example, the following image shows the CloudWatch log groups for two test instances.

![The Amazon CloudWatch console, log groups, /aws/connect/mytest88 and mytest89.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cloudwatch-log-group.png)

 A log entry added as each block in your flow is triggered. You can configure CloudWatch to send alerts when unexpected events occur during active flows.

**What happens if my log group is deleted?** You need to manually re-create the CloudWatch log group. Otherwise, Connect Customer won't publish more logs.

## Pricing for flow logging
<a name="pricing-contact-flow-logs"></a>

You are not charged for generating flow logs, but you are charged for using CloudWatch for generating and storing the logs. Free tier customers are charged only for usage that exceeds service quotas. For details about Amazon CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
