---
source_url: https://docs.aws.amazon.com/chatbot/latest/adminguide/monitoring-investigations.html
---

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Monitoring investigations with Amazon Q Developer in chat applications
<a name="monitoring-investigations"></a>

You can use Amazon Q Developer operational investigations in your Microsoft Teams and Slack chat channels to investigate and identify the cause of application issues when they occur. An Amazon Q operational investigation traverses and analyzes volumes of data, such as logs, metrics, deployments, and configuration changes. It can then identify anomalies and the root cause of issues. Investigations can be initiated automatically from Amazon CloudWatch Alarm actions. When a root cause is identified, the assistant recommends high-confidence runbooks curated by AWS to help mitigate issues where applicable. You can update colleagues about the investigation using Jira and ServiceNow integration and one-click investigation status updates.

**Topics**
+ [Tutorial: Configuring Amazon Q Developer operational investigations in chat applications](config-cbt-investigations.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
