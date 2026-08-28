---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-blackframes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow BlackFrames
<a name="aws-properties-mediaconnect-flow-blackframes"></a>

 Configures settings for the `BlackFrames` metric.

## Syntax
<a name="aws-properties-mediaconnect-flow-blackframes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-blackframes-syntax.json"></a>

```
{
  "[State](#cfn-mediaconnect-flow-blackframes-state)" : {{String}},
  "[ThresholdSeconds](#cfn-mediaconnect-flow-blackframes-thresholdseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-blackframes-syntax.yaml"></a>

```
  [State](#cfn-mediaconnect-flow-blackframes-state): {{String}}
  [ThresholdSeconds](#cfn-mediaconnect-flow-blackframes-thresholdseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-blackframes-properties"></a>

`State`  <a name="cfn-mediaconnect-flow-blackframes-state"></a>
 Indicates whether the `BlackFrames` metric is enabled or disabled.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThresholdSeconds`  <a name="cfn-mediaconnect-flow-blackframes-thresholdseconds"></a>
 Specifies the number of consecutive seconds of black frames that triggers an event or alert.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
