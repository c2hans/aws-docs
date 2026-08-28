---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/contact-flow-log-alerts.html
---

# Create alerts for events in your flow logs stored in an Amazon CloudWatch log group
<a name="contact-flow-log-alerts"></a>

You can configure CloudWatch to define a filter pattern that looks for specific events in your flow logs and then creates an alert when an entry for that event is added to the log.

For example, you can set an alert for when a flow block goes down an error path as a customer interacts with the flow. Log entries are typically available in CloudWatch within a short time, giving you near real-time notification of events in flows.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
