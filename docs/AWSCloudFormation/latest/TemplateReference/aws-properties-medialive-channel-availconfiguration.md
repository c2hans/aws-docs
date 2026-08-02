---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-availconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AvailConfiguration
<a name="aws-properties-medialive-channel-availconfiguration"></a>

The setup of ad avail handling in the output.

The parent of this entity is EncoderSettings.

## Syntax
<a name="aws-properties-medialive-channel-availconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-availconfiguration-syntax.json"></a>

```
{
  "[AvailSettings](#cfn-medialive-channel-availconfiguration-availsettings)" : {{AvailSettings}},
  "[Scte35SegmentationScope](#cfn-medialive-channel-availconfiguration-scte35segmentationscope)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-availconfiguration-syntax.yaml"></a>

```
  [AvailSettings](#cfn-medialive-channel-availconfiguration-availsettings): {{
    AvailSettings}}
  [Scte35SegmentationScope](#cfn-medialive-channel-availconfiguration-scte35segmentationscope): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-availconfiguration-properties"></a>

`AvailSettings`  <a name="cfn-medialive-channel-availconfiguration-availsettings"></a>
The setup of ad avail handling in the output.
*Required*: No
*Type*: [AvailSettings](aws-properties-medialive-channel-availsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scte35SegmentationScope`  <a name="cfn-medialive-channel-availconfiguration-scte35segmentationscope"></a>
Configures whether SCTE-35 passthrough triggers segment breaks in all output groups that use segmented outputs. Insertion of a SCTE-35 message typically results in a segment break, in addition to the regular cadence of breaks. ALL\_OUTPUT\_GROUPS: Insert the segment break in all output groups that have segmented outputs. This is the legacy behavior. SCTE35\_ENABLED\_OUTPUT\_GROUPS: Insert the segment break only in output groups that have SCTE-35 passthrough enabled. This is the recommended value, because it reduces unnecessary segment breaks.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
