---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-composition-compositionthumbnailconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::Composition CompositionThumbnailConfiguration
<a name="aws-properties-ivs-composition-compositionthumbnailconfiguration"></a>

<a name="aws-properties-ivs-composition-compositionthumbnailconfiguration-description"></a>The `CompositionThumbnailConfiguration` property type specifies Property description not available. for an [AWS::IVS::Composition](aws-resource-ivs-composition.md).

## Syntax
<a name="aws-properties-ivs-composition-compositionthumbnailconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-composition-compositionthumbnailconfiguration-syntax.json"></a>

```
{
  "[Storage](#cfn-ivs-composition-compositionthumbnailconfiguration-storage)" : {{[ String, ... ]}},
  "[TargetIntervalSeconds](#cfn-ivs-composition-compositionthumbnailconfiguration-targetintervalseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ivs-composition-compositionthumbnailconfiguration-syntax.yaml"></a>

```
  [Storage](#cfn-ivs-composition-compositionthumbnailconfiguration-storage): {{
    - String}}
  [TargetIntervalSeconds](#cfn-ivs-composition-compositionthumbnailconfiguration-targetintervalseconds): {{Integer}}
```

## Properties
<a name="aws-properties-ivs-composition-compositionthumbnailconfiguration-properties"></a>

`Storage`  <a name="cfn-ivs-composition-compositionthumbnailconfiguration-storage"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Allowed values*: `SEQUENTIAL | LATEST`
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetIntervalSeconds`  <a name="cfn-ivs-composition-compositionthumbnailconfiguration-targetintervalseconds"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `86400`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
