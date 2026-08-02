---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-h265filtersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel H265FilterSettings
<a name="aws-properties-medialive-channel-h265filtersettings"></a>

Settings to configure video filters that apply to the H265 codec.

The parent of this entity is H265Settings.

## Syntax
<a name="aws-properties-medialive-channel-h265filtersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-h265filtersettings-syntax.json"></a>

```
{
  "[BandwidthReductionFilterSettings](#cfn-medialive-channel-h265filtersettings-bandwidthreductionfiltersettings)" : {{BandwidthReductionFilterSettings}},
  "[TemporalFilterSettings](#cfn-medialive-channel-h265filtersettings-temporalfiltersettings)" : {{TemporalFilterSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-h265filtersettings-syntax.yaml"></a>

```
  [BandwidthReductionFilterSettings](#cfn-medialive-channel-h265filtersettings-bandwidthreductionfiltersettings): {{
    BandwidthReductionFilterSettings}}
  [TemporalFilterSettings](#cfn-medialive-channel-h265filtersettings-temporalfiltersettings): {{
    TemporalFilterSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-h265filtersettings-properties"></a>

`BandwidthReductionFilterSettings`  <a name="cfn-medialive-channel-h265filtersettings-bandwidthreductionfiltersettings"></a>
Bandwidth reduction filter settings for the H.265 codec.
*Required*: No
*Type*: [BandwidthReductionFilterSettings](aws-properties-medialive-channel-bandwidthreductionfiltersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemporalFilterSettings`  <a name="cfn-medialive-channel-h265filtersettings-temporalfiltersettings"></a>
Settings for applying the temporal filter to the video.
*Required*: No
*Type*: [TemporalFilterSettings](aws-properties-medialive-channel-temporalfiltersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
