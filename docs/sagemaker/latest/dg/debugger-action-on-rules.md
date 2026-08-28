---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-action-on-rules.html
---

# Action on Amazon SageMaker Debugger rules
<a name="debugger-action-on-rules"></a>

**Note**
Amazon SageMaker Debugger is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Debugger, but we do not plan to introduce new features. For more information, see [Debugger availability change](debugger-availability-change.md).

Based on the Debugger rule evaluation status, you can set up automated actions such as stopping a training job and sending notifications using Amazon Simple Notification Service (Amazon SNS). You can also create your own actions using Amazon CloudWatch Events and AWS Lambda. To learn how to set up automated actions based on the Debugger rule evaluation status, see the following topics.

**Topics**
+ [Use Debugger built-in actions for rules](debugger-built-in-actions.md)
+ [Actions on rules using Amazon CloudWatch and AWS Lambda](debugger-cloudwatch-lambda.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
