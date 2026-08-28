---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-receiptrule-stopaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ReceiptRule StopAction
<a name="aws-properties-ses-receiptrule-stopaction"></a>

When included in a receipt rule, this action terminates the evaluation of the receipt rule set and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

For information about setting a stop action in a receipt rule, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-stop.html).

## Syntax
<a name="aws-properties-ses-receiptrule-stopaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-receiptrule-stopaction-syntax.json"></a>

```
{
  "[Scope](#cfn-ses-receiptrule-stopaction-scope)" : {{String}},
  "[TopicArn](#cfn-ses-receiptrule-stopaction-topicarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-receiptrule-stopaction-syntax.yaml"></a>

```
  [Scope](#cfn-ses-receiptrule-stopaction-scope): {{String}}
  [TopicArn](#cfn-ses-receiptrule-stopaction-topicarn): {{String}}
```

## Properties
<a name="aws-properties-ses-receiptrule-stopaction-properties"></a>

`Scope`  <a name="cfn-ses-receiptrule-stopaction-scope"></a>
The scope of the StopAction. The only acceptable value is `RuleSet`.
*Required*: Yes
*Type*: String
*Allowed values*: `RuleSet`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicArn`  <a name="cfn-ses-receiptrule-stopaction-topicarn"></a>
The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. You can find the ARN of a topic by using the [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) Amazon SNS operation.
For more information about Amazon SNS topics, see the [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
