---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediaconnect-flowmediastream.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::FlowMediaStream
<a name="aws-resource-mediaconnect-flowmediastream"></a>

 Adds media streams to an existing flow. After you add a media stream to a flow, you can associate it with a source and/or an output that uses the ST 2110 JPEG XS or CDI protocol.

## Syntax
<a name="aws-resource-mediaconnect-flowmediastream-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediaconnect-flowmediastream-syntax.json"></a>

```
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

```
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
Property description not available.
*Required*: No
*Type*: [MediaStreamAttributes](aws-properties-mediaconnect-flowmediastream-mediastreamattributes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClockRate`  <a name="cfn-mediaconnect-flowmediastream-clockrate"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-mediaconnect-flowmediastream-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlowArn`  <a name="cfn-mediaconnect-flowmediastream-flowarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:flow:[a-zA-Z0-9-]+:[a-zA-Z0-9_-]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MediaStreamId`  <a name="cfn-mediaconnect-flowmediastream-mediastreamid"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MediaStreamName`  <a name="cfn-mediaconnect-flowmediastream-mediastreamname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MediaStreamType`  <a name="cfn-mediaconnect-flowmediastream-mediastreamtype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `video | audio | ancillary-data`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-mediaconnect-flowmediastream-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-mediaconnect-flowmediastream-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VideoFormat`  <a name="cfn-mediaconnect-flowmediastream-videoformat"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediaconnect-flowmediastream-return-values"></a>

### Ref
<a name="aws-resource-mediaconnect-flowmediastream-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-mediaconnect-flowmediastream-return-values-fn--getatt"></a>

####
<a name="aws-resource-mediaconnect-flowmediastream-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Fmt`  <a name="Fmt-fn::getatt"></a>
Property description not available.
