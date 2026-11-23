---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-blackframesconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput BlackFramesConfiguration

Detects black frames in the router input's source content and reports them through a CloudWatch metric, an EventBridge event, and a router input message.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-blackframesconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-blackframesconfiguration-syntax.json"></a>

```json
{
  "[State](#cfn-mediaconnect-routerinput-blackframesconfiguration-state)" : {{String}},
  "[ThresholdSeconds](#cfn-mediaconnect-routerinput-blackframesconfiguration-thresholdseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-blackframesconfiguration-syntax.yaml"></a>

```yaml
  [State](#cfn-mediaconnect-routerinput-blackframesconfiguration-state): {{String}}
  [ThresholdSeconds](#cfn-mediaconnect-routerinput-blackframesconfiguration-thresholdseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-blackframesconfiguration-properties"></a>

`State`  <a name="cfn-mediaconnect-routerinput-blackframesconfiguration-state"></a>
Indicates whether black frames detection is enabled or disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThresholdSeconds`  <a name="cfn-mediaconnect-routerinput-blackframesconfiguration-thresholdseconds"></a>
The number of consecutive seconds of black frames that MediaConnect must detect before it reports an issue.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
