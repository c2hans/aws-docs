---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-silentaudioconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput SilentAudioConfiguration
<a name="aws-properties-mediaconnect-routerinput-silentaudioconfiguration"></a>

<a name="aws-properties-mediaconnect-routerinput-silentaudioconfiguration-description"></a>The `SilentAudioConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::RouterInput](aws-resource-mediaconnect-routerinput.md).

## Syntax
<a name="aws-properties-mediaconnect-routerinput-silentaudioconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-silentaudioconfiguration-syntax.json"></a>

```
{
  "[State](#cfn-mediaconnect-routerinput-silentaudioconfiguration-state)" : {{String}},
  "[ThresholdSeconds](#cfn-mediaconnect-routerinput-silentaudioconfiguration-thresholdseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-silentaudioconfiguration-syntax.yaml"></a>

```
  [State](#cfn-mediaconnect-routerinput-silentaudioconfiguration-state): {{String}}
  [ThresholdSeconds](#cfn-mediaconnect-routerinput-silentaudioconfiguration-thresholdseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-silentaudioconfiguration-properties"></a>

`State`  <a name="cfn-mediaconnect-routerinput-silentaudioconfiguration-state"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThresholdSeconds`  <a name="cfn-mediaconnect-routerinput-silentaudioconfiguration-thresholdseconds"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
