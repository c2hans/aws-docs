---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-smartsubtitlesourcesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel SmartSubtitleSourceSettings
<a name="aws-properties-medialive-channel-smartsubtitlesourcesettings"></a>

Settings for a caption selector that uses subtitles that AWS Elemental Inference generates from the channel audio (Smart Subtitles). The channel's InferenceSettings must specify an Elemental Inference feed (InferenceSettings.FeedArn). The feed must have a subtitling output. For more information about Smart Subtitles, see [Smart Subtitles using Elemental Inference](https://docs.aws.amazon.com/medialive/latest/ug/elemental-inference-automatic-subtitling.html) in the *AWS Elemental MediaLive User Guide*.

The parent of this entity is CaptionSelectorSettings.

## Syntax
<a name="aws-properties-medialive-channel-smartsubtitlesourcesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-smartsubtitlesourcesettings-syntax.json"></a>

```
{
  "[CaptionSynchronizationMode](#cfn-medialive-channel-smartsubtitlesourcesettings-captionsynchronizationmode)" : {{String}},
  "[InferenceFeedOutput](#cfn-medialive-channel-smartsubtitlesourcesettings-inferencefeedoutput)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-smartsubtitlesourcesettings-syntax.yaml"></a>

```
  [CaptionSynchronizationMode](#cfn-medialive-channel-smartsubtitlesourcesettings-captionsynchronizationmode): {{String}}
  [InferenceFeedOutput](#cfn-medialive-channel-smartsubtitlesourcesettings-inferencefeedoutput): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-smartsubtitlesourcesettings-properties"></a>

`CaptionSynchronizationMode`  <a name="cfn-medialive-channel-smartsubtitlesourcesettings-captionsynchronizationmode"></a>
Specifies whether MediaLive delays the video to synchronize the subtitles with the audio and video. Valid values:
+ `NO_VIDEO_DELAY` – MediaLive doesn't delay the video. It inserts the subtitles into the video as they become available from Elemental Inference, so subtitles appear later than the speech they transcribe.
+ `VIDEO_ALIGNED_CAPTIONS` – MediaLive delays the video so that the subtitles appear at the same time as the speech they transcribe.
If you omit this property, MediaLive uses `VIDEO_ALIGNED_CAPTIONS`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InferenceFeedOutput`  <a name="cfn-medialive-channel-smartsubtitlesourcesettings-inferencefeedoutput"></a>
The name of the Elemental Inference feed output that supplies subtitles to this caption selector. For example, `medialive-subtitling-output-0`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
