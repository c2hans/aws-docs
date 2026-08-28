---
source_url: https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-stop.html
---

# Stop rule set action
<a name="receiving-email-action-stop"></a>

The **Stop** action terminates the evaluation of the receipt rule set and, optionally, notifies you through Amazon SNS. This action has the following options.
+ **SNS Topic—**The name or ARN of the Amazon SNS topic to notify when the Stop action is performed. An example of an Amazon SNS topic ARN is *arn:aws:sns:us-east-1:123456789012:MyTopic*. You can also create an Amazon SNS topic when you set up your action by choosing **Create SNS Topic**. For more information about Amazon SNS topics, see the [Amazon Simple Notification Service Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html).
**Note**
The Amazon SNS topic you choose must be in the same AWS Region as the Amazon SES endpoint you use to receive email.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
