---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/monitoring.html
---

# Monitoring
<a name="monitoring"></a>

You can use other AWS services to monitor AWS Config resources.
+ You can use Amazon Simple Notification Service (SNS) to send you notifications every time a supported AWS resource is created, updated, or otherwise modified as a result of user API activity.
+ You can use Amazon EventBridge to detect and react to changes in the status of AWS Config events.

**Topics**
+ [Using Amazon SQS](monitor-resource-changes.md)
+ [Using Amazon EventBridge](monitor-config-with-cloudwatchevents.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
