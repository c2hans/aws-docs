---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-otaupdate-awsjobpresignedurlconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate AwsJobPresignedUrlConfig
<a name="aws-properties-iot-otaupdate-awsjobpresignedurlconfig"></a>

Configuration information for pre-signed URLs. Valid when `protocols` contains HTTP.

## Syntax
<a name="aws-properties-iot-otaupdate-awsjobpresignedurlconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-otaupdate-awsjobpresignedurlconfig-syntax.json"></a>

```
{
  "[ExpiresInSec](#cfn-iot-otaupdate-awsjobpresignedurlconfig-expiresinsec)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-iot-otaupdate-awsjobpresignedurlconfig-syntax.yaml"></a>

```
  [ExpiresInSec](#cfn-iot-otaupdate-awsjobpresignedurlconfig-expiresinsec): {{Integer}}
```

## Properties
<a name="aws-properties-iot-otaupdate-awsjobpresignedurlconfig-properties"></a>

`ExpiresInSec`  <a name="cfn-iot-otaupdate-awsjobpresignedurlconfig-expiresinsec"></a>
How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 1800 seconds. Pre-signed URLs are generated when a request for the job document is received.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
