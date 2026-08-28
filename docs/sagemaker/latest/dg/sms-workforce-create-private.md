---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private.html
---

# Create a Private Workforce (Amazon Cognito)
<a name="sms-workforce-create-private"></a>

When you use Amazon Cognito, you can create a private workforce in one of the following ways:
+ Create a new workforce while you are creating your labeling job. To learn how, see [Create an Amazon Cognito Workforce When Creating a Labeling Job](sms-workforce-create-private-console.md#create-workforce-labeling-job).
+ Create a new workforce before you create your labeling job. To learn how, see [Create an Amazon Cognito Workforce Using the Labeling Workforces Page](sms-workforce-create-private-console.md#create-workforce-sm-console).
+ Import an existing workforce after creating a user pool in the Amazon Cognito console. To learn how, see [Create a Private Workforce (Amazon Cognito Console)](sms-workforce-create-private-cognito.md).

Once you create a private workforce, that workforce and all work teams and workers associated with it are available to use for all Ground Truth labeling job tasks and Amazon Augmented AI human review workflows tasks.

If you are new to Amazon SageMaker AI and want to test Ground Truth or Amazon A2I, we suggest that you create a private work team consisting of people from your organization using the console. Use this work team when creating labeling or human review workflows (flow definitions) to test your worker UI and job workflow.

**Topics**
+ [Create a Private Workforce (Amazon SageMaker AI Console)](sms-workforce-create-private-console.md)
+ [Create a Private Workforce (Amazon Cognito Console)](sms-workforce-create-private-cognito.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
