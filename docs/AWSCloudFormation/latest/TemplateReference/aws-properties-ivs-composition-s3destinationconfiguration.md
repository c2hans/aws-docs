---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-composition-s3destinationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::Composition S3DestinationConfiguration
<a name="aws-properties-ivs-composition-s3destinationconfiguration"></a>

A complex type that describes an S3 location where recorded videos will be stored.

## Syntax
<a name="aws-properties-ivs-composition-s3destinationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-composition-s3destinationconfiguration-syntax.json"></a>

```
{
  "[EncoderConfigurationArns](#cfn-ivs-composition-s3destinationconfiguration-encoderconfigurationarns)" : {{[ String, ... ]}},
  "[RecordingConfiguration](#cfn-ivs-composition-s3destinationconfiguration-recordingconfiguration)" : {{RecordingConfiguration}},
  "[StorageConfigurationArn](#cfn-ivs-composition-s3destinationconfiguration-storageconfigurationarn)" : {{String}},
  "[ThumbnailConfigurations](#cfn-ivs-composition-s3destinationconfiguration-thumbnailconfigurations)" : {{[ CompositionThumbnailConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-ivs-composition-s3destinationconfiguration-syntax.yaml"></a>

```
  [EncoderConfigurationArns](#cfn-ivs-composition-s3destinationconfiguration-encoderconfigurationarns): {{
    - String}}
  [RecordingConfiguration](#cfn-ivs-composition-s3destinationconfiguration-recordingconfiguration): {{
    RecordingConfiguration}}
  [StorageConfigurationArn](#cfn-ivs-composition-s3destinationconfiguration-storageconfigurationarn): {{String}}
  [ThumbnailConfigurations](#cfn-ivs-composition-s3destinationconfiguration-thumbnailconfigurations): {{
    - CompositionThumbnailConfiguration}}
```

## Properties
<a name="aws-properties-ivs-composition-s3destinationconfiguration-properties"></a>

`EncoderConfigurationArns`  <a name="cfn-ivs-composition-s3destinationconfiguration-encoderconfigurationarns"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `128 | 1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecordingConfiguration`  <a name="cfn-ivs-composition-s3destinationconfiguration-recordingconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [RecordingConfiguration](aws-properties-ivs-composition-recordingconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageConfigurationArn`  <a name="cfn-ivs-composition-s3destinationconfiguration-storageconfigurationarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws:ivs:[a-z0-9-]+:[0-9]+:storage-configuration/[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ThumbnailConfigurations`  <a name="cfn-ivs-composition-s3destinationconfiguration-thumbnailconfigurations"></a>
Property description not available.
*Required*: No
*Type*: Array of [CompositionThumbnailConfiguration](aws-properties-ivs-composition-compositionthumbnailconfiguration.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
