---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-metrics.html
---

# CloudWatch Metrics
<a name="browser-metrics"></a>

You can view the following metrics in Amazon CloudWatch:
+ Session counts: The number of browser sessions that have been requested
+ Session duration: The length of time browser sessions are active
+ Error rates: The frequency of errors encountered during browser sessions
+ Resource utilization: CPU, memory, and network usage by browser sessions

These metrics can be used to monitor the usage and performance of your browser sessions, set up alarms for abnormal behavior, and optimize your resource allocation.

For more information, see [AgentCore generated built-in tools observability data](observability-tool-metrics.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
