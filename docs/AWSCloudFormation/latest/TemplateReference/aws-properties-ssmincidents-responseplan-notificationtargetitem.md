---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmincidents-responseplan-notificationtargetitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMIncidents::ResponsePlan NotificationTargetItem
<a name="aws-properties-ssmincidents-responseplan-notificationtargetitem"></a>

The Amazon SNS topic that's used by Amazon Q Developer in chat applications to notify the incidents chat channel.

## Syntax
<a name="aws-properties-ssmincidents-responseplan-notificationtargetitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmincidents-responseplan-notificationtargetitem-syntax.json"></a>

```
{
  "[SnsTopicArn](#cfn-ssmincidents-responseplan-notificationtargetitem-snstopicarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssmincidents-responseplan-notificationtargetitem-syntax.yaml"></a>

```
  [SnsTopicArn](#cfn-ssmincidents-responseplan-notificationtargetitem-snstopicarn): {{String}}
```

## Properties
<a name="aws-properties-ssmincidents-responseplan-notificationtargetitem-properties"></a>

`SnsTopicArn`  <a name="cfn-ssmincidents-responseplan-notificationtargetitem-snstopicarn"></a>
The Amazon Resource Name (ARN) of the Amazon SNS topic.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-(cn|us-gov))?:sns:(([a-z]+-)+[0-9])?:([0-9]{12})?:[^.]+$`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
