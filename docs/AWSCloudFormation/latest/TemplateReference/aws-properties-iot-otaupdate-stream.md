---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-otaupdate-stream.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate Stream
<a name="aws-properties-iot-otaupdate-stream"></a>

Describes a group of files that can be streamed.

## Syntax
<a name="aws-properties-iot-otaupdate-stream-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-otaupdate-stream-syntax.json"></a>

```
{
  "[FileId](#cfn-iot-otaupdate-stream-fileid)" : {{Integer}},
  "[StreamId](#cfn-iot-otaupdate-stream-streamid)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-otaupdate-stream-syntax.yaml"></a>

```
  [FileId](#cfn-iot-otaupdate-stream-fileid): {{Integer}}
  [StreamId](#cfn-iot-otaupdate-stream-streamid): {{String}}
```

## Properties
<a name="aws-properties-iot-otaupdate-stream-properties"></a>

`FileId`  <a name="cfn-iot-otaupdate-stream-fileid"></a>
The ID of a file associated with a stream.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StreamId`  <a name="cfn-iot-otaupdate-stream-streamid"></a>
The stream ID.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
