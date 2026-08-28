---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-private.html
---

# Manage a Private Workforce (Amazon Cognito)
<a name="sms-workforce-management-private"></a>

After you have created a private workforce using Amazon Cognito, you can create and manage work teams using the Amazon SageMaker AI console and API operations.

You can do the following using either the [SageMaker AI console](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-private-console.html) or [Amazon Cognito console](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-private-cognito.html).
+ Add and delete work teams.
+ Add workers to your workforce and one or more work teams.
+ Disable or remove workers from your workforce and one or more workteams. If you add workers to a workforce using the Amazon Cognito console, you must use the same console to remove the worker from the workforce.

You can restrict access to tasks to workers at specific IP addresses using the SageMaker API. For more information, see [Private workforce management using the Amazon SageMaker API](sms-workforce-management-private-api.md).

**Topics**
+ [Manage a Workforce (Amazon SageMaker AI Console)](sms-workforce-management-private-console.md)
+ [Manage a Private Workforce (Amazon Cognito Console)](sms-workforce-management-private-cognito.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
