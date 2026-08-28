---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/slack-integration.html
---

# Slack integration
<a name="slack-integration"></a>

This solution includes an optional configuration to send notifications to your existing Slack channel. To use this feature, you must have an existing Slack channel and specify Slack webhook URL on the Systems Manager Parameter Store `/QuotaMonitor/SlackHook`.

The following figure depicts an example of using Slack notifications with the solution.

 **Image depicts an example Quota Monitor Notification in Slack**

![slack integration](http://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/slack-integration.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quota Monitor for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
