---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-frozenframesconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput FrozenFramesConfiguration
<a name="aws-properties-mediaconnect-routerinput-frozenframesconfiguration"></a>

<a name="aws-properties-mediaconnect-routerinput-frozenframesconfiguration-description"></a>The `FrozenFramesConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::RouterInput](aws-resource-mediaconnect-routerinput.md).

## Syntax
<a name="aws-properties-mediaconnect-routerinput-frozenframesconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-frozenframesconfiguration-syntax.json"></a>

```
{
  "[State](#cfn-mediaconnect-routerinput-frozenframesconfiguration-state)" : {{String}},
  "[ThresholdSeconds](#cfn-mediaconnect-routerinput-frozenframesconfiguration-thresholdseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-frozenframesconfiguration-syntax.yaml"></a>

```
  [State](#cfn-mediaconnect-routerinput-frozenframesconfiguration-state): {{String}}
  [ThresholdSeconds](#cfn-mediaconnect-routerinput-frozenframesconfiguration-thresholdseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-frozenframesconfiguration-properties"></a>

`State`  <a name="cfn-mediaconnect-routerinput-frozenframesconfiguration-state"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThresholdSeconds`  <a name="cfn-mediaconnect-routerinput-frozenframesconfiguration-thresholdseconds"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
