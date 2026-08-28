---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-cfn-budget-notifications.html
---

# Budget threshold notifications to email and Slack with CloudFormation
<a name="examples-cfn-budget-notifications"></a>

The [budget\_events\_notification](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/notification_templates/budget_events_notification) CloudFormation template sets up notifications by email and to Slack when a budget threshold is reached in the `aws.deadline` service. The template creates the following resources:
+ An SNS topic with an email subscription.
+ An SNS topic policy that allows AWS services such as EventBridge to publish messages to the topic.
+ An IAM role that grants AWS Chatbot permission to publish messages.
+ An AWS Chatbot configuration that sends notifications to your Slack channel.
+ An EventBridge rule that captures `Budget Threshold Reached` events from `aws.deadline` and sends them to the SNS topic.

To deploy the template for Slack notifications, add AWS Chatbot to your Slack workspace, then copy the Slack channel ID and workspace ID for use as template parameters.

For more information about Deadline Cloud budgets and events, see [Managing Deadline Cloud events using Amazon EventBridge](eventbridge-integration.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
