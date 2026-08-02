---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-recordingconfiguration-renditionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::RecordingConfiguration RenditionConfiguration
<a name="aws-properties-ivs-recordingconfiguration-renditionconfiguration"></a>

The RenditionConfiguration property type describes which renditions should be recorded for a stream.

## Syntax
<a name="aws-properties-ivs-recordingconfiguration-renditionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-recordingconfiguration-renditionconfiguration-syntax.json"></a>

```
{
  "[Renditions](#cfn-ivs-recordingconfiguration-renditionconfiguration-renditions)" : {{[ String, ... ]}},
  "[RenditionSelection](#cfn-ivs-recordingconfiguration-renditionconfiguration-renditionselection)" : {{String}}
}
```

### YAML
<a name="aws-properties-ivs-recordingconfiguration-renditionconfiguration-syntax.yaml"></a>

```
  [Renditions](#cfn-ivs-recordingconfiguration-renditionconfiguration-renditions): {{
    - String}}
  [RenditionSelection](#cfn-ivs-recordingconfiguration-renditionconfiguration-renditionselection): {{String}}
```

## Properties
<a name="aws-properties-ivs-recordingconfiguration-renditionconfiguration-properties"></a>

`Renditions`  <a name="cfn-ivs-recordingconfiguration-renditionconfiguration-renditions"></a>
A list of which renditions are recorded for a stream, if `renditionSelection` is `CUSTOM`; otherwise, this field is irrelevant. The selected renditions are recorded if they are available during the stream. If a selected rendition is unavailable, the best available rendition is recorded. For details on the resolution dimensions of each rendition, see [Auto-Record to Amazon S3](https://docs.aws.amazon.com//ivs/latest/LowLatencyUserGuide/record-to-s3.html).
*Required*: No
*Type*: Array of String
*Allowed values*: `FULL_HD | HD | SD | LOWEST_RESOLUTION`
*Minimum*: `0`
*Maximum*: `4`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RenditionSelection`  <a name="cfn-ivs-recordingconfiguration-renditionconfiguration-renditionselection"></a>
The set of renditions are recorded for a stream. For `BASIC` channels, the `CUSTOM` value has no effect. If `CUSTOM` is specified, a set of renditions can be specified in the `renditions` field. Default: `ALL`.
*Required*: No
*Type*: String
*Allowed values*: `ALL | NONE | CUSTOM`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
