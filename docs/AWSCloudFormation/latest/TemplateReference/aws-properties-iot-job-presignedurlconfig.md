---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-job-presignedurlconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Job PresignedUrlConfig
<a name="aws-properties-iot-job-presignedurlconfig"></a>

Configuration for pre-signed S3 URLs.

## Syntax
<a name="aws-properties-iot-job-presignedurlconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-job-presignedurlconfig-syntax.json"></a>

```
{
  "[ExpiresInSec](#cfn-iot-job-presignedurlconfig-expiresinsec)" : {{Integer}},
  "[RoleArn](#cfn-iot-job-presignedurlconfig-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-job-presignedurlconfig-syntax.yaml"></a>

```
  [ExpiresInSec](#cfn-iot-job-presignedurlconfig-expiresinsec): {{Integer}}
  [RoleArn](#cfn-iot-job-presignedurlconfig-rolearn): {{String}}
```

## Properties
<a name="aws-properties-iot-job-presignedurlconfig-properties"></a>

`ExpiresInSec`  <a name="cfn-iot-job-presignedurlconfig-expiresinsec"></a>
How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job document.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-iot-job-presignedurlconfig-rolearn"></a>
The ARN of an IAM role that grants permission to download files from the S3 bucket where the job data/updates are stored. The role must also grant permission for IoT to download the files.
For information about addressing the confused deputy problem, see [cross-service confused deputy prevention](https://docs.aws.amazon.com/iot/latest/developerguide/cross-service-confused-deputy-prevention.html) in the *AWS IoT Core developer guide*.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
