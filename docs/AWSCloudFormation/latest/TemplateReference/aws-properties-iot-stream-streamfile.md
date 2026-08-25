---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-stream-streamfile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Stream StreamFile
<a name="aws-properties-iot-stream-streamfile"></a>

Represents a file to stream.

## Syntax
<a name="aws-properties-iot-stream-streamfile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-stream-streamfile-syntax.json"></a>

```
{
  "[FileId](#cfn-iot-stream-streamfile-fileid)" : {{Integer}},
  "[S3Location](#cfn-iot-stream-streamfile-s3location)" : {{S3Location}}
}
```

### YAML
<a name="aws-properties-iot-stream-streamfile-syntax.yaml"></a>

```
  [FileId](#cfn-iot-stream-streamfile-fileid): {{Integer}}
  [S3Location](#cfn-iot-stream-streamfile-s3location): {{
    S3Location}}
```

## Properties
<a name="aws-properties-iot-stream-streamfile-properties"></a>

`FileId`  <a name="cfn-iot-stream-streamfile-fileid"></a>
The file ID.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Location`  <a name="cfn-iot-stream-streamfile-s3location"></a>
The location of the file in S3.
*Required*: No
*Type*: [S3Location](aws-properties-iot-stream-s3location.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
