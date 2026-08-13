---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-composition-recordingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::Composition RecordingConfiguration
<a name="aws-properties-ivs-composition-recordingconfiguration"></a>

An object representing a configuration to record a channel stream.

## Syntax
<a name="aws-properties-ivs-composition-recordingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-composition-recordingconfiguration-syntax.json"></a>

```
{
  "[Format](#cfn-ivs-composition-recordingconfiguration-format)" : {{String}},
  "[HlsConfiguration](#cfn-ivs-composition-recordingconfiguration-hlsconfiguration)" : {{CompositionRecordingHlsConfiguration}}
}
```

### YAML
<a name="aws-properties-ivs-composition-recordingconfiguration-syntax.yaml"></a>

```
  [Format](#cfn-ivs-composition-recordingconfiguration-format): {{String}}
  [HlsConfiguration](#cfn-ivs-composition-recordingconfiguration-hlsconfiguration): {{
    CompositionRecordingHlsConfiguration}}
```

## Properties
<a name="aws-properties-ivs-composition-recordingconfiguration-properties"></a>

`Format`  <a name="cfn-ivs-composition-recordingconfiguration-format"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `HLS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HlsConfiguration`  <a name="cfn-ivs-composition-recordingconfiguration-hlsconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [CompositionRecordingHlsConfiguration](aws-properties-ivs-composition-compositionrecordinghlsconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
