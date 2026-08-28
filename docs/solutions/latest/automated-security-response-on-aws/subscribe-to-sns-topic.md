---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/subscribe-to-sns-topic.html
---

# Subscribe to the SNS topic
<a name="subscribe-to-sns-topic"></a>

 **Remediation Updates**

 **Topic -** [SO0111-ASR\_Topic](https://us-east-1.console.aws.amazon.com/sns/v3/home?region=us-east-1#/topic/arn:aws:sns:us-east-1:111111111111:SO0111-ASR_Topic)

In the admin account, subscribe to the Amazon SNS topic created by the admin stack. This notifies you when remediations are initiated and when they succeed or fail.

 **Alarms**

 **Topic -** [SO0111-ASR\_Alarm\_Topic](https://us-east-1.console.aws.amazon.com/sns/v3/home?region=us-east-1#/topic/arn:aws:sns:us-east-1:111111111111:SO0111-ASR_Alarm_Topic)

In the admin account, subscribe to the Amazon SNS topic created by the admin stack. This will notify you when metric alarms initiate.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
