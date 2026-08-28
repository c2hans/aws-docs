---
source_url: https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-services.html
---

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Supported services for Amazon Q Developer in chat applications
<a name="chatbot-services"></a>

Amazon Q Developer in chat applications supports AWS services that emit events to Amazon EventBridge, including Amazon GuardDuty, CloudFormation, AWS Cost Anomaly Detection, and AWS Budgets. For a complete list of supported services, see the [*Amazon EventBridge Event Reference*](https://docs.aws.amazon.com/eventbridge/latest/ref/welcome.html).

Amazon Q Developer in chat applications also supports notifications for the following services:
+ Amazon CloudWatch
+ Amazon CodeCatalyst
+ AWS Cost Anomaly Detection

Most AWS services that you can manage using the [AWS Command Line Interface (CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) are also supported. Subsequently, you can manage your AWS resources from these services using AWS CLI commands directly from your chat channels.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
