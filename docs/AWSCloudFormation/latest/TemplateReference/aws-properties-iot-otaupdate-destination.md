---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-otaupdate-destination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate Destination
<a name="aws-properties-iot-otaupdate-destination"></a>

Describes the location of the updated firmware.

## Syntax
<a name="aws-properties-iot-otaupdate-destination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-otaupdate-destination-syntax.json"></a>

```
{
  "[S3Destination](#cfn-iot-otaupdate-destination-s3destination)" : {{S3Destination}}
}
```

### YAML
<a name="aws-properties-iot-otaupdate-destination-syntax.yaml"></a>

```
  [S3Destination](#cfn-iot-otaupdate-destination-s3destination): {{
    S3Destination}}
```

## Properties
<a name="aws-properties-iot-otaupdate-destination-properties"></a>

`S3Destination`  <a name="cfn-iot-otaupdate-destination-s3destination"></a>
Describes the location in S3 of the updated firmware.
*Required*: No
*Type*: [S3Destination](aws-properties-iot-otaupdate-s3destination.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
