---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/fleet-monitor.html
---

# Monitor your EC2 Fleet or Spot Fleet
<a name="fleet-monitor"></a>

Effective monitoring of your EC2 Fleet or Spot Fleet is essential for maintaining optimal performance and ensuring reliability. There are various tools to help you achieve this, including Amazon CloudWatch and Amazon EventBridge, which are covered in this topic.

With CloudWatch, you can collect and track metrics, set alarms, and automatically react to changes in your fleet’s status.

With EventBridge, you can monitor and respond programmatically to events emitted by your fleet. By defining rules in EventBridge, you can automate responses to specific fleet events, such as instance termination or fleet state changes, improving your operational efficiency.

**Topics**
+ [Monitor your EC2 Fleet or Spot Fleet using CloudWatch](ec2-fleet-cloudwatch-metrics.md)
+ [Monitor and programmatically respond to the events emitted by your EC2 Fleet or Spot Fleet using Amazon EventBridge](monitor-ec2-fleet-using-eventbridge.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
