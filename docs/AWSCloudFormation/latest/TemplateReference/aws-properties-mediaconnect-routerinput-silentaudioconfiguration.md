---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-silentaudioconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput SilentAudioConfiguration

Detects silent audio in the router input's source content and reports it through a CloudWatch metric, an EventBridge event, and a router input message.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-silentaudioconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-silentaudioconfiguration-syntax.json"></a>

```json
{
  "[State](#cfn-mediaconnect-routerinput-silentaudioconfiguration-state)" : {{String}},
  "[ThresholdSeconds](#cfn-mediaconnect-routerinput-silentaudioconfiguration-thresholdseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-silentaudioconfiguration-syntax.yaml"></a>

```yaml
  [State](#cfn-mediaconnect-routerinput-silentaudioconfiguration-state): {{String}}
  [ThresholdSeconds](#cfn-mediaconnect-routerinput-silentaudioconfiguration-thresholdseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-silentaudioconfiguration-properties"></a>

`State`  <a name="cfn-mediaconnect-routerinput-silentaudioconfiguration-state"></a>
Indicates whether silent audio detection is enabled or disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThresholdSeconds`  <a name="cfn-mediaconnect-routerinput-silentaudioconfiguration-thresholdseconds"></a>
The number of consecutive seconds of silence that MediaConnect must detect before it reports an issue.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
