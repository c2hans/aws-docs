---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-stream.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Stream
<a name="aws-resource-iot-stream"></a>

Describes a group of files that can be streamed.

## Syntax
<a name="aws-resource-iot-stream-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iot-stream-syntax.json"></a>

```
{
  "Type" : "AWS::IoT::Stream",
  "Properties" : {
      "[Description](#cfn-iot-stream-description)" : {{String}},
      "[Files](#cfn-iot-stream-files)" : {{[ StreamFile, ... ]}},
      "[RoleArn](#cfn-iot-stream-rolearn)" : {{String}},
      "[StreamId](#cfn-iot-stream-streamid)" : {{String}},
      "[Tags](#cfn-iot-stream-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iot-stream-syntax.yaml"></a>

```
Type: AWS::IoT::Stream
Properties:
  [Description](#cfn-iot-stream-description): {{String}}
  [Files](#cfn-iot-stream-files): {{
    - StreamFile}}
  [RoleArn](#cfn-iot-stream-rolearn): {{String}}
  [StreamId](#cfn-iot-stream-streamid): {{String}}
  [Tags](#cfn-iot-stream-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iot-stream-properties"></a>

`Description`  <a name="cfn-iot-stream-description"></a>
The description of the stream.
*Required*: No
*Type*: String
*Pattern*: `^[^\p{C}]+$`
*Maximum*: `2028`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Files`  <a name="cfn-iot-stream-files"></a>
The files to stream.
*Required*: Yes
*Type*: Array of [StreamFile](aws-properties-iot-stream-streamfile.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-iot-stream-rolearn"></a>
An IAM role AWS IoT assumes to access your S3 files.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamId`  <a name="cfn-iot-stream-streamid"></a>
The stream ID.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iot-stream-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-iot-stream-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iot-stream-return-values"></a>

### Ref
<a name="aws-resource-iot-stream-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-iot-stream-return-values-fn--getatt"></a>

####
<a name="aws-resource-iot-stream-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date when the stream was created.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The date when the stream was last updated.

`StreamVersion`  <a name="StreamVersion-fn::getatt"></a>
The stream version.
