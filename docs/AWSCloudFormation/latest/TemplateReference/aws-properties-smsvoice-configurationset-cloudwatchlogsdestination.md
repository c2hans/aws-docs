---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-smsvoice-configurationset-cloudwatchlogsdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::ConfigurationSet CloudWatchLogsDestination
<a name="aws-properties-smsvoice-configurationset-cloudwatchlogsdestination"></a>

Contains the destination configuration to use when publishing message sending events.

## Syntax
<a name="aws-properties-smsvoice-configurationset-cloudwatchlogsdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-smsvoice-configurationset-cloudwatchlogsdestination-syntax.json"></a>

```
{
  "[IamRoleArn](#cfn-smsvoice-configurationset-cloudwatchlogsdestination-iamrolearn)" : {{String}},
  "[LogGroupArn](#cfn-smsvoice-configurationset-cloudwatchlogsdestination-loggrouparn)" : {{String}}
}
```

### YAML
<a name="aws-properties-smsvoice-configurationset-cloudwatchlogsdestination-syntax.yaml"></a>

```
  [IamRoleArn](#cfn-smsvoice-configurationset-cloudwatchlogsdestination-iamrolearn): {{String}}
  [LogGroupArn](#cfn-smsvoice-configurationset-cloudwatchlogsdestination-loggrouparn): {{String}}
```

## Properties
<a name="aws-properties-smsvoice-configurationset-cloudwatchlogsdestination-properties"></a>

`IamRoleArn`  <a name="cfn-smsvoice-configurationset-cloudwatchlogsdestination-iamrolearn"></a>
The Amazon Resource Name (ARN) of an AWS Identity and Access Management role that is able to write event data to an Amazon CloudWatch destination.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:\S+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroupArn`  <a name="cfn-smsvoice-configurationset-cloudwatchlogsdestination-loggrouparn"></a>
The name of the Amazon CloudWatch log group that you want to record events in.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:\S+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
