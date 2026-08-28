---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-workteam-notificationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Workteam NotificationConfiguration
<a name="aws-properties-sagemaker-workteam-notificationconfiguration"></a>

Configures Amazon SNS notifications of available or expiring work items for work teams.

## Syntax
<a name="aws-properties-sagemaker-workteam-notificationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-workteam-notificationconfiguration-syntax.json"></a>

```
{
  "[NotificationTopicArn](#cfn-sagemaker-workteam-notificationconfiguration-notificationtopicarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-workteam-notificationconfiguration-syntax.yaml"></a>

```
  [NotificationTopicArn](#cfn-sagemaker-workteam-notificationconfiguration-notificationtopicarn): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-workteam-notificationconfiguration-properties"></a>

`NotificationTopicArn`  <a name="cfn-sagemaker-workteam-notificationconfiguration-notificationtopicarn"></a>
The ARN for the Amazon SNS topic to which notifications should be published.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws[a-z\-]*:sns:[a-z0-9\-]*:[0-9]{12}:[a-zA-Z0-9_.-]*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
