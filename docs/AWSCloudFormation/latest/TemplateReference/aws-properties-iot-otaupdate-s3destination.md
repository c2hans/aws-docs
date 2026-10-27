---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-otaupdate-s3destination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate S3Destination
<a name="aws-properties-iot-otaupdate-s3destination"></a>

Describes the location of updated firmware in S3.

## Syntax
<a name="aws-properties-iot-otaupdate-s3destination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-otaupdate-s3destination-syntax.json"></a>

```
{
  "[Bucket](#cfn-iot-otaupdate-s3destination-bucket)" : {{String}},
  "[Prefix](#cfn-iot-otaupdate-s3destination-prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-otaupdate-s3destination-syntax.yaml"></a>

```
  [Bucket](#cfn-iot-otaupdate-s3destination-bucket): {{String}}
  [Prefix](#cfn-iot-otaupdate-s3destination-prefix): {{String}}
```

## Properties
<a name="aws-properties-iot-otaupdate-s3destination-properties"></a>

`Bucket`  <a name="cfn-iot-otaupdate-s3destination-bucket"></a>
The S3 bucket that contains the updated firmware.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Prefix`  <a name="cfn-iot-otaupdate-s3destination-prefix"></a>
The S3 prefix.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
