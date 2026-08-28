---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-events-metrics.html
---

# AWS Cloud WAN events and metrics
<a name="cloudwan-events-metrics"></a>

AWS provides the following monitoring tools to watch the resources in your global network, report when something is wrong, and take automatic actions when appropriate.
+ *Amazon CloudWatch* monitors your AWS resources and the applications that you run on AWS in real time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take actions when a specified metric reaches a threshold that you specify. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).
+ *Amazon EventBridge* delivers a near-real-time stream of system events that describe changes in AWS resources. EventBridge enables automated event-driven computing, as you can write rules that watch for certain events and then trigger automated actions in other AWS services when these events happen. For more information, see the [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/).

You must first onboard CloudWatch Logs Insights before you can view Events on the AWS Cloud WAN dashboards. See [Onboard CloudWatch Logs Insights for AWS Cloud WAN](cloudwan-onboard-events.md) for the onboarding steps.

**Topics**
+ [CloudWatch metrics](cloudwan-metrics.md)
+ [Onboard CloudWatch Logs Insights](cloudwan-onboard-events.md)
+ [Monitor with Amazon CloudWatch Events](cloudwan-cloudwatch-events.md)
+ [Monitor Cloud WAN with CloudWatch metrics](cloudwan-cloudwatch-metrics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
