---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/smart-crop-monitor.html
---

# Monitoring smart crop activity
<a name="smart-crop-monitor"></a>

You can monitor smart crop activity using these AWS services:
+ Metrics that Amazon CloudWatch produces, using data sent by Elemental Inference. See [ Monitoring AWS Elemental Inference with Amazon CloudWatch ](https://docs.aws.amazon.com/elemental-inference/latest/userguide/monitoring-cloudwatch) in the *AWS Elemental Inference user guide*.
+ Events that Elemental Inference produces. You can use Amazon EventBridge to work with these events. See [ Monitoring AWS Elemental Inference events with Amazon EventBridge ](https://docs.aws.amazon.com/elemental-inference/latest/userguide/monitoring-events) in the *AWS Elemental Inference user guide*.
+ Actions that Amazon EventBridge takes and that are collected by AWS CloudTrail. See [ Monitoring Elemental Inference API calls with AWS CloudTrail](https://docs.aws.amazon.com/elemental-inference/latest/userguide/logging-using-cloudtrail) in the *AWS Elemental Inference user guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
