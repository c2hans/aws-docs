---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-srtgroupsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel SrtGroupSettings
<a name="aws-properties-medialive-channel-srtgroupsettings"></a>

Srt Group Settings

## Syntax
<a name="aws-properties-medialive-channel-srtgroupsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-srtgroupsettings-syntax.json"></a>

```
{
  "[InputLossAction](#cfn-medialive-channel-srtgroupsettings-inputlossaction)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-srtgroupsettings-syntax.yaml"></a>

```
  [InputLossAction](#cfn-medialive-channel-srtgroupsettings-inputlossaction): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-srtgroupsettings-properties"></a>

`InputLossAction`  <a name="cfn-medialive-channel-srtgroupsettings-inputlossaction"></a>
Specifies behavior of last resort when input video is lost, and no more backup inputs are available. When dropTs is selected the entire transport stream will stop being emitted. When dropProgram is selected the program can be dropped from the transport stream (and replaced with null packets to meet the TS bitrate requirement). Or, when emitProgram is chosen the transport stream will continue to be produced normally with repeat frames, black frames, or slate frames substituted for the absent input video.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
