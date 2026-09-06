---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-h264filtersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel H264FilterSettings
<a name="aws-properties-medialive-channel-h264filtersettings"></a>

Settings to configure video filters that apply to the H264 codec.

The parent of this entity is H264Settings.

## Syntax
<a name="aws-properties-medialive-channel-h264filtersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-h264filtersettings-syntax.json"></a>

```
{
  "[BandwidthReductionFilterSettings](#cfn-medialive-channel-h264filtersettings-bandwidthreductionfiltersettings)" : {{BandwidthReductionFilterSettings}},
  "[TemporalFilterSettings](#cfn-medialive-channel-h264filtersettings-temporalfiltersettings)" : {{TemporalFilterSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-h264filtersettings-syntax.yaml"></a>

```
  [BandwidthReductionFilterSettings](#cfn-medialive-channel-h264filtersettings-bandwidthreductionfiltersettings): {{
    BandwidthReductionFilterSettings}}
  [TemporalFilterSettings](#cfn-medialive-channel-h264filtersettings-temporalfiltersettings): {{
    TemporalFilterSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-h264filtersettings-properties"></a>

`BandwidthReductionFilterSettings`  <a name="cfn-medialive-channel-h264filtersettings-bandwidthreductionfiltersettings"></a>
Bandwidth reduction filter settings for the H.264 codec.
*Required*: No
*Type*: [BandwidthReductionFilterSettings](aws-properties-medialive-channel-bandwidthreductionfiltersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemporalFilterSettings`  <a name="cfn-medialive-channel-h264filtersettings-temporalfiltersettings"></a>
Settings for applying the temporal filter to the video.
*Required*: No
*Type*: [TemporalFilterSettings](aws-properties-medialive-channel-temporalfiltersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
