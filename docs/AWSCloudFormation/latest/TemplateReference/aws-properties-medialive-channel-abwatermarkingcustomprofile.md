---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-abwatermarkingcustomprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AbWatermarkingCustomProfile
<a name="aws-properties-medialive-channel-abwatermarkingcustomprofile"></a>

The vendor-specified custom profile options

## Syntax
<a name="aws-properties-medialive-channel-abwatermarkingcustomprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-abwatermarkingcustomprofile-syntax.json"></a>

```
{
  "[EmbeddingFrequency](#cfn-medialive-channel-abwatermarkingcustomprofile-embeddingfrequency)" : {{Number}},
  "[SceneCut](#cfn-medialive-channel-abwatermarkingcustomprofile-scenecut)" : {{Number}},
  "[TargetPsnr](#cfn-medialive-channel-abwatermarkingcustomprofile-targetpsnr)" : {{Number}}
}
```

### YAML
<a name="aws-properties-medialive-channel-abwatermarkingcustomprofile-syntax.yaml"></a>

```
  [EmbeddingFrequency](#cfn-medialive-channel-abwatermarkingcustomprofile-embeddingfrequency): {{Number}}
  [SceneCut](#cfn-medialive-channel-abwatermarkingcustomprofile-scenecut): {{Number}}
  [TargetPsnr](#cfn-medialive-channel-abwatermarkingcustomprofile-targetpsnr): {{Number}}
```

## Properties
<a name="aws-properties-medialive-channel-abwatermarkingcustomprofile-properties"></a>

`EmbeddingFrequency`  <a name="cfn-medialive-channel-abwatermarkingcustomprofile-embeddingfrequency"></a>
The frequency with which watermarks will be embedded, in milliseconds.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SceneCut`  <a name="cfn-medialive-channel-abwatermarkingcustomprofile-scenecut"></a>
The number of frames after scene-cut to embed the watermark.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetPsnr`  <a name="cfn-medialive-channel-abwatermarkingcustomprofile-targetpsnr"></a>
The target PSNR of the watermarked frame
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
