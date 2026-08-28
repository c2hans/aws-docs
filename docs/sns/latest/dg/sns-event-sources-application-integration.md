---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-application-integration.html
---

# Application integration services
<a name="sns-event-sources-application-integration"></a>

The following table describes how Amazon SNS integrates with application integration services such as EventBridge and AWS Step Functions, enabling real-time data routing and notifications for business-critical applications.

You can leverage these integrations to receive alerts from EventBridge events and orchestrate workflows using Step Functions, enhancing the automation and responsiveness of your applications.

| AWS service | Benefit of using with Amazon SNS |
| --- | --- |
| [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html) – Delivers a stream of real-time data from your own applications, software-as-a-service (SaaS) applications, and AWS services and routes that data to targets, including Amazon SNS. EventBridge was formerly called CloudWatch Events. | Receive notifications of EventBridge events. For more information, see [Amazon EventBridge targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-targets.html) in the *Amazon EventBridge User Guide*. |
| [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) – Lets you combine AWS Lambda functions and other AWS services to build business-critical applications. | Receive notification of Step Functions events. For more information, see [Call Amazon SNS with Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-sns.html) in the *AWS Step Functions Developer Guide*. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
