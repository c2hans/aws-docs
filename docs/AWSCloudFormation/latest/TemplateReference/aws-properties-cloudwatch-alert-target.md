---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alert-target.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alert Target
<a name="aws-properties-cloudwatch-alert-target"></a>

Where the notification is sent.

## Syntax
<a name="aws-properties-cloudwatch-alert-target-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alert-target-syntax.json"></a>

```
{
  "[Arn](#cfn-cloudwatch-alert-target-arn)" : {{String}},
  "[Metadata](#cfn-cloudwatch-alert-target-metadata)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Type](#cfn-cloudwatch-alert-target-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alert-target-syntax.yaml"></a>

```
  [Arn](#cfn-cloudwatch-alert-target-arn): {{String}}
  [Metadata](#cfn-cloudwatch-alert-target-metadata): {{
    {{Key}}: {{Value}}}}
  [Type](#cfn-cloudwatch-alert-target-type): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-alert-target-properties"></a>

`Arn`  <a name="cfn-cloudwatch-alert-target-arn"></a>
The ARN of the target. For sns, the ARN of the Amazon SNS topic. For slack and pagerduty, the ARN of a CloudWatch Omni integration.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.+$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metadata`  <a name="cfn-cloudwatch-alert-target-metadata"></a>
Settings specific to the target, as key-value pairs (up to 20). The keys depend on the integration type. Not used for sns targets.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-cloudwatch-alert-target-type"></a>
The target type. Valid values: sns, slack, pagerduty.
*Required*: Yes
*Type*: String
*Allowed values*: `sns | slack | pagerduty`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
