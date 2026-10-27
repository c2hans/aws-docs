---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-otaupdate-filelocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate FileLocation
<a name="aws-properties-iot-otaupdate-filelocation"></a>

The location of the OTA update.

## Syntax
<a name="aws-properties-iot-otaupdate-filelocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-otaupdate-filelocation-syntax.json"></a>

```
{
  "[S3Location](#cfn-iot-otaupdate-filelocation-s3location)" : {{S3Location}},
  "[Stream](#cfn-iot-otaupdate-filelocation-stream)" : {{Stream}}
}
```

### YAML
<a name="aws-properties-iot-otaupdate-filelocation-syntax.yaml"></a>

```
  [S3Location](#cfn-iot-otaupdate-filelocation-s3location): {{
    S3Location}}
  [Stream](#cfn-iot-otaupdate-filelocation-stream): {{
    Stream}}
```

## Properties
<a name="aws-properties-iot-otaupdate-filelocation-properties"></a>

`S3Location`  <a name="cfn-iot-otaupdate-filelocation-s3location"></a>
The location of the updated firmware in S3.
*Required*: No
*Type*: [S3Location](aws-properties-iot-otaupdate-s3location.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Stream`  <a name="cfn-iot-otaupdate-filelocation-stream"></a>
The stream that contains the OTA update.
*Required*: No
*Type*: [Stream](aws-properties-iot-otaupdate-stream.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
