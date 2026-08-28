---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-smsvoice-configurationset-snsdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::ConfigurationSet SnsDestination
<a name="aws-properties-smsvoice-configurationset-snsdestination"></a>

An object that defines an Amazon SNS destination for events. You can use Amazon SNS to send notification when certain events occur.

## Syntax
<a name="aws-properties-smsvoice-configurationset-snsdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-smsvoice-configurationset-snsdestination-syntax.json"></a>

```
{
  "[TopicArn](#cfn-smsvoice-configurationset-snsdestination-topicarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-smsvoice-configurationset-snsdestination-syntax.yaml"></a>

```
  [TopicArn](#cfn-smsvoice-configurationset-snsdestination-topicarn): {{String}}
```

## Properties
<a name="aws-properties-smsvoice-configurationset-snsdestination-properties"></a>

`TopicArn`  <a name="cfn-smsvoice-configurationset-snsdestination-topicarn"></a>
The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish events to.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:\S+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
