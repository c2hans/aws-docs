---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediaconnect-flowmediastream.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::FlowMediaStream

 Adds media streams to an existing flow. After you add a media stream to a flow, you can associate it with a source and/or an output that uses the ST 2110 JPEG XS or CDI protocol.

## Syntax
<a name="aws-resource-mediaconnect-flowmediastream-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediaconnect-flowmediastream-syntax.json"></a>

```json
{
  "Type" : "AWS::MediaConnect::FlowMediaStream",
  "Properties" : {
      "[Attributes](#cfn-mediaconnect-flowmediastream-attributes)" : {{MediaStreamAttributes}},
      "[ClockRate](#cfn-mediaconnect-flowmediastream-clockrate)" : {{Integer}},
      "[Description](#cfn-mediaconnect-flowmediastream-description)" : {{String}},
      "[FlowArn](#cfn-mediaconnect-flowmediastream-flowarn)" : {{String}},
      "[MediaStreamId](#cfn-mediaconnect-flowmediastream-mediastreamid)" : {{Integer}},
      "[MediaStreamName](#cfn-mediaconnect-flowmediastream-mediastreamname)" : {{String}},
      "[MediaStreamType](#cfn-mediaconnect-flowmediastream-mediastreamtype)" : {{String}},
      "[Tags](#cfn-mediaconnect-flowmediastream-tags)" : {{[ Tag, ... ]}},
      "[VideoFormat](#cfn-mediaconnect-flowmediastream-videoformat)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-mediaconnect-flowmediastream-syntax.yaml"></a>

```yaml
Type: AWS::MediaConnect::FlowMediaStream
Properties:
  [Attributes](#cfn-mediaconnect-flowmediastream-attributes): {{
    MediaStreamAttributes}}
  [ClockRate](#cfn-mediaconnect-flowmediastream-clockrate): {{Integer}}
  [Description](#cfn-mediaconnect-flowmediastream-description): {{String}}
  [FlowArn](#cfn-mediaconnect-flowmediastream-flowarn): {{String}}
  [MediaStreamId](#cfn-mediaconnect-flowmediastream-mediastreamid): {{Integer}}
  [MediaStreamName](#cfn-mediaconnect-flowmediastream-mediastreamname): {{String}}
  [MediaStreamType](#cfn-mediaconnect-flowmediastream-mediastreamtype): {{String}}
  [Tags](#cfn-mediaconnect-flowmediastream-tags): {{
    - Tag}}
  [VideoFormat](#cfn-mediaconnect-flowmediastream-videoformat): {{String}}
```

## Properties
<a name="aws-resource-mediaconnect-flowmediastream-properties"></a>

`Attributes`  <a name="cfn-mediaconnect-flowmediastream-attributes"></a>
 The attributes that you want to assign to the new media stream.
*Required*: No
*Type*: [MediaStreamAttributes](aws-properties-mediaconnect-flowmediastream-mediastreamattributes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClockRate`  <a name="cfn-mediaconnect-flowmediastream-clockrate"></a>
 The sample rate (in Hz) for the stream. If the media stream type is video or ancillary data, set this value to 90000. If the media stream type is audio, set this value to either 48000 or 96000.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-mediaconnect-flowmediastream-description"></a>
 A description that can help you quickly identify what your media stream is used for.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlowArn`  <a name="cfn-mediaconnect-flowmediastream-flowarn"></a>
 The Amazon Resource Name (ARN) of the flow.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:flow:[a-zA-Z0-9-]+:[a-zA-Z0-9_-]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MediaStreamId`  <a name="cfn-mediaconnect-flowmediastream-mediastreamid"></a>
 A unique identifier for the media stream.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MediaStreamName`  <a name="cfn-mediaconnect-flowmediastream-mediastreamname"></a>
 A name that helps you distinguish one media stream from another.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MediaStreamType`  <a name="cfn-mediaconnect-flowmediastream-mediastreamtype"></a>
 The type of media stream.
*Required*: Yes
*Type*: String
*Allowed values*: `video | audio | ancillary-data`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-mediaconnect-flowmediastream-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Resource tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-mediaconnect-flowmediastream-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VideoFormat`  <a name="cfn-mediaconnect-flowmediastream-videoformat"></a>
 The resolution of the video.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediaconnect-flowmediastream-return-values"></a>

### Ref
<a name="aws-resource-mediaconnect-flowmediastream-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the media stream ARN. For example:

 `{ "Ref": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame/mediaStream/Video1" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-mediaconnect-flowmediastream-return-values-fn--getatt"></a>

####
<a name="aws-resource-mediaconnect-flowmediastream-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the media stream.

`Fmt`  <a name="Fmt-fn::getatt"></a>
 The format type number (sometimes referred to as RTP payload type) of the media stream. MediaConnect assigns this value to the media stream. For ST 2110 JPEG XS outputs, you need to provide this value to the receiver.
