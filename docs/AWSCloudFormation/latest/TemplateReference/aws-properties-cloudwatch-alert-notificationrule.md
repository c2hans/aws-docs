---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alert-notificationrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alert NotificationRule
<a name="aws-properties-cloudwatch-alert-notificationrule"></a>

A notification rule: which alert states trigger it, and where the notification is sent.

## Syntax
<a name="aws-properties-cloudwatch-alert-notificationrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alert-notificationrule-syntax.json"></a>

```
{
  "[Target](#cfn-cloudwatch-alert-notificationrule-target)" : {{Target}},
  "[Trigger](#cfn-cloudwatch-alert-notificationrule-trigger)" : {{Trigger}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alert-notificationrule-syntax.yaml"></a>

```
  [Target](#cfn-cloudwatch-alert-notificationrule-target): {{
    Target}}
  [Trigger](#cfn-cloudwatch-alert-notificationrule-trigger): {{
    Trigger}}
```

## Properties
<a name="aws-properties-cloudwatch-alert-notificationrule-properties"></a>

`Target`  <a name="cfn-cloudwatch-alert-notificationrule-target"></a>
Property description not available.
*Required*: Yes
*Type*: [Target](aws-properties-cloudwatch-alert-target.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Trigger`  <a name="cfn-cloudwatch-alert-notificationrule-trigger"></a>
Property description not available.
*Required*: Yes
*Type*: [Trigger](aws-properties-cloudwatch-alert-trigger.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
