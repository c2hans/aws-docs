---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alert-trigger.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alert Trigger
<a name="aws-properties-cloudwatch-alert-trigger"></a>

The alert states that trigger the notification rule.

## Syntax
<a name="aws-properties-cloudwatch-alert-trigger-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alert-trigger-syntax.json"></a>

```
{
  "[StateValues](#cfn-cloudwatch-alert-trigger-statevalues)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alert-trigger-syntax.yaml"></a>

```
  [StateValues](#cfn-cloudwatch-alert-trigger-statevalues): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudwatch-alert-trigger-properties"></a>

`StateValues`  <a name="cfn-cloudwatch-alert-trigger-statevalues"></a>
The alert states that trigger this rule. A notification is sent when the alert enters any listed state. If omitted or empty, every state triggers the rule.
*Required*: No
*Type*: Array of String
*Allowed values*: `OK | WARNING | CRITICAL | NODATA`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
