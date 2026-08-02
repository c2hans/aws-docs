---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-mediastream.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow MediaStream
<a name="aws-properties-mediaconnect-flow-mediastream"></a>

 A media stream represents one component of your content, such as video, audio, or ancillary data. After you add a media stream to your flow, you can associate it with sources and outputs that use the ST 2110 JPEG XS or CDI protocol.

## Syntax
<a name="aws-properties-mediaconnect-flow-mediastream-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-mediastream-syntax.json"></a>

```
{
  "[Attributes](#cfn-mediaconnect-flow-mediastream-attributes)" : {{MediaStreamAttributes}},
  "[ClockRate](#cfn-mediaconnect-flow-mediastream-clockrate)" : {{Integer}},
  "[Description](#cfn-mediaconnect-flow-mediastream-description)" : {{String}},
  "[Fmt](#cfn-mediaconnect-flow-mediastream-fmt)" : {{Integer}},
  "[MediaStreamId](#cfn-mediaconnect-flow-mediastream-mediastreamid)" : {{Integer}},
  "[MediaStreamName](#cfn-mediaconnect-flow-mediastream-mediastreamname)" : {{String}},
  "[MediaStreamType](#cfn-mediaconnect-flow-mediastream-mediastreamtype)" : {{String}},
  "[Tags](#cfn-mediaconnect-flow-mediastream-tags)" : {{[ Tag, ... ]}},
  "[VideoFormat](#cfn-mediaconnect-flow-mediastream-videoformat)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-mediastream-syntax.yaml"></a>

```
  [Attributes](#cfn-mediaconnect-flow-mediastream-attributes): {{
    MediaStreamAttributes}}
  [ClockRate](#cfn-mediaconnect-flow-mediastream-clockrate): {{Integer}}
  [Description](#cfn-mediaconnect-flow-mediastream-description): {{String}}
  [Fmt](#cfn-mediaconnect-flow-mediastream-fmt): {{Integer}}
  [MediaStreamId](#cfn-mediaconnect-flow-mediastream-mediastreamid): {{Integer}}
  [MediaStreamName](#cfn-mediaconnect-flow-mediastream-mediastreamname): {{String}}
  [MediaStreamType](#cfn-mediaconnect-flow-mediastream-mediastreamtype): {{String}}
  [Tags](#cfn-mediaconnect-flow-mediastream-tags): {{
    - Tag}}
  [VideoFormat](#cfn-mediaconnect-flow-mediastream-videoformat): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-mediastream-properties"></a>

`Attributes`  <a name="cfn-mediaconnect-flow-mediastream-attributes"></a>
 Attributes that are related to the media stream.
*Required*: No
*Type*: [MediaStreamAttributes](aws-properties-mediaconnect-flow-mediastreamattributes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClockRate`  <a name="cfn-mediaconnect-flow-mediastream-clockrate"></a>
 The sample rate for the stream. This value is measured in Hz.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-mediaconnect-flow-mediastream-description"></a>
 A description that can help you quickly identify what your media stream is used for.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Fmt`  <a name="cfn-mediaconnect-flow-mediastream-fmt"></a>
 The format type number (sometimes referred to as RTP payload type) of the media stream. MediaConnect assigns this value to the media stream. For ST 2110 JPEG XS outputs, you need to provide this value to the receiver.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaStreamId`  <a name="cfn-mediaconnect-flow-mediastream-mediastreamid"></a>
 A unique identifier for the media stream.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaStreamName`  <a name="cfn-mediaconnect-flow-mediastream-mediastreamname"></a>
 A name that helps you distinguish one media stream from another.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaStreamType`  <a name="cfn-mediaconnect-flow-mediastream-mediastreamtype"></a>
 The type of media stream.
*Required*: Yes
*Type*: String
*Allowed values*: `video | audio | ancillary-data`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-mediaconnect-flow-mediastream-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Resource tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-mediaconnect-flow-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VideoFormat`  <a name="cfn-mediaconnect-flow-mediastream-videoformat"></a>
 The resolution of the video.
*Required*: No
*Type*: String
*Allowed values*: `2160p | 1080p | 1080i | 720p | 480p`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
