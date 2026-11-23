---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-frozenframesconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput FrozenFramesConfiguration

Detects frozen video frames in the router input's source content and reports them through a CloudWatch metric, an EventBridge event, and a router input message.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-frozenframesconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-frozenframesconfiguration-syntax.json"></a>

```json
{
  "[State](#cfn-mediaconnect-routerinput-frozenframesconfiguration-state)" : {{String}},
  "[ThresholdSeconds](#cfn-mediaconnect-routerinput-frozenframesconfiguration-thresholdseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-frozenframesconfiguration-syntax.yaml"></a>

```yaml
  [State](#cfn-mediaconnect-routerinput-frozenframesconfiguration-state): {{String}}
  [ThresholdSeconds](#cfn-mediaconnect-routerinput-frozenframesconfiguration-thresholdseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-frozenframesconfiguration-properties"></a>

`State`  <a name="cfn-mediaconnect-routerinput-frozenframesconfiguration-state"></a>
Indicates whether frozen frames detection is enabled or disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThresholdSeconds`  <a name="cfn-mediaconnect-routerinput-frozenframesconfiguration-thresholdseconds"></a>
The number of consecutive seconds of a frozen frame that MediaConnect must detect before it reports an issue.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
