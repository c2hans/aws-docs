---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::EventBridgeRuleTemplate EventBridgeRuleTemplateTarget
<a name="aws-properties-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget"></a>

The target to which to send matching events.

## Syntax
<a name="aws-properties-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget-syntax.json"></a>

```
{
  "[Arn](#cfn-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget-syntax.yaml"></a>

```
  [Arn](#cfn-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget-arn): {{String}}
```

## Properties
<a name="aws-properties-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget-properties"></a>

`Arn`  <a name="cfn-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget-arn"></a>
Target ARNs must be either an SNS topic or CloudWatch log group.
*Required*: Yes
*Type*: String
*Pattern*: `^arn.+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
