---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-frozenframes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow FrozenFrames
<a name="aws-properties-mediaconnect-flow-frozenframes"></a>

 Configures settings for the `FrozenFrames` metric.

## Syntax
<a name="aws-properties-mediaconnect-flow-frozenframes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-frozenframes-syntax.json"></a>

```
{
  "[State](#cfn-mediaconnect-flow-frozenframes-state)" : {{String}},
  "[ThresholdSeconds](#cfn-mediaconnect-flow-frozenframes-thresholdseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-frozenframes-syntax.yaml"></a>

```
  [State](#cfn-mediaconnect-flow-frozenframes-state): {{String}}
  [ThresholdSeconds](#cfn-mediaconnect-flow-frozenframes-thresholdseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-frozenframes-properties"></a>

`State`  <a name="cfn-mediaconnect-flow-frozenframes-state"></a>
Indicates whether the `FrozenFrames` metric is enabled or disabled.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThresholdSeconds`  <a name="cfn-mediaconnect-flow-frozenframes-thresholdseconds"></a>
 Specifies the number of consecutive seconds of a static image that triggers an event or alert.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
