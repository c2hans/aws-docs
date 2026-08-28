---
source_url: https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-cloudwatch.html
---

# Monitoring deployments with Amazon CloudWatch tools
<a name="monitoring-cloudwatch"></a>

You can monitor CodeDeploy deployments using the following CloudWatch tools: Amazon CloudWatch Events, CloudWatch alarms, and Amazon CloudWatch Logs.

Reviewing the logs created by the CodeDeploy agent and deployments can help you troubleshoot the causes of deployment failures. As an alternative to reviewing CodeDeploy logs on one instance at a time, you can use CloudWatch Logs to monitor all logs in a central location.

For information about using CloudWatch alarms and CloudWatch Events to monitor your CodeDeploy deployments, see the following topics.

**Topics**
+ [Monitoring deployments with CloudWatch alarms in CodeDeploy](monitoring-create-alarms.md)
+ [Monitoring deployments with Amazon CloudWatch Events](monitoring-cloudwatch-events.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
